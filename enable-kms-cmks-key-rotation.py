#!/usr/bin/env python

import argparse
import boto3
import sys

profile = sys.argv[1]
boto3.setup_default_session(profile_name=profile)
account_number = boto3.client("sts").get_caller_identity()["Account"]
for region in ["ap-southeast-2", "us-east-1"]:
    try:
        kms = boto3.client('kms', region_name=region)
        for key in kms.list_keys()['Keys']:
            KeyId = key['KeyId']
            try:
                status = kms.enable_key_rotation(KeyId=KeyId)
                print(f"{account_number},{KeyId},Enabled")
            except Exception as e:
                # print(e)
                pass
    except:
        pass
