#!/bin/bash

set -x

pip install --user boto3

aws configure sso

# Create List of AWS accounts
# And
# sso profiles
mv ~/.aws/config ~/.aws/config.backup
rm accounts.txt
python3 make-account-profiles.py something

# Enable Automatic Key roation and save the status
rm -fr enable-kms-cmks-key-rotation*.csv

for account in $(< accounts.txt)
do
    profile=sso-$account
    python3 enable-kms-cmks-key-rotation.py $profile
done
