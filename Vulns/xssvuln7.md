# Vulnerability 7: Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, the malicious javascript will be reflected on the victim's `/friends`list

- Vulnerability: Stored XSS 
- Where: `name` field in `/update_profile's` multipart post-form
- Impact: The malicious javascript that the attacker stored on the `name` field of his profile will be executed on victims browser when he accesses `/friends`, should the victim accept the attacker's friend request
## Steps to reproduce

1. Create an account 
2. Click on your `profile`, write the prefered javascript on the `name` field and save it, there is no char limit
3. Click on `add friend` 
3. Type the `username` that you want to attack
4. Wait for the victim to accept your friend request
5. Your malicious javascript will now run when the victim sends a request to `friends`

[(POC)](xssvuln7.py)
