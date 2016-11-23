
#### Finding all EC2 instances with CW Alarms ####
Interesting question came up today. How do find all the instances in a given account that have (or do not have) a *CloudWatch* alarm associated with them. Since in a given account, you could have thousands of instances it may not be practical or desirable to get this information from the **Console**

While unfortuately there is no, (at least not yet) a single command to create such a list, a little bash script 
