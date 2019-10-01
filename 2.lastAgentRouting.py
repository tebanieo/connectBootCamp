import json
import boto3
tableName= 'LastAgent'
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    
    phoneNumber = event['Details']['ContactData']['CustomerEndpoint']['Address']
    #phoneNumber = '+61415233688'

    table = dynamodb.Table(tableName)
    response = table.get_item(Key={'phoneNumber' : phoneNumber})
        
    if 'Item' in response:
        print("Match")
        phoneNumber = response['Item']['phoneNumber']
        LastAgent = response['Item']['Agent']

        return {'LastAgent' : LastAgent}
            
    else:
        return { 'Message': 'NoMatch'}
    