#!/usr/bin/env python

import argparse
import boto3
import sys
from os.path import expanduser

account_list = open('accounts.txt', 'w')
sso_config = open(expanduser("~") + '/.aws/config', "a")
org = boto3.client('organizations')

paginator = org.get_paginator('list_accounts')
for page in paginator.paginate():
    for account in page['Accounts']:
        account_number = account['Id']
        account_list.write(account_number + '\n')
        sso_config.write(f"[profile 'sso-{account_number}']\n")
        sso_config.write(f"sso_start_url = https://{sys.argv[1]}.awsapps.com/start\n")
        sso_config.write(f"sso_region = us-east-1\n")
        sso_config.write(f"sso_account_id = {account_number}\n")
        sso_config.write(f"sso_role_name = AdministratorAccess\n")
        sso_config.write(f"region = ap-southeast-2\n")
        sso_config.write(f"\n")

account_list.close()
sso_config.close()
