import boto3
s3 = boto3.client('s3')
S3 = boto3.resource('s3')
print('Buckets : ')
for bucket in S3.buckets.all():
    print(bucket.name)
print("subiendo un archivo...")
bucketName = raw_input("ingrese nombre del bucket : ")
Key = raw_input("ingrese nombre del archivo  : ")
outPutname = raw_input("ingrese nombre del archivo en s3 : ")
s3.upload_file(Key,bucketName,outPutname)
