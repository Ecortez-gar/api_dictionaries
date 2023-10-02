#rest apis
#Application program interface
import requests# request something from the internet
import json #javascript object notation

response = requests.get("https://randomuser.me/api/")
# print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']
print(title)
first = response.json()['results'][0]['name']['first']
print(first)
last = response.json()['results'][0]['name']['last']
print(last)
email = response.json()['results'][0]['email']
print(email)
phone_number = response.json()['results'][0]['phone']
print(phone_number)
city = response.json()['results'][0]['location']['city']
print(city)
postal_code = response.json()['results'][0]['location']['postcode']
print(postal_code)
street_adress = response.json()['results'][0]['location']['street']
print(street_adress)
dob = response.json()['results'][0]['dob']['date']
print(dob)
login = response.json()['results'][0]['login']['uuid']
print(login)
age = response.json()['results'][0]['dob']['age']
print(age)

