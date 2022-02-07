import queue
import boto3
import json
import env

def SNS():
    topicArn = 'arn:aws:sns:us-east-1:-----------:practo'       #------ credentials(can't disclose as anyone can use acc.)
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=env.AWSAccessKeyId,
        aws_secret_access_key=env.AWSSecretKey,article
        region_name='us-east-1'
    )

    publisharticle = {'articelId':8976 , 'amount': 2000}

    response = snsClient.publish(TopicArn=topicArn,
                                Message=json.dumps(publisharticle),
                                Subject='Article',
                                MessageAttributes = { "ArticleType" :{"DataType":"String","StringValue":"PURCHASE"}}
    )

    print(response['ResponseMetadata']['HTTPStatusCode'])


def SQS():
    sqsResource = boto3.client(
        'sqs',
        aws_access_key_id=env.AWSAccessKeyId,
        aws_secret_access_key=env.AWSSecretKey,
        region_name='us-east-1'
    )

    queueUrl = "https://queue.amazonaws.com/------------/pacto"     #------ credentials(can't disclose as anyone can use acc.)
    response = sqsResource.receive_message(
        QueueUrl=queueUrl,
        AttributeNames=[
        'SentTimestamp'
        ],
        MaxNumberOfMessages=1,      #can be incresed till 10,default=1
        MessageAttributeNames=[
        'All'       #return all values
        ],
        VisibilityTimeout=0,    #duration for which the call waits for a message to arrive in the queue before returning.
        WaitTimeSeconds=0
    )

    print(response)




if __name__ == "__main__":
    print("------Welcome to AWS SNS ans SQS-------")
    SNS()
    SQS()