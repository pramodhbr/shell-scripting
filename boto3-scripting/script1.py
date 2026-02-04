import boto3

ec2=boto3.resource("ec2")

instance=ec2.Instance("i-08cb51d177fca43a3")

# print((instance.state)["Name"])

# print("####################### Starting EC2 Instance")

# instance.start()
# instance.wait_until_running()

# print("############# EC2 Instance Started")

print("####################### Stoping EC2 Instance")

instance.stop()
instance.wait_until_stopped()

print("############# EC2 Instance Started")