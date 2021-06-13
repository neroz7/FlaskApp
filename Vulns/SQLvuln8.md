# Vulnerability 8: SQL Injection allows to create multiple posts at for other users 

- Vulnerability: SQL Injection 
- Where: Field `Content` in create post form 
- Impact: Allows to create multiple posts at once and for other users

# Steps to reproduce

1. Login with an account
2. Go to create a post
3. Insert in field `Content`: `hello', 'Public'), ('test1', 'hacked', 'Public')  -- `
4. Check if posts were created

[(PoC)](SQLvuln8.py)