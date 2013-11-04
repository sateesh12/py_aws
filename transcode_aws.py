#!/usr/bin/python
#Author: Sateesh
#Purpose: Transcode Video  using AWS.

import boto
#Method:
#Inputs: Bucket name to be created.
#Output: If bucket already exists, then return -1 or a -2 , else return 0
def create_bucket(bucket_name):
	s3 = boto.connect_s3()
	bucket = s3.lookup(bucket_name)
	if bucket:
		print("Bucket already exists: " + bucket_name)
		return -1
	else:
		try:
			bucket = s3.create_bucket(bucket_name)
		except:
			print("Bucket name is not unique: " + bucket_name)
			return -2
	return 0



#Main
retval = create_bucket("sateesh_video_transcode_primary")
print("Debugging Message: " +str(retval))

	
