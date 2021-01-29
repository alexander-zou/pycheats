#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

@File   : load_excel_file.py   
@Author : jiachen.zou@jiiov.com   
@Date   : 2021-01-28 19:38 CST(+0800)   
@Brief  :  

'''

# pip install openpyxl xlrd
# xlrd for older xls files, openpyxl for newer xlsx, xlsm files.

# more info :   https://pypi.org/project/xlrd/
#               https://openpyxl.readthedocs.io/en/stable/           

import xlrd

print( 'use_xlrd.xls :')
wb = xlrd.open_workbook( 'use_xlrd.xls')
print( wb.sheet_names())

sheet = wb.sheet_by_index( 0)
# equivalent to: wb.sheet_by_name( wb.sheet_names()[ 0])

# Travel:
for row_id in range( sheet.nrows):
    print( sheet.row_values( row_id))

# Randomly fetch by coordinates:
print( "Row0, Col2: ", sheet.cell_value( 0, 2))

import openpyxl

print( 'use_openpyxl.xlsx :')
wb = openpyxl.load_workbook( 'use_openpyxl.xlsx', read_only = True, data_only = True)
# data_only is True means prefer to retrieve formula's result calculated by Excel
print( wb.sheetnames)

# Travel:
sheet = wb[ 'Sheet1']
for row in sheet.rows:
    print( [ cell.value for cell in row])

# Randomly fetch by coordinates:
print( "Row1, ColC: ", sheet[ 'C1'].value)

# End of 'load_excel_file.py' 

