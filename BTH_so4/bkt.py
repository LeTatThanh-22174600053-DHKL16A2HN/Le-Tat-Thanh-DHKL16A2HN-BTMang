import boto3 
from botocore.client import Config 
 
s3 = boto3.client('s3', 
    endpoint_url='http://localhost:9000', 
    aws_access_key_id='thanhle25', 
    aws_secret_access_key='thanh2504', 
    config=Config(signature_version='s3v4'), 
    region_name='us-east-1') 
 
s3.download_file('thanh-le','Data_LêTátThành_053.csv','Data_LêTátThành_053.csv') 
print("Download thành công!")