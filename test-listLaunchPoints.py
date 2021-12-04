import sys, os, pickle
from pywebostv.connection import WebOSClient
from pywebostv.controls import ApplicationControl

TOKEN_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'lgtv.conf')

def tokenLoad():
	try:
		with open(TOKEN_PATH, 'rb') as f:
			return pickle.load(f)
	except FileNotFoundError:
		return {}

client = WebOSClient('172.0.17.230')
client.connect()
connected = False
for status in client.register( tokenLoad() ):
	if status == WebOSClient.REGISTERED:
		connected = True
		print("Connection OK")

if not connected:
	print('Connection failed')
	sys.exit()

appObj = ApplicationControl(client)
launchPoints = appObj.list_launch_points()
print(launchPoints)
for item in launchPoints:
	print(item['title'], item['largeIcon'])
