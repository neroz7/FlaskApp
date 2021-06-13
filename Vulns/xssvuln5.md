# Vulnerability 5: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, this javascript is then reflected on the victims browser when he accesses `pending requests`

- Vulnerability: Stored XSS 
- Where: `username` input field in the `/register` form post
- Impact: The malicious javascript that the attacker registered  as his `username` field  will be executed on victims browser when he accesses `/pending_requests` to check if he has received any friend requests
## Steps to reproduce

1. Register an account with a malicious 20 char length javascript `username`
2. Click on `add friend` 
3. Type the `username` that you want to attack
4. Your 20 char javascript  will be executed on the victims browser when he acceses his `pending requests` 


[(POC)](xssvuln5.py)