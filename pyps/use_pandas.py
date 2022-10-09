#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : use_pandas.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-29 17:12 CST(+0800)   
@Brief  :  

'''

# pip install pandas
# more info: https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started

import pandas

# Create DataFrame:
data_frame = pandas.DataFrame( [['ant', 'bee', 'cat'], ['dog', None, 'fly']], columns = [ 'ColumnA', 'ColumnB', 'ColumnC'])
print( data_frame)
print( 'data_frame.shape: ', data_frame.shape)

# Random Access and Check for NULL data:
print( pandas.isnull( data_frame))
print( pandas.isnull( data_frame.at[ 1, 'ColumnB']))
# opposite to pandas.notnull()

# Load data:
data_frame = pandas.read_csv( 'use_csv.csv')
# to read all cells(except for empty cells) as str:
#   data_frame = pandas.read_csv( 'use_csv.csv', dtype=str)

# to load data from database:
'''
import sqlalchemy
engine = sqlalchemy.create_engine( ...) # see use_sqlalchemy.py for more info
data_frame = pandas.read_sql_table( 'Table Name', engine)
date_frame = pandas.read_sql_query( 'SQL Statement', engine)
'''

# Statistics:
ages = data_frame[ 'Age']
print( 'Age Statistics: ', ages.mean(), ages.std())

# Append: 
# data_frame = data_frame.append( { 'Name':'Daisy', 'Age':30}, ignore_index=True) # DEPRECATED!!!
data_frame = pandas.concat( [ data_frame, pandas.DataFrame( [[ 'Daisy', 30]], columns=[ 'Name', 'Age'])])

# Travel:
for idx, row in data_frame.iterrows():
    print( idx, ( row[ 'Name'], row[ 'Role'], row[ 'Age']))

# Counting:
print( "number of age data: ", data_frame[ 'Age'].count())
print( "number of unique age: ", data_frame[ 'Age'].nunique())

# Filter Rows:
elder = data_frame[ data_frame[ 'Age'] > 28]
print( 'number of name data (Age>28): ', elder.count()[ 'Name']) # equivalent to: elder[ 'Name'].count()
print( 'number of role data (Age>28): ', elder.count()[ 'Role'])

# Retrieve Rows:
print( 'Retrieve Row -1:')
print( data_frame.iloc[ -1])
print( 'Retrieve Row 0, 1, 3:')
print( data_frame.iloc[ [ 0, 1, 3]])
print( 'Retrieve Row 0, 2:')
print( data_frame.iloc[ ::2])

# Calculate Column:
data_frame[ 'Age-Last-Year'] = data_frame[ 'Age'] - 1
data_frame[ 'Role'].fillna( '???', inplace = True)
data_frame[ 'Name+Role'] = data_frame[ 'Name'] + ' : ' + data_frame[ 'Role']

# Plotting:
try:
    import matplotlib.pyplot as plt
    data_frame.plot.scatter( x='Role', y='Name', c='Age', colormap='jet', title='Scatter Graph')
    plt.show()
except: pass

# Drop Column:
data_frame.drop( [ 'Role', 'Age'], axis = 1, inplace = True)

# Output:
#data_frame.to_excel( 'output.xls')
#data_frame.to_csv( 'output.csv')
#data_frame.to_csv( 'output.csv', encoding='utf-8-sig') # use BOM to avoid Excel codec confusion
print( data_frame)

# From Dictionary:
data_frame = pandas.DataFrame( {
    'Column1' : [ 1, 2, 3, 4, 7, 9],
    'Column2' : [ 'XYZW', 'XXXXX', 'A', 'A', 'ABC', 'CBA']
})
print( 'Original Order:\n', data_frame)

# Sorting:
print( 'Sort By Column2:\n', data_frame.sort_values( by='Column2'))
print( 'Sort By Column2+Column1, Descending:\n', data_frame.sort_values( by=['Column2','Column1'], ascending=False))
print( 'Sort By len() of Column2:\n', data_frame.sort_values( by='Column2', key=lambda col:col.apply( lambda s:len( s))))

# End of 'use_pandas.py' 

