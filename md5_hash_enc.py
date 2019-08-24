#USAGE : python md5_hash_enc.py 1 100
import hashlib
import sys

LOWER_LIMIT=int(sys.argv[1])
UPPER_LIMIT=int(sys.argv[2])
for i in range(UPPER_LIMIT-LOWER_LIMIT):
	print hashlib.md5(str(i)).hexdigest()

