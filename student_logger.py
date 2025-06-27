import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Students')

students = [
    {'student_id': '001', 'name': 'Alice Appiah', 'course': 'AWS Cloud Fundamentals'},
    {'student_id': '002', 'name': 'Rita Okloo', 'course': 'Linux Basics'}
]

for student in students:
    response = table.put_item(Item=student)
    print(f"Inserted: {student['name']} | Status: {response['ResponseMetadata']['HTTPStatusCode']}")
