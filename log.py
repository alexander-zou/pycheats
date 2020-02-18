#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging

def simple_use():
    # basicConfig 必须最先调用，否则彻底不生效
    logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug( "this line won't show!")
    logging.info( 'sample log line: int = %d, float = %f' % ( 123, 4.56))

def oo_use():
    LOG_FILE_NAME = "test.log"
    logger = logging.getLogger( 'log-test')
    formatter = logging.Formatter( '%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler( filename = LOG_FILE_NAME)
    handler.setFormatter( formatter)
    logger.addHandler( handler)

    logger.debug( '0000000')
    logger.info( '11111')
    # 默认级别为WARNING:
    logger.warning( '22222')
    logger.error( '33333333')
    logger.critical( '!!!!!!!!!!')

    with open( LOG_FILE_NAME, 'r') as f:
        print( "====== '" + LOG_FILE_NAME + "' =======")
        print( f.read())
        print( "=========================")
    import os
    os.remove( LOG_FILE_NAME)

oo_use()
simple_use()




