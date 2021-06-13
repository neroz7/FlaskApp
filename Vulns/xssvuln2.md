# Vulnerability 2: The `/edit_post` resource isn't subject to authentication and `Private` blogposts are accessible by `id` only

- Vulnerability: Stored XSS 
- Where: `/edit_post` resource 
- Impact: Attacker can inject javascript on another user's `blogpost` , EVERY blogpost as a resource is reachable through `edit_post` without authentication being required, the python script gets us access a special blogpost by the `admin` and injects javascript into another blogpost

## Steps to reproduce

1. Put the website url + `/edit_post?id=1` on your browser to get the secret admin post
2. Pick another blogpost to edit: url + `edit_post?id=2` 
3. Inject malicious javascript `repeat every occurance of ' in your script to escape the filters`

[(POC)](xssvuln2.py)