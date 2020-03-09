from datetime import date
import time
import json
import boto3
 
 
tableName= 'publicHoliday' #DynamoDB table name
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    try:
        today = str(date.today())
        today=time.strftime("%d/%m/%Y")
        print(today)
        table = dynamodb.Table(tableName)
        response = table.get_item(Key={'Date' : today})
        #print(response )
       
        if 'Item' in response:
            print("Match")
            holidayToday= 'TRUE'
            return {'holidayToday' : holidayToday}
       
        else:
            holidayToday= 'FALSE'
            return {'holidayToday' : holidayToday}
           
    except Exception as e:
         return {'Lambda Error'}