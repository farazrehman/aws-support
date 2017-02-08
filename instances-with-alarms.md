
#### Finding all EC2 instances with CW Alarms ####
Interesting question came up today. How do I find all the instances in a given account that have (or do not have) a **CloudWatch** alarm associated with them? Since in a given account, you could potentially have thousands of instances, it may not be practical or desirable to get this information from the Console

While unfortuately there is no, (at least not yet) a single command to create such a list, a set of commands can be used, glued together in a Bash script, to do the trick

##### 1. Create a list of all instance-ids #####
```
aws ec2 describe-instances --filter "Name=tag:Name, Values=blue-*" --query 'Reservations[*].Instances[*].{ID:InstanceId}' --output text > all_instances.txt
```

##### 2. Use the following Bash script to get instances that have associated CW Alarms #####
```
for alarm in `aws cloudwatch describe-alarms --query 'MetricAlarms[*].{NAME:AlarmName}' --output text`; do aws cloudwatch describe-alarms --alarm-names $alarm --query 'MetricAlarms[*].Dimensions[*].{Instance:Value}' --output text; done > instances_with_alarms.txt
```

The first commands writes out a list of **All** EC-2 instances (instance-ids only) in file ```all_instances.txt``` while the second command writes out the ids of instances that have CloudWatch alarms associated with them. You may have to do some additional cleanup to get the data in the right form. If you are trying to get the list of instances that **DO NOT** have alarms, you can simply compare the two text files using ```diff``` or some other tool



