# Vulnerability 5: SQL Injection that allows to piggyback any mysql query

- Vulnerability: SQL Injection 
- Where: Field `Name` in update profile form 
- Impact: Allows to piggyback any mysql query, e.g Drop table or create table

## Steps to reproduce

1. Login with any account
2. Go to update profile
3. Insert current and new password of your account
4. Insert in the field `Name`: `' where username = 'test'; drop table FriendsRequests; -- `
5. Update profile and enter in a page that gives an error due to an inexistint table

[(PoC)](SQLvuln5.py)