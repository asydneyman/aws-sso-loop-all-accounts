#!/usr/bin/env python

import boto3
import sys

profile = sys.argv[1]
boto3.setup_default_session(profile_name=profile)
account_number = boto3.client("sts").get_caller_identity()["Account"]
success_status = open('enable-kms-cmks-key-rotation-success.csv', "a")
failed_status = open('enable-kms-cmks-key-rotation-failed.csv', "a")
for region in ["ap-southeast-2", "us-east-1"]:
    try:
        kms = boto3.client('kms', region_name=region)
        for key in kms.list_keys()['Keys']:
            KeyId = key['KeyId']
            try:
                status = kms.enable_key_rotation(KeyId=KeyId)
                success_status.write(f"{account_number},{KeyId},Enabled,{region}\n")
            except Exception as e:
                failed_status.write(f"{account_number},{KeyId},Failed,{region}\n")
                pass

    except:
        failed_status.write(f"{account_number},,Failed,{region}\n")
