from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Use the default VPC
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # Create a security group
        security_group = ec2.SecurityGroup(
            self, "NginxSecurityGroup",
            vpc=vpc,
            description="Allow HTTP traffic",
            allow_all_outbound=True
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP traffic from anywhere"
        )

        # Create a role for the EC2 instance
        role = iam.Role(
            self, "NginxInstanceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        # Create the EC2 instance
        instance = ec2.Instance(
            self, "NginxInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            role=role,
            security_group=security_group,
        )

        # Add user data to install and start nginx
        instance.add_user_data(
            "yum update -y",
            "amazon-linux-extras install nginx1 -y",
            "systemctl start nginx",
            "systemctl enable nginx"
        )

        # Output the public IP of the instance
        self.output_props = {
            'instance_public_ip': instance.instance_public_ip
        }
        