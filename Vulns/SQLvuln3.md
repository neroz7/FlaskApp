# Vulnerability 3: SQL Injection that allows to edit posts from another person

- Vulnerability: SQL Injection
- Where: Field `Content` in edit post form 
- Impact: Allows to change posts from another person

## Steps to reproduce

1. Login into an account with at least one post
2. Click to edit post
3. Insert into the field `Content`:  `not mine', type = 'public' where author = '*pretended author*' and post_id=*post_id* -- `
4. Update post and verify it in the homepage

[(PoC)](SQLvuln3.py)