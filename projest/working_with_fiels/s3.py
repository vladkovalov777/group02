import boto3


ACCESS_KEY = 'e13de50095d962888c357d437d0bc855'
SECRET_KEY = '92c703ef97a891d9dc79f3adb3ed484b18eacc6f9b3d5fb0c4bbe6f586d31c2e'
ENDPOINT = "https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com"
REGION_NAME = 'EEUR'

PUBLIC_URL = 'https://pub-f0b804e4a87c49ec9fa377abd59b7d70.r2.dev'
BUCKET_NAME = 'group04092025'

s3client = boto3.client(
    service_name='s3',
    region_name=REGION_NAME,
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

# UPLOAD FILE

target_file_name = 'images/Pumpkin/123456.png'
s3client.upload_file('123456.png', BUCKET_NAME, target_file_name)
# https://pub-f0b804e4a87c49ec9fa377abd59b7d70.r2.dev/images/spring123.jpeg
print(f'{PUBLIC_URL}/{target_file_name}')