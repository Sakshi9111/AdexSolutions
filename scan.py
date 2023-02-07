import boto3

#Create an S3 client
s3 = boto3.client('s3')


BUCKET_NAME = 'adexs3files' # replace with your bucket name
KEY = ['tree.txt','forest.txt'] # replace with your object key

s3 = boto3.resource('s3')
for obj in KEY:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'obj')
    
        
   
            
         
    
         
 
# #Scan files
# scan_keys = ['tree', 'forest']

# #Upload to s3
# s3.upload_file(filename, bucket_name, des_filename)
