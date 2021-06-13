# Vulnerability 11: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim's browser whenever he searches for the attacker's username via `search_friend`

- Vulnerability: Stored XSS 
- Where: `username` input field in the `/register` form post
- Impact: The malicious javascript that the attacker registered with on the `username` field, should the victim accept the attacker's friend request, will be reflected on the victim's browser should he use `search_friend` to find the attacker's username
## Steps to reproduce

1. Register an account with a malicious 20 char length javascript `username`
2. Click on `add friend` 
3. Type the `username` that you want to attack
4. Wait for the victim to accept your request
5. Wait for victim to search for the attacker's username
6. Your malicious 20 char javascript will now run when the victim searches the attackers profile via `/search_friend`


[(POC)](xssvuln11.py)