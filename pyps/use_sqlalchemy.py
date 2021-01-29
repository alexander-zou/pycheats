#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_sqlalchemy.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-29 12:07 CST(+0800)   
@Brief  :  

'''

# pip install SQLAlchemy pymysql
# pymysql is needed for connecting to mysql server

# more info:    https://docs.sqlalchemy.org/en/13/core/tutorial.html
#               https://docs.sqlalchemy.org/en/13/orm/tutorial.html

import sqlalchemy
from sqlalchemy import sql

# Create or open sqlite db:
engine = sqlalchemy.create_engine( 'sqlite:///use_sqlalchemy.db', echo = False)
# echo set to True to print detailed communication log
# absolute path shall be like: 'sqlite:////use_sqlalchemy.db' or 'sqlite:///C:\\use_sqlalchemy.db'
# to connect to mysql server with pymysql, use url like: 'mysql+pymysql://User:Pass@Server:Port/DB_Name'

# Create Tables:
metadata = sqlalchemy.MetaData()
table = sqlalchemy.Table( 'Table5', metadata,
            sqlalchemy.Column( 'id', sqlalchemy.Integer, primary_key = True),
            sqlalchemy.Column( 'name', sqlalchemy.String, nullable = False),
            sqlalchemy.Column( 'test score', sqlalchemy.Float, default = 0)
        )
metadata.create_all( engine) # create all tables in engine, if not already exists

# Fetch existing tables:
conn = engine.connect()
meta = sqlalchemy.MetaData()
meta.reflect( engine)
print( meta.tables.keys())      # tables is immutabledict
table = meta.tables[ 'Table5'] # get Table() instance

# Insert:
insert = table.insert()
conn.execute( insert.values( name = 'Suzumiya'))
conn.execute( insert.values( { 'name' : 'Kyon', 'test score' : 59.9}))
conn.execute( insert.values( ( None, 'Nagato', 99.99)))
conn.execute( insert.values( [
                                { 'name' : 'Asahina', 'test score' : 96.0},
                                { 'name' : 'Koizumi', 'test score' : 80}
                            ])
            )

# Select:
select = table.select()
for row in conn.execute( select):
    print( row[ 0], row[ 'name'], row)

print( ">>> SELECT * FROM Table5 WHERE name = 'Kyon'")
result = conn.execute(
                select.where( table.c.name == 'Kyon')
            ).fetchall()
print( result)

# Column Name with special charactor:
print( ">>> SELECT * FROM Table5 WHERE `test score` < 60")
print( conn.execute(
            select.where( sqlalchemy.Column( 'test score') < 60)
        ).fetchall()
)

# 'AND' and 'OR':
print( ">>> SELECT * FROM Table5 WHERE name like 'K%' AND id <= 2")
condition = sqlalchemy.sql.and_( table.c.name.like( 'K%'), table.c.id <= 2)
print( conn.execute( select.where( condition)).fetchall())

# Update:
update = table.update()
print( ">>> UPDATE Table5 SET name = 'Tanikawa' WHERE name = 'Kyon'")
conn.execute( update.where( table.c.name == 'Kyon').values( name = 'Tanikawa'))

# Delete:
print( ">>> DELETE FROM Table5 WHERE id = 4")
conn.execute( table.delete().where( table.c.id == 4))

# Final result:
print( ">>> SELECT * FROM Table5")
print( conn.execute( table.select()).fetchall())

import os
try:
    os.remove( 'use_sqlalchemy.db')
except:
    pass

# End of 'use_sqlalchemy.py' 

