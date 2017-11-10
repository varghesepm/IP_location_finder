#!/usr/local/bin/python3

import requests
import subprocess

subprocess.call('clear',shell=True)

msg = 'python script to fetch ip geodata'

print()
print(msg.upper())
print('-' * len(msg))
print()

ipSearch = input('Enter Your Ip-Address : ')

if ipSearch:
 try:

  searchString = 'https://freegeoip.net/json/'+ipSearch
  reply = requests.get(searchString)
  ipJson = reply.json()


  city = ipJson.get('city','------')
  country_code = ipJson.get('country_code','None')
  country_name = ipJson.get('country_name','None')
  ip  = ipJson.get('ip','None')
  latitude = ipJson.get('latitude','None')
  longitude = ipJson.get('longitude','None')
  metro_code = ipJson.get('metro_code','None')
  region_code = ipJson.get('region_code','None')
  region_name = ipJson.get('region_name','None')
  time_zone = ipJson.get('time_zone','None')
  zip_code = ipJson.get('zip_code','None')

  print()
  print('{:<14}{:^3}{}'.format('IP-Address',':',ip))
  print('{:<14}{:^3}{}'.format('City Name',':',city))
  print('{:<14}{:^3}{}'.format('Country Code',':',country_code))
  print('{:<14}{:^3}{}'.format('Country Name',':',country_name))
  print('{:<14}{:^3}{}'.format('Latitude',':',latitude))
  print('{:<14}{:^3}{}'.format('Longitude',':',longitude))
  print('{:<14}{:^3}{}'.format('Region Code',':',region_code))
  print('{:<14}{:^3}{}'.format('Region Name',':',region_name))
  print('{:<14}{:^3}{}'.format('Time Zone',':',time_zone))
  print('{:<14}{:^3}{}'.format('Zip Code',':',zip_code))
  print()

 except Exception as err:
  print('Error :',err)

else:
 print('Ip-Address Is Empty.')
