#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : chinese_numbers.py   
@Author : zouji   
@Date   : 2023-02-26 15:54    (+0800)   
@Brief  :  

'''

import math

def chinese2int( s, imply_unit=1):
    s = s.strip()
    if len( s) <= 0:
        return 0
    if s.startswith( '负'):
        return - chinese2int( s[ 1:])
    elif s.startswith( '零'):
        return chinese2int( s[ 1:])
    idx = s.rfind( '亿')
    if idx >= 0:
        return chinese2int( s[ 0:idx]) * 100000000 + chinese2int( s[ idx+1:], imply_unit=10000000)
    idx = s.rfind( '万')
    if idx >= 0:
        return chinese2int( s[ 0:idx]) * 10000 + chinese2int( s[ idx+1:], imply_unit=1000)
    idx = max( s.rfind( '千'), s.rfind( '仟'))
    if idx >= 0:
        return chinese2int( s[ 0:idx]) * 1000 + chinese2int( s[ idx+1:], imply_unit=100)
    idx = max( s.rfind( '百'), s.rfind( '佰'))
    if idx >= 0:
        return chinese2int( s[ 0:idx]) * 100 + chinese2int( s[ idx+1:], imply_unit=10)
    idx = max( s.rfind( '十'), s.rfind( '拾'))
    if idx > 0:
        return chinese2int( s[ 0:idx]) * 10 + chinese2int( s[ idx+1:])
    elif idx == 0:
        return 10 + chinese2int( s[ idx+1:])
    return {
        '零': 0, '〇': 0,
        '一': 1, '壹': 1,
        '二': 2, '贰': 2, '两': 2,
        '三': 3, '叁': 3,
        '四': 4, '肆': 4,
        '五': 5, '伍': 5,
        '六': 6, '陆': 6,
        '七': 7, '柒': 7,
        '八': 8, '捌': 8,
        '九': 9, '玖': 9}[ s] * imply_unit

def int2chinese( num):
    chi_chars = [ '零', '一', '二', '三', '四', '五', '六', '七', '八', '九',]
    chi_units = [ '', '十', '百', '千']
    num = int( num)
    def process_section( num, first_section=True):
        if num <= 0:
            return ''
        digits = int( math.log10( num)) + 1
        if digits > 8:
            return process_section( num // 100000000, first_section) + '亿' + process_section( num % 100000000, False)
        elif digits > 4:
            return process_section( num // 10000, first_section) + '万' + process_section( num % 10000, False)
        elif first_section and 10 <= num <= 19:
            if num == 10:
                return chi_units[ 1]
            else:
                return chi_units[ 1] + chi_chars[ num % 10]
        else:
            unit_skipped = False
            result = ''
            for unit in range( digits-1 if first_section else 3, -1, -1):
                n = num // ( 10 ** unit) % 10
                if n <= 0:
                    unit_skipped = True
                else:
                    if unit_skipped:
                        unit_skipped = False
                        result += chi_chars[ 0]
                    result += chi_chars[ n] + chi_units[ unit]
            return result
    if num < 0:
        return '负' + process_section( -num)
    elif num > 0:
        return process_section( num)
    elif num == 0:
        return chi_chars[ 0]


if __name__ == '__main__':
    n = 123456789
    chi = int2chinese( n)
    print( chi)
    print( chinese2int( chi))

# End of 'chinese_numbers.py' 

