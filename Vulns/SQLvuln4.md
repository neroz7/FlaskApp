# Vulnerability 4: SQL Injection that allows to change any user account info like the password

- Vulnerability: SQL Injection 
- Where: Field `Name` in update profile form 
- Impact: Allows to change any user account info including password

## Steps to reproduce

1. Login with any account
2. Go to update profile
3. Insert current and new password of your account
4. Insert in the field `Name`:  `',  username='investor', password='*new password*' where username='investor' -- '`
5. Update profile
6. Login with new password to verify

[(PoC)](SQLvuln4.py)