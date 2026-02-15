import boto3
from datetime import datetime, timezone

client = boto3.client("iam")

paginator = client.get_paginator('list_users')
current_date = datetime.now(timezone.utc)

max_key_age=5


for responce in paginator.paginate():
    for user in responce["Users"]:
        username=user["UserName"]

        access_keys=client.list_access_keys(
    UserName=username,)
        for accesskey in access_keys["AccessKeyMetadata"]:
            access_id = accesskey["AccessKeyId"]
            key_creation_date = accesskey["CreateDate"]
            age = (current_date - key_creation_date).days
            if age > max_key_age:
                print("Print deactivate the key user:", username)
                response = client.update_access_key(
                    UserName=username,
                    AccessKeyId=access_id,
                    Status='Active'
                )