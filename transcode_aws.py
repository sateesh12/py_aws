#!/usr/bin/python
#Author: Sateesh
#Purpose: Transcode Video  using AWS.

import boto
import sys
from boto.elastictranscoder.layer1 import ElasticTranscoderConnection
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

#Method
#Inputs: bucket_name, the bucket into which you want to add files.
#        key_name, a unique name for the key
#        file_name, path of the actual video file, which needs to be streamed to S3.
#Output:
#       0, successfully sent the file.
#      -1, Error case.
def store_data_into_s3(bucket_name, key_name,file_name):
	s3 = boto.connect_s3()
	bucket = s3.lookup(bucket_name)
	if bucket:
		key = bucket.new_key(key_name)
		key.set_contents_from_filename(file_name)
		return 0
	else:
		create_bucket(bucket_name)
		return -1


#Method
#	Create a pipeline
#	Create pre-set 
#	Create job
#Inputs: 
#Outputs:
#	 0, success
#	-1, Failure to connect to Elastic Transcoder
#       -2, Failure to create pipe-line
#       -3, Failure to create job
#Note:
#    As of now pipeline id is extracted from the web, need to find how to get it from script !
def transcode(input_bucket, output_bucket,input_filename,output_filename):
	transcode_input = {'Container': 'auto', 'Key': input_filename,'Resolution': 'auto', 'AspectRatio': 'auto', 'FrameRate': 'auto', 'Interlaced': 'auto'}
	transcode_output = {'Rotate': 'auto', 'PresetId': '1351620000001-100080',  'Key': output_filename}
# Connect to the elastic trans-coder.
	et = boto.elastictranscoder.layer1.ElasticTranscoderConnection()
	if et:
		pipeline = et.create_pipeline("sateesh_from_script_2",input_bucket, output_bucket,"arn:aws:iam::457658703256:role/Add_ET_As_Trusted", {"Progressing":"","Completed":"","Warning":"","Error":""})
		if pipeline:
			job = et.create_job("1384084736575-ih4r4t",transcode_input,transcode_output)
			if job:
				return 0
			else:
				return -3
		else:
			return -2
	else:
		return -1	

#Main
retval = create_bucket("sateesh_video_transcode_primary")
print("Debugging Message 1 : " +str(retval))

retval = store_data_into_s3("sateesh_video_transcode_primary", "test","./2013-04-29 22.47.20.mp4")
print("Debugging Message 2 : " +str(retval))

retval = transcode("sateesh_video_transcode_primary","sateesh_video_transcode_primary","test","11_nov_2013_from_script")
print("Debugging Message 3 : " +str(retval))
