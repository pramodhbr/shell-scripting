import boto3

ec2 = boto3.resource("ec2")

regions = []
for region in ec2.meta.client.describe_regions()['Regions']:
    regions.append(region["RegionName"])

for region in regions:
    ec2 = boto3.resource("ec2",region_name=region)
    print("Ec2 Region: ",region)
    ec2_filter={'Name': 'instance-state-name', 'Values' : ['running']}
    instances = ec2.instances.filter(Filters=[ec2_filter])

    for instance in instances:
        instance.stop()
        print("The following instances are in stopped state")


# ec2_filter={'Name': 'instance-type', 'Values' : ['t3.micro']}

# ec2_tag={'Name': 'tag:Name', 'Valuese': ['test-1']}
# instance_iterator = ec2.instances.filter(
#     Filters=[ec2_tag,ec2_filter]
# )


# for instance in instance_iterator:
#     instance.stop()