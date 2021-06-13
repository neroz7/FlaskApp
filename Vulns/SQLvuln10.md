# Vulnerability 10: SQL Injection in register form allows multiple registers

- Vulnerability: SQL Injection
- Where: `password` field in register form
- Impact: Allows multiple registers to be executed at once

## Steps to reproduce

1. Insert `username` = `123` and `password` = `123'), ('1234', '1234`
2. Login as user `1234`

[(POC)](SQLvuln10.py)
