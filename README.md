py_aws
======

Transcoding Video using AWS

The purpose of this project is to demonstrate a transcode of video from one encoding type to another. 
The steps are as follows: 
Phase-1
1. Create a bucket, this is a one time task,
2. Add source video files into the S3 bucket 
3. Create a pipeline for the transcode 
4. Set up a job based on the destination encoding type.
5. Download the re-encoded video back to HDD
6. Delete the source and destination videos from the S3 bucket to cut-down on billing.
7. 


Phase-2
1. Provide a web front end for the Phase-1
