import sys
import json
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

data = {'Name' : ['Person-A','Person-B','Person-C'],
        'Country':['Australia','India','USA'],
        'Age': ['24','34','44']}

df = pd.DataFrame(data) 

print(df);

loginInfo = json.load(open('/Users/suryakantjethwa/Developer/Python/Python Research/myDemo/login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

sf = Salesforce(username = username, password = password, security_token = security_token, domain = domain)
session_id, instance = SalesforceLogin(username = username, password = password, security_token = security_token,domain = domain)
sf = Salesforce(instance = instance, session_id = session_id)
print(sf);


for element in dir(sf):
  if not element.startswith('_'):
    if isinstance(getattr(sf, element), str):
      print('Property Name: {0} ;Value: {1}'.format(element, getattr(sf, element)))


metadata_org = sf.describe()
print(metadata_org);

print (metadata_org['encoding'])
print (metadata_org['maxBatchSize'])
print(metadata_org['sobjects'])
df_sobjects = pd.DataFrame(metadata_org['sobjects'])
df_sobjects.to_csv('org metadata info.csv', index = False)
