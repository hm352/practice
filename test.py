import librato
import requests
import responses
import time
import pytest 


api = librato.connect('app66128321@heroku.com', '44afa7919166947db3891f778b320ee24ae978b5283c315fe68ec8eee5bcefe0')

compose = 'mean(s("app-availability", "*", {function: "mean", period: "3600"}))'

start_time = int(time.time()) - 8 * 3600

guage = api.get("address_match.get",start_time=start_time, resolution=1)

print('############################################')

print(guage.measurements)

print('############################################')

print(type(guage))

print('############################################')


care_keys = ["measure_time", "value", "count"]
g = guage.measurements['chetwood-integrations']

print(g)

#################### guage testing

def guage_test():
	if (type(guage) == 'librato.metrics.Guage'):
		assert True
	else: 
		assert False 


print('############################################')

m_list= []

m_dict= {}

################## iterating through dictionary

for i, j in enumerate(g):
	for k,v in j.items():
		m_list.append(v)

d = list()

for i, j in enumerate(g):

   _d = {k: v for k, v in j.items() if k in care_keys}
   d.append(_d)
 

def pytest_is_list():
	if(type(d)==list):
		assert True
	else:
		assert False