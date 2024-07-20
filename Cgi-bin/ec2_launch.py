#!/usr/bin/python3
import cgi
import cgitb
import boto3

cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

access_key = form.getvalue('accessKey')
secret_key = form.getvalue('secretKey')
region = form.getvalue('region', 'ap-south-1')
instance_type = form.getvalue('instanceType', 't2.micro')
image_id = form.getvalue('imageId', 'ami-05a5bb48beb785bf1')

try:
    ec2 = boto3.resource(
        "ec2",
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    instance = ec2.create_instances(
        InstanceType=instance_type,
        ImageId=image_id,
        MaxCount=1,
        MinCount=1
    )

    instance_id = instance[0].id
    print(f"Instance created successfully. Instance ID: {instance_id}")

except Exception as e:
    print(f"Error: {str(e)}")
