import librato
import requests

api = librato.connect('app66128321@heroku.com', '44afa7919166947db3891f778b320ee24ae978b5283c315fe68ec8eee5bcefe0')

def test_librato_api_working():

	if (api.status_code()==200):
		
		assert True

	else:
		assert False