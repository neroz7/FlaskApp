# Vulnerability 6: SQL Injection allows with inference to check if a user exists

- Vulnerability: SQL Injection - blind injection
- Where: Field `Username` in login form 
- Impact: Allows to check if a user exists in the database with inference

## Steps to reproduce

1. In login page, insert in the field `Username`: `*username*' and 1=0 -- `
2. Check the message, should say `Username or password are invalid`
3. This time insert in the field `Username`: `*username*' and 1=1 -- ` 
4. If the message `Username or password are invalid` appears then user does not exist, but if you go to a blank homepage then it exists

[(PoC)](SQLvuln6.py)