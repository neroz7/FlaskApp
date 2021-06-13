# Vulnerability 4: Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and this input is being reflected when the victim accesses `/pending_requests`resource

- Vulnerability: Stored XSS 
- Where: `name` field in `/update_profile's` multipart post-form
- Impact: The malicious javascript that the attacker stored on the `name` field of his profile will be executed on victims browser when he accesses `/pending_requests` to check if he has received any friend requests
## Steps to reproduce

1. Create an account 
2. Click on your `profile`, write the prefered javascript on the `name` field and save it, there is no char limit
3. Click on `add friend` 
3. Type the `username` that you want to attack
4. Your malicious javascript will be executed on the victims browser when he acceses his `pending requests`


[(POC)](xssvuln4.py)