# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:31:35 2021

@author: Peter
"""

import pymysql
import paramiko
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser
import os

home = expanduser('~')
file = 'file_openssh'
folder_path = r'PATH_TO_RSA'
pkeyfilepath = os.path.join(folder_path, file)
ssh_pw = 'PASSWORD'
mypkey = paramiko.RSAKey.from_private_key_file(pkeyfilepath, password = ssh_pw)
# if you want to use ssh password use - ssh_password='your ssh password', below

sql_hostname = 'HOST_ADDRESS(aws.com)'
sql_username = 'USER_NAME'
sql_password = 'SQL_PW_OF_DB'
sql_main_database = 'DB_NAME'
sql_port = "port_number" #(3306,3008 etc.) # just an int

ssh_host = 'SSH_IP'
ssh_user = 'USER_NAME'
ssh_port = "ssh_port_Number" #i.e. 21 # just an int

def query_db(query):

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)
        
        data = pd.read_sql_query(query, conn)
        conn.close()
        
        return data