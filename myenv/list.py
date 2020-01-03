import boto3
s3 = boto3.resource('s3')
print('Buckets : ')
for bucket in s3.buckets.all():
    print(bucket.name)
bucketname = raw_input("ingrese nombre del bucket : ")
my_bucket = s3.Bucket(bucketname)
print("archivos en "+str(bucketname)+": ")
for file in my_bucket.objects.all():
    print(file.key)
