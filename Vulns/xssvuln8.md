# Vulnerability 8: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim's `/friends` list

- Vulnerability: Stored XSS 
- Where: `username` input field in the `/register` form post
- Impact: The malicious javascript that the attacker registered with on the `username` field of his profile will be executed on victims browser when he accesses `/friends`, should the victim accept the attacker's friend request
## Steps to reproduce

1. Register an account with a malicious 20 char length javascript `username`
2. Click on `add friend` 
3. Type the `username` that you want to attack
4. Wait for the victim to accept your request
4. Your 20 char javascript  will be executed on the victims browser when he accesess his friend list via `/friends` 


[(POC)](xssvuln8.py)