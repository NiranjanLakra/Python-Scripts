
# USAGE : python base64encoder.py numbers2.txt 2

import base64
import sys
with open(sys.argv[1], 'r') as file:
	t=file.readlines()
	for f in t:
		temp=f
		for i in range (0,int(sys.argv[2])):
			temp=base64.b64encode(temp)
		print(temp)
