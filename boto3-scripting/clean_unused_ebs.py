import boto3

ec2 = boto3.resource("ec2")

volume_iterator = ec2.volumes.filter(
        Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        },
    ],
)

for vol in volume_iterator:
    vol_id=vol.id
    volume=ec2.Volume(vol_id)
    print("Delete volume",vol_id)
    volume.delete()