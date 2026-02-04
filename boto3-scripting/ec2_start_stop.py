import boto3

ec2 = boto3.resource("ec2")



# ec2_filter={'Name': 'instance-type', 'Values' : ['t3.micro']}

# ec2_tag={'Name': 'tag:Name', 'Values': ['test-1']}
# instance_iterator = ec2.instances.filter(
#     Filters=[ec2_tag,ec2_filter]
# )


# for instance in instance_iterator:
#     instance.stop()