import requests

x = requests.get('http://localhost:3000/')

print(x.text)

y = requests.post('http://localhost:3000/', json={'key': 'python post'})

print(y.text)

print('end')
