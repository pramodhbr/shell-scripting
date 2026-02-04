import boto3

# iam = boto3.resource("iam")


# print(iam.users.all())

# count=1
# for user in iam.users.all():
#     print(count,user.name)
#     count+=1


iam = boto3.client("iam")

response = iam.list_users()

# print(response["Users"][0]["UserName"])

for user in response["Users"]:
    print(user["UserName"])