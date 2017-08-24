### Trusted Advisor - List of All Checks

This handy one liner will print the list of all TA checks along with short name and category for quick reference

```bash
aws support describe-trusted-advisor-checks  --language "en" --query 'checks[*].{CAT:category,ID:id, Name:name}' --output text 
```

You get a nice formated list that looks this

----
```python
cost_optimizing	Qch7DwouX1	Low Utilization Amazon EC2 Instances
cost_optimizing	hjLMh88uM8	Idle Load Balancers
cost_optimizing	DAvU99Dc4C	Underutilized Amazon EBS Volumes
cost_optimizing	Z4AUBRNSmz	Unassociated Elastic IP Addresses
security	HCP4007jGY	Security Groups - Specific Ports Unrestricted
security	1iG5NDGVre	Security Groups - Unrestricted Access
security	zXCkfM1nI3	IAM Use
security	Pfx0RwqBli	Amazon S3 Bucket Permissions
security	7DAFEmoDos	MFA on Root Account
security	Yw2K9puPzl	IAM Password Policy
security	nNauJisYIT	Amazon RDS Security Group Access Risk
fault_tolerance	H7IgTzjTYb	Amazon EBS Snapshots
fault_tolerance	wuy7G1zxql	Amazon EC2 Availability Zone Balance
fault_tolerance	iqdCTZKCUp	Load Balancer Optimization 
fault_tolerance	S45wrEXrLz	VPN Tunnel Redundancy
performance	ZRxQlPsb6c	High Utilization Amazon EC2 Instances
```

Here is another one, this one actually narrows the output down to checks that belong to 'Security' category and prints only the check ID and Name

```bash
aws --region us-east-1 support describe-trusted-advisor-checks --language en --query "checks[?category=='security'].{CAT:category,NAME:name}" --output text
```

Here is what the output looks like:
----
```python
security	Security Groups - Specific Ports Unrestricted
security	Security Groups - Unrestricted Access
security	IAM Use
security	Amazon S3 Bucket Permissions
security	MFA on Root Account
security	IAM Password Policy
security	Amazon RDS Security Group Access Risk
security	Amazon Route 53 MX Resource Record Sets and Sender Policy Framework
security	AWS CloudTrail Logging
security	ELB Listener Security
security	ELB Security Groups
security	CloudFront Custom SSL Certificates in the IAM Certificate Store
security	CloudFront SSL Certificate on the Origin Server
security	IAM Access Key Rotation
security	Exposed Access Keys
security	Amazon EBS Public Snapshots
security	Amazon RDS Public Snapshots
```
