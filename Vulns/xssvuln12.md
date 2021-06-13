# Vulnerability 12: Attacker can upload any malicious script to the server as an `image` via  the `update_profile`form, these scripts can then be loaded by the attacker using `create_blogpost` and be reflected to victims who enter the server's main page

- Vulnerability: Stored XSS 
- Where: `photo` input field in the `/update_profile` multipart form post and `create_post` form
- Impact: The attacker is able to inject malicious javascript of `BIG` sizes instead of images to be stored as his profile picture, the script gets stored in the webserver and can later be loaded by the attacker exploiting other vulnurabilities

1. Register an account 
2. Click on `update profile` 
3. Load the malicious script as an image for the attacker's profile
4. Inspect elements of the updated webpage
5. Find the `url` where the server stored your script (it's in `/static/photos`)
6. Copy this `url` and make a new blogpost where you inject the following script : `<script src="http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt/` + `url` `</script>`
7. The script injected in the `blogpost` is now loading the javascript previously stored as an image and will be executed on a victim's browser who accesses the default server page


[(POC)](xssvuln12.py)