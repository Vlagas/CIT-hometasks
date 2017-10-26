import requests

register_link = 'https://cit-home1.herokuapp.com/api/register'
check_link = 'https://cit-home1.herokuapp.com/api/check_me'
json_args = {'first name': 'Vladimir', 'last name': 'Gasta', 'Hello': 'World'}
head = {'content-type': 'application/json'}
r = requests.get(register_link, json=json_args,headers=head)
print(r.json())
check=requests.get(check_link)
print(check.json())