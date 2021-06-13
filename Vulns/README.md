# Project1-Group39

Group Image available [here](http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt/)

## SQL Injection

- Vulnerability 1: SQL Injection allows to change a readonly variable(e.g username) if no friends are added [(link)](SQLvuln1.md)
- Vulnerability 2: SQL Injection allows to login into any account including admin accounts without entering the password [(link)](SQLvuln2.md)
- Vulnerability 3: SQL Injection that allows to edit posts from another person [(link)](SQLvuln3.md)
- Vulnerability 4: SQL Injection that allows to change any user account info like the password [(link)](SQLvuln4.md)
- Vulnerability 5: SQL Injection that allows to piggyback any mysql query [(link)](SQLvuln5.md)
- Vulnerability 6: SQL Injection allows with inference to check if a user exists [(link)](SQLvuln6.md)
- Vulnerability 7: SQL Injection allows with network delays to check values from the DB (e.g a char from a password) [(link)](SQLvuln7.md)
- Vulnerability 8: SQL Injection allows to create multiple posts at for other users [(link)](SQLvuln8.md)
- Vulnerability 9: SQL Injection in my friends page allows to leak database information [(link)](SQLvuln9.md)
- Vulnerability 10: SQL Injection in register form allows multiple registers [(link)](SQLvuln10.md)
- Vulnerability 11: SQL Injection in add friend page allows to infer user password [(link)](SQLvuln11.md)

## XSS

- Vulnerability 1: Attacker can bypass the simple filter and inject javascript in `/create_post` which is then reflected in the server's `default page` [(link)](xssvuln1.md)
- Vulnerability 2: The `/edit_post` resource isn't subject to authentication and `Private` blogposts are accessible by `id` only [(link)](xssvuln2.md)
- Vulnerability 3: Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and this input is being reflected when the victim accesses `/pending_requests`resource [(link)](xssvuln3.md)
- Vulnerability 4: Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and this input is being reflected when the victim accesses `/pending_requests`resource [(link)](xssvuln4.md)
- Vulnerability 5: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, this javascript is then reflected on the victims browser when he accesses `pending requests` [(link)](xssvuln5.md)
- Vulnerability 6: Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, malicious javascript will be reflected on the victim's `/friends`list [(link)](xssvuln6.md)
- Vulnerability 7: Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, the malicious javascript will be reflected on the victim's `/friends`list [(link)](xssvuln7.md)
- Vulnerability 8: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim's `/friends` list [(link)](xssvuln8.md)
- Vulnerability 9: Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, further searches for the attacker's username via `/search_friend` will reflect the malicious script on victims browser [(link)](xssvuln9.md)
- Vulnerability 10: Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, further searches for the attacker's username via `/search_friend` will reflect the malicious script on victims browser [(link)](xssvuln10.md)
- Vulnerability 11: Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim's browser whenever he searches for the attacker's username via `search_friend` [(link)](xssvuln11.md)
- Vulnerability 12: Attacker can upload any malicious script to the server as an `image` via  the `update_profile`form, these scripts can then be loaded by the attacker using `create_blogpost` and be reflected to victims who enter the server's main page [(link)](xssvuln12.md)
