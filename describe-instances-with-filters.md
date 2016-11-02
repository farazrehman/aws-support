The 'describe-instances' is a very power CLI/API call that returns a detailed dataset about every single EC2 instance in your account. However, chances are that you have more than just a handful of instances in your account so when you run this call in its default form like this

```
aws ec2 describe-instances --output table
```

The amount of data get returned back will make it difficult to consume. Luckily, AWS CLI has built-in --filter and --query switches that can help you keep your result set nice, clean and manageable. Following example shows how to filter out your instances by a specific "tag" using wildcards, and display only the fields that you really care about

```
aws ec2 describe-instances --filter "Name=tag:Name, Values=blue-*" --query 'Reservations[*].Instances[*].{ID:InstanceId, Name:PrivateDnsName}' --output text --output table
```

The above command will filter out all the EC2 instances that have a tag, "Name" set to the value "blue-*", (notice the use of wildcard in the value. Here is the result of running the above command

```
------------------------------------------------
|               DescribeInstances              |
+-------------+--------------------------------+
|     ID      |             Name               |
+-------------+--------------------------------+
|  i-62xcbxxx |  ip-172-16-1-xxx.ec2.internal  |
|  i-63xcbxxx |  ip-172-16-1-xxx.ec2.internal  |
|  i-6fxcbxxx |  ip-172-16-1-xxx.ec2.internal  |
|  i-6excbxxx |  ip-172-16-1-xxx.ec2.internal  |
+-------------+--------------------------------+

```
