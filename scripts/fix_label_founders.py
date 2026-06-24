import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')
labels_table = dynamodb.Table('detroit-techno-labels')

fixes = [
    ('label_430_west',    ['Lenny Burden', 'Lawrence Burden']),
    ('label_direct_beat', ['Tommy Hamilton', 'Keith Tucker', 'DJ Stingray']),
]

for label_id, founder_list in fixes:
    labels_table.update_item(
        Key={'label_id': label_id},
        UpdateExpression='SET founder = :f',
        ExpressionAttributeValues={':f': founder_list}
    )
    print(f"Fixed founder field: {label_id}")

print("\n✓ Done.")