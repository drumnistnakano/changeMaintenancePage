import subprocess
import os
import boto3
 
def lambda_handler(event, context):
    initial_arn = event['initial_arn']
    secound_arn = event['secound_arn']
    client = boto3.client('elbv2')
    try:
        client.set_rule_priorities(
        RulePriorities=[
                {
                    'RuleArn': initial_arn,
                    'Priority': 1
                },
                {
                    'RuleArn': secount_arn,
                    'Priority': 2
                },
            ] 
        )
    except Exception as error:
        call_sns(str(error))
        return 2

def call_sns(msg):
    """
    Nortify via E-mail if Exception arised.
    """
    topic_arn = os.environ["TOPIC_ARN"]
    subject = os.environ["SUBJECT"]
    client = boto3.client("sns")
    request = {
        'TopicArn': topic_arn,
        'Message': msg,
        'Subject': subject
        }

    client.publish(**request)
