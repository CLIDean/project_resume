#creates table from scratch
import boto3
import json

api_url = boto3.client('cloudformation').describe_stacks(StackName='ashback')['Stacks'][0]['Outputs'][0]['OutputValue']

global_table_name = api_url


def lambda_handler(event, context):

    try:
        print(api_url)
        #increment table string number
        tab_var = global_table_name

        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table(tab_var)

        response = table.get_item(TableName=tab_var, Key={'count': 2})
        print(response)
    
        added_count = (response['Item']['attribute1'])

        print(type(added_count))
        
        added_count = int(added_count) +1
        
        print(added_count)
        added_count = str(added_count)
        
        update_expression = 'SET attribute1 = :added_count'
        expression_values = {':added_count': added_count}
        response2 = table.update_item(TableName=tab_var, Key={'count': 2}, UpdateExpression= update_expression, ExpressionAttributeValues = expression_values)
        
        
        # return added_count
        return {
            "statusCode": 200,
            'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
            "body": json.dumps({
                "visitCount": added_count,
            }),
        }




    except:
        try:
                #create new attribute and item in existing table
            table_name = global_table_name
    
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(table_name)
    
            table.put_item(
                Item={
                    'count': 2,
                    'attribute1': 2
                }
            )
            return {
            "statusCode": 200,
            'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
            "body": json.dumps({
                "visitCount": '1',
            }),
        }

        except:
            # Create a boto3 client for DynamoDB
            dynamodb = boto3.client('dynamodb')
            table_name_variable = global_table_name
            
            # Define the table's schema
            table_schema = {
                'AttributeDefinitions': [
                    {
                        'AttributeName': 'count',
                        'AttributeType': 'N'
                    },
                ],
                'KeySchema': [
                    {
                        'AttributeName': 'count',
                        'KeyType': 'HASH'
                    },
                ],
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                },
                'TableName': table_name_variable
            }
            
            # Create the table
            response = dynamodb.create_table(**table_schema)
            
            # table_name = global_table_name
    
            # dynamodb = boto3.resource('dynamodb')
            # table = dynamodb.Table(table_name)
            
    
            # table.put_item(
            #     Item={
            #         'count': 2,
            #         'attribute1': 0
            #     }
            # )
            
            print(response)
        
            return {
            "statusCode": 200,
            'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
            "body": json.dumps({
                "visitCount": '2',
            }),
        }





































# '''import boto3
# import json

# dynamodb = boto3.resource('dynamodb')

# table = dynamodb.Table('site_visits')

# cloudformation = boto3.client('cloudformation')

# def lambda_handler(event, context):

#     stack_name = 'ashback'
#     output_name = 'MyTableName'
    
#     result = cloudformation.describe_stacks(StackName=stack_name)
#     stack = result['Stacks'][0]
#     output = next(output for output in stack['Outputs'] if output['OutputKey'] == output_name)
#     topic_arn = output['OutputValue']

#     dynamic_table_name = output_name


#     response = table.get_item(TableName=dynamic_table_name, Key={'count': 0})
#     # print(response['Item'])
#     # print(response['Item']['attribute1'])
#     added_count = (response['Item']['attribute1'])
    
     
#     added_count = int(added_count['N']) +1
#     # added_count = added_count +1
    
    
#     update_expression = 'SET attribute1 = :added_count'
#     expression_values = {':added_count': {'N': added_count}}
#     response2 = table.update_item(TableName=dynamic_table_name, Key={'count': 0}, UpdateExpression= update_expression, ExpressionAttributeValues = expression_values)
   
#     print(added_count)
    
    
#     # return added_count
#     return {
#         # "statusCode": 200,
#         "body": json.dumps({
#             "visitCount": added_count,
#             "outputvalue": topic_arn,
#             # "message": "hello world",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }
    









# '''
# import boto3
# import json

# dynamodb = boto3.resource('dynamodb')

# table = dynamodb.Table('site_visits')

# def lambda_handler(event, context):
#     response = table.get_item(TableName='site_visits', Key={'count': 0})
#     # print(response['Item'])
#     # print(response['Item']['attribute1'])
#     added_count = (response['Item']['attribute1'])
    
     
#     added_count = int(added_count['N']) +1
#     # added_count = added_count +1
    
    
#     update_expression = 'SET attribute1 = :added_count'
#     expression_values = {':added_count': {'N': added_count}}
#     response2 = table.update_item(TableName='site_visits', Key={'count': 0}, UpdateExpression= update_expression, ExpressionAttributeValues = expression_values)
   
#     print(added_count)
    
    
#     # return added_count
#     return {
#         # "statusCode": 200,
#         "body": json.dumps({
#             "visitCount": added_count,
#             # "message": "hello world",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }
   













































#import boto3
#import json
#
#dynamodb = boto3.resource('dynamodb')
#
#table = dynamodb.Table('site_visits')
#
#cloudformation = boto3.client('cloudformation')
#
#def lambda_handler(event, context):
#
#    stack_name = 'ashback'
#    output_name = 'MyTableName'
#    
#    result = cloudformation.describe_stacks(StackName=stack_name)
#    stack = result['Stacks'][0]
#    output = next(output for output in stack['Outputs'] if output['OutputKey'] == output_name)
#    topic_arn = output['OutputValue']
#
#    dynamic_table_name = output_name
#
#
#    response = table.get_item(TableName=dynamic_table_name, Key={'count': 0})
#    # print(response['Item'])
#    # print(response['Item']['attribute1'])
#    added_count = (response['Item']['attribute1'])
#    
#     
#    added_count = int(added_count['N']) +1
#    # added_count = added_count +1
#    
#    
#    update_expression = 'SET attribute1 = :added_count'
#    expression_values = {':added_count': {'N': added_count}}
#    response2 = table.update_item(TableName=dynamic_table_name, Key={'count': 0}, UpdateExpression= update_expression, ExpressionAttributeValues = expression_values)
#   
#    print(added_count)
#    
#    
#    # return added_count
#    return {
#        # "statusCode": 200,
#        "body": json.dumps({
#            "visitCount": added_count,
#            "outputvalue": topic_arn,
#            # "message": "hello world",
#            # "location": ip.text.replace("\n", "")
#        }),
#    }
#    
#
#
#
#
#
#
#
#
#
#'''
#import boto3
#import json
#
#dynamodb = boto3.resource('dynamodb')
#
#table = dynamodb.Table('site_visits')
#
#def lambda_handler(event, context):
#    response = table.get_item(TableName='site_visits', Key={'count': 0})
#    # print(response['Item'])
#    # print(response['Item']['attribute1'])
#    added_count = (response['Item']['attribute1'])
#    
#     
#    added_count = int(added_count['N']) +1
#    # added_count = added_count +1
#    
#    
#    update_expression = 'SET attribute1 = :added_count'
#    expression_values = {':added_count': {'N': added_count}}
#    response2 = table.update_item(TableName='site_visits', Key={'count': 0}, UpdateExpression= update_expression, ExpressionAttributeValues = expression_values)
#   
#    print(added_count)
#    
#    
#    # return added_count
#    return {
#        # "statusCode": 200,
#        "body": json.dumps({
#            "visitCount": added_count,
#            # "message": "hello world",
#            # "location": ip.text.replace("\n", "")
#        }),
#    }
#   '''
