# Vulnerability 1: SQL Injection allows to change a readonly variable(e.g username) if no friends are added
    
- Vulnerability: SQL Injection
- Where: Field `About` in Update profile form 
- Impact: Allows to change a readonly variable

## Steps to reproduce

1. Login with an new account (no friends or posts)
2. Insert current and new password correctly
3. Insert `', username = '*pretended username* '` in About Field and click update profile
4. Refresh page to login again with the new username

[(PoC)](SQLvuln1.py)