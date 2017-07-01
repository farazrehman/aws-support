# aws-support
This reposistory is a collection of handy scripts (mostly Python) and CLI commands to interface with AWS Support backend. Here is what you need to get started

- AWS CLI installed on local machine *EC2 instances running Amazon linux already have them pre-installed*
- If running EC2, you can launch instance with the role that allowes access to EC2 support backend. For this you can create a  role with policy **SupportUser** - If that is not possible, you can also store your EC2 access keys on the local machine, but this **a security risk and NOT recommended for production environments**

**Please make sure that you have the credentials (either stored locally) or via instance role to permit execution of CLI/scripts on your machine**


> Finally here comes the usual rant...I come up with these commands/scripts while helping customers in the field with their day to day problems and post them here with a hope that someone else might find them useful. Having said that, I make no guarantee that these will work in every situation or I will be able to keep them upto date for the future. In other words, please feel free to use them but only at your own risk!! 


__Please see__:

[Configuring the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)



