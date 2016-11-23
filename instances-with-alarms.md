
#### Finding all EC2 instances with CW Alarms ####
Interesting question came up today. How do I find all the instances in a given account that have (or do not have) a *CloudWatch* alarm associated with them? Since in a given account, you could potentially have thousands of instances, it may not be practical or desirable to get this information from the Console

While unfortuately there is no, (at least not yet) a single command to create such a list, a set of commands can be used glued together in a Bash script can do the trick

##### 1. Create a list of all instance-ids #####
```
aws ec2 describe-instances --filter "Name=tag:Name, Values=blue-*" --query 'Reservations[*].Instances[*].{ID:InstanceId}' --output text > instances.txt
```



