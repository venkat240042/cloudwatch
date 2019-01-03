import boto3
cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'EC2-cloudwatch',
          'Value': 'i-05b963ae6b6edd462'
        },
    ],
    Unit='Seconds'
)

# Delete alarm
cloudwatch.delete_alarms(
  AlarmNames=['Web_Server_CPU_Utilization'],
)
