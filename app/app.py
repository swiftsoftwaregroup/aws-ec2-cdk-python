#!/usr/bin/env python3
import os

import aws_cdk as cdk

from app.app_stack import AppStack


app = cdk.App()

AppStack(
    app, 
    construct_id="NginxEc2Stack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
