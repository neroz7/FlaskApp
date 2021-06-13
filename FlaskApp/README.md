# Fix Report of Group 39

## Phase 2 Deadline: 08Nov2020-23h59m)

### SQL Injection

- _Vulnerability 1: SQL Injection allows to change a readonly variable(e.g username) if no friends are added_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `update_user` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 2: SQL Injection allows to login into any account including admin accounts without entering the password_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `login_user` and `get_all_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 3: SQL Injection that allows to edit posts from another person_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `edit_post` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 4: SQL Injection that allows to change any user account info like the password_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `update_user` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 5: SQL Injection that allows to piggyback any mysql query_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `update_user` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 6: SQL Injection allows with inference to check if a user exists_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `login_user` and `get_all_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 7: SQL Injection allows with network delays to check values from the DB (e.g a char from a password)_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `login_user` and `get_all_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 8: SQL Injection allows to create multiple posts at for other users_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `new_post` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 9: SQL Injection in my friends page allows to leak database information_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `get_friends` and `get_all_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 10: SQL Injection in register form allows multiple registers_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `register_user` and `commit_results` by separating user supplied params from query and using prepared statements.

- _Vulnerability 11: SQL Injection in add friend page allows to infer user password_
  - Root cause: the source of this vulnerability was improper construction of query string by mixing user input with original query.
  - Changes: Fixed function `get_user` and `get_all_results` by separating user supplied params from query and using prepared statements.

### XSS

- Vulnerability 1:  Attacker can bypass the simple filter and inject javascript in /create_post which is then reflected in the server’s default page
  - Root cause: The content provided by the attacker is not properly escaped before being given to the html content the victim's browser will load
  - Changes: Changed mapping function `create_post` in `views.py` to escape the content provided by the user before it is sent to the backend to make a new post

- Vulnerability 2:  The /edit_post resource isn’t subject to authentication and Private blogposts are accessible by id only
  - Root cause: The username of the person requesting to edit a blogpost is not subject to authorization policies regarding the authorship of the blogpost
  - Changes: Changed `get_post` in model.py to take the `username` of the session as an argument and verify this user against the authorship of requested blogpost, if it's not the same author the user cannot edit that blogpost.

- Vulnerability 3:  Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and this input is being reflected when the victim accesses `/pending_requests` resource
  - Root cause: The input field `about` of a profile is reflected when a user loads his pending requests, these attributes aren't being properly escaped after the pending requests of a user are loaded from the DB
  - Changes: Changed `get_pending_requests` in model.py to escape the attribute `content` of all the loaded pending requests before these are sent to the victim's browser
  
- Vulnerability 4:  Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and this input is being reflected when the victim accesses `/pending_requests` resource 
  - Root cause: The input field `name` of a profile is reflected when a user loads his pending requests, these attribute aren't being properly escaped after the pending requests of a user are loaded from the DB
  - Changes: Changed `get_pending_requests` in model.py to escape the attribute `name` of all the loaded pending requests before these are sent to the victim's browser                                

- Vulnerability 5:  Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, this javascript is then reflected on the victims browser when he accesses `pending_requests`
  - Root cause: An attacker has a 20 char limit to register a `username`, dangerous metachars are being allowed in this value which can lead to very short malicious JS scripts to be injected
  - Changes: Changed mapping function `register` in `views.py` to decline the creation of any user whose `username` contains `<>/\.`  

- Vulnerability 6:  Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, malicious javascript will be reflected on the victim’s `/friends` list
  - Root cause: The input field `about` of a profile is reflected when a user loads his friend list, these atributes aren't being properly escaped after the friends of a user are loaded from the DB
  - Changes:  Changed `get_friends` in model.py to escape the attribute `content` of all the loaded friends before these are sent to the victim's browser

- Vulnerability 7:  Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, the malicious javascript will be reflected on the victim’s `/friends` list
  - Root cause: The input field `name` of a profile is reflected when a user loads his friend list, these atributes aren't being properly escaped after the friends of a user are loaded from the DB
  - Changes: Changed `get_friends` in model.py to escape the attribute `name` of all the loaded friends before these are sent to the victim's browser

- Vulnerability 8:  Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim’s `/friends` list
  - Root cause: An attacker has a 20 char limit to register a `username`, dangerous metachars are being allowed in this value which can lead to very short malicious JS scripts to be injected
  - Changes: Changed mapping function `register` in `views.py` to decline the creation of any user whose `username` contains `<>/\.`  

- Vulnerability 9:  Attacker can inject javascript into the `about` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, further searches for the attacker’s `username` via `/search_friend` will reflect the malicious script on victims browser
  - Root cause: The input field `about` of a profile is reflected when a user searches for his friend, these atributes aren't being properly escaped after the friend the victim searched for is pulled from the DB
  - Changes: Since searching for a friend uses the same backend function `get_friends` in `model.py` only it narrows the query from loading all friends, to a specified one, the earlier changes made to escape the `content` attribute of all loaded friends also fixed this vulnerability.
  
- Vulnerability 10:  Attacker can inject javascript into the `name` input field in the `/update_profile` form, add a victim user as a friend via `/add_friend` and should the victim accept this friend request, further searches for the attacker’s `username` via `/search_friend` will reflect the malicious script on victims browser
  - Root cause: The input field `name` of a profile is reflected when a user searches for his friend, these atributes aren't being properly escaped after the friend the victim searched for is pulled from the DB
  - Changes: Since searching for a friend uses the same backend function `get_friends` in `model.py` only it narrows the query from loading all friends, to a specified one, the earlier changes made to escape the `name` attribute of all loaded friends also fixed this vulnerability.
  
- Vulnerability 11:  Attacker can register as an account whose `username` is a 20 char length javascript, and send a friend request to a victim, should the victim accept this friend request, the malicious javascript will be reflected on the victim’s browser whenever he searches for the attacker’s username via `/search_friend`
  - Root cause:  An attacker has a 20 char limit to register a `username`, dangerous metachars are being allowed in this value which can lead to very short malicious JS scripts to be injected
  - Changes: Changed mapping function `register` in `views.py` to decline the creation of any user whose `username` contains `<>/\.` 
  
- Vulnerability 12:   Attacker can upload any malicious script to the server as an image via the `update_profile` form, these scripts can then be loaded by the attacker using `/create_blogpost` and be reflected to victims who enter the server’s main page
  - Root cause: Arbitrary file extensions are able to be uploaded unto the server as a user `photo`
  - Changes: Changed mapping function `update_profile` in `views.py` to refuse requests  whose `photo` uploads aren't `.jpg` or `.png`, and properly escaped the `content` of a blogpost, disabling scripts that would otherwise call the malicious file from executing on the victim's browser.
  
