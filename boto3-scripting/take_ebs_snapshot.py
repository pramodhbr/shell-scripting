import boto3

ec2 = boto3.resource("ec2")

volume_iterator = ec2.volumes.all()

print(volume_iterator)

for vol in volume_iterator:
    vol_id=vol.id
    volume = ec2.Volume(vol_id)
    print("Taking EBS volume snapshot")
    volume.create_snapshot(VolumeId=vol_id)