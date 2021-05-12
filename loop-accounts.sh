#!/bin/bash

for account in $(< accounts.txt)
do
    profile=sso-$account
    python3 enable-kms-cmks-key-rotation.py $profile >> enable-kms-cmks-key-rotation-status.csv
done
