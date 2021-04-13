import json
import boto3

""" Function for copying the objects to S3:prod-bui-backup as soon as objects uploaded on S3:prod-bui
    Managed By: Jignesh Polara
"""

# boto3 S3 initialization
s3_client = boto3.client("s3")


def lambda_handler(event, context):
   destination_bucket_name = 'jpolara1-destination-bucket'

   # event contains all information about uploaded object
   print("Event :", event)

   # Bucket Name where file was uploaded
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path)
   file_key_name = event['Records'][0]['s3']['object']['key']

   # Copy Source Object
   copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

 
   try:
      print ("Using waiter to waiting for object to persist through s3 service")
      waiter = s3_client.get_waiter('object_exists')
      waiter.wait(Bucket=source_bucket_name, Key=file_key_name)
      # S3 copy object operation
      s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)
      print("Source Bucket: {0}, Object Name : {1}".format(source_bucket_name, file_key_name))
      print("Destination Bucket: {0}, Object Name : {1}".format(destination_bucket_name, file_key_name))
      print("Object copied successfully...")

   except Exception as err:
      print ("Error -"+str(err))
      return e