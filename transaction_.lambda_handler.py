import json

def lambda_handler(event, context):
    # TODO implement

    #1. parse out query string parameters
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']


    print('transactionId='+ transactionId)
    print('transactionType='+ transactionType)
    print('transactionAmount='+ transactionAmount)


    #2. Consrtuct the bosy of response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from lambda land'

    #3. Construct http request object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['content-type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)


    #4 return the response object
    return responseObject




    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
