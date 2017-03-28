import logging, boto3, datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('cloudwatch')

def handler(event, context):

    serviceName=''
    clusterName=''
    dimensions = []
    try:
        if 'service:' in event['detail']['group']:
            serviceName=event['detail']['group'].split(':')[1]
            dimensions.append({'Name': 'ServiceName', 'Value': serviceName})
    except:
        pass
    try:
        clusterName=event['detail']['clusterArn'].rsplit('/', 1)[-1]
        dimensions.append({'Name': 'ClusterName', 'Value': clusterName})
    except:
        pass

    logger.info('parsed dimensions as {}'.format(dimensions))

    if dimensions:
        putMetricResponse = client.put_metric_data(
            Namespace='ECS',
            MetricData=[
                {
                    'MetricName': 'TasksStopped',
                    'Dimensions': dimensions,
                    'Timestamp': datetime.datetime.now(),
                    'Value': 1,
                    'Unit': 'Count'
                },
            ]
        )
    else:
        logger.error('failed to parse any dimensions')

    return {}
