import boto3

client = boto3.client("ec2")

client.start_instances(InstanceIds=["i-08cb51d177fca43a3"])

waiter = client.get_waiter('instance_running')

waiter.wait(
    InstanceIds=["i-08cb51d177fca43a3"])


print("Ec2 instance started")