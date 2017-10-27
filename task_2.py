import requests
import json
register_link = 'https://cit-home1.herokuapp.com/api/register'
check_link = 'https://cit-home1.herokuapp.com/api/check_me'
json_args = json.dumps({'first name': 'Vladimir', 'last name': 'Gasta'})
head = {'content-type': 'application/json'}
r = requests.post(register_link, data=json_args,headers=head)
print(r)
check=requests.get(check_link)
print(check.json())