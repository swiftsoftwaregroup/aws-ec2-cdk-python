# ec2-aws-cdk-python

Deploy EC2 instance using the AWS CDK for Python

## Development

Configure project:

```bash
source configure.sh
```

Open in Visual Studio Code:

```bash
code .
```

### Deploy

Print the CloudFormation template for the stack. You should see the CloudFormation template without any errors:

```bash
cdk synth --profile default
```
Bootstrap the CDK environment. This should be done only once per account. Skip this step if you have done it already. See [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) for details:

```bash
cdk bootstrap --profile default
```
Deploy the stack:

```bash
cdk deploy --profile default
```

### Test Deployment

Check that you can browse the `nginx` default site:

```bash
key="aws-ec2-key"
instance="NginxEc2Stack/NginxInstance"

instance_public_ip=$(aws ec2 describe-instances \
    --filters \
       Name=tag:Name,Values=$instance \
        Name=instance-state-name,Values=running \
| jq -r '.Reservations[0].Instances[0].PublicIpAddress')

open http://$instance_public_ip
```

### Cleanup

```bash
cdk destroy --profile default
```

**Opptional**: To delete the `CDKToolkit` CloudFormation template which is created by the AWS CDK during bootstrap:

```bash
aws cloudformation delete-stack --stack-name CDKToolkit --profile default
```

The bootstrap process creates an S3 Bucket with a name:  `cdk-<hash>-assets-<account_id>-<region>`. This bucket will not be deleted automatically and will remain in your account if not deleted manually. 

## How to create a new project

```bash
# Node.js
nvm use 20.16.0

# Python
mkdir app
cd app
cdk init app --language python

# Install Python packages
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```