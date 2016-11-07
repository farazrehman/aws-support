
import boto3
import json
import pprint


print " **** AWS Support API Demo ****"
print 
print 

client = boto3.client('support')

# --- Print a list of Severity Levels ---
codes = client.describe_severity_levels(
    language='en'
)
levels = codes['severityLevels']
#Sprint type(levels)

print (" ---- AWS Support Severity Levels ---- ")
print (" ************************************* ")

for i in range(len(levels)):
    c = levels[i]
    print ("  ["+str(i)+"] "+c['name'])
# -------------

print
print

# --- Get the list of services ---
services = client.describe_services()
mServices = services['services']
#print type(mServices)
print (" ---- AWS Support Service Names ---- ")
print (" *********************************** ")
for i in range(len(mServices)):
	q = mServices[i]
	print ("  ("+str(i)+") "+q['code']+" ["+q['name']+"]")
	
#pp = pprint.PrettyPrinter()
#pp.pprint(services)



# response = client.create_case(
#     subject='Test case - Please Ignore',
#     serviceCode='other',
#     severityCode='low',
#     categoryCode='',
#     communicationBody='string',
#     ccEmailAddresses=[
#         'string',
#     ],
#     language='string',
#     issueType='string',
#     attachmentSetId='string'
# )




#response = client.describe_trusted_advisor_checks (language='en')
# json.dumps(response)

