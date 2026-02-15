import boto3

ec2 = boto3.resource("ec2")

snapshot_iterator = ec2.snapshots.filter(OwnerIds=['self'])


for snap in snapshot_iterator:
    print(dir(snap))
    snap_id=snap.snapshot_id
    snap=ec2.Snapshot(snap_id)
    try:
       print("Deleting snapshot",snap_id)
       snap.delete()
    except:
        print("Cannot delete the snapshot since it is already used by existing AMI or EC2 instance")