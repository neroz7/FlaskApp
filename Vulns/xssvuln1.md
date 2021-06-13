# Vulnerability 1: Attacker can bypass the simple filter and inject javascript in `/create_post` which is then reflected in the server's `default page`

- Vulnerability: Stored XSS
- Where: `content` field of `/create_post` post-form 
- Impact: The python script creates a 30 min pastebin to collect user data, the injected script is executed on every client's browser upon visit, current payload's javascript is stealing client cookies discreetly via `XMLHttpRequest`. With a user's cookies, a malicious attacker can impersonate as that user and send requests to `state dependent services` who will interpret these requests as coming from the victim

## Steps to reproduce

1. Register as a user via 
2. Access `New post` by clicking on it
3. Inject malicious javascript `repeat every occurance of ' in your script to escape the filters`

[(POC)](xssvuln1.py)