# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:36:59 2017

@author: kvan
"""

import pymssql
import pandas as pd

## instance a python db connection object- same form as psycopg2/python-mysql drivers also
conn = pymssql.connect(server="localhost", user="sa1",password="reports", port=1433)  # You can lookup the port number inside SQL server. 

## Hey Look, college data
stmt = "SELECT * FROM pack..masterbox"
# Excute Query here
df = pd.read_sql(stmt,conn)

print(df.head(5))
print("done")
