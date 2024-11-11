from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2Instances
from diagrams.aws.network import Route53, ELB
from diagrams.aws.general import Client
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.storage import EBS, EFS




with Diagram(name="Whattimeisit", show=False, filename="diagrams/sas/whattimeisit"):
    
    with Cluster("Auto Scaling Group"):
        with Cluster("AZ1"):
            ec2_1 = EC2Instances("EC2")
    
        with Cluster("AZ2"):
            ec2_2 = EC2Instances("EC2")
    
    with Cluster("Elastic Load Balancer + Health Check"):
        elb = ELB("ELB")
    
    client = Client("Client")
    
    Route53("Route53") << client >> elb >> [ec2_1, ec2_2]
    
with Diagram(name="MyShoppingCart", show=False, filename="diagrams/sas/myshoppingcard"):
    
    with Cluster("Auto Scaling Group"):
        with Cluster("AZ1"):
            ec2_1 = EC2Instances("EC2")
    
        with Cluster("AZ2"):
            ec2_2 = EC2Instances("EC2")
            
    
    with Cluster("Elastic Load Balancer + Health Check"):
        elb = ELB("ELB")

    with Cluster("Security Group"):
        cache = ElastiCache("Cache")
        rds = RDS("Database")
    
    client = Client("Client")
    
    Route53("Route53") << client >> elb >> [ec2_1, ec2_2] >> cache >> rds
    
with Diagram(name="my wordpress", show=False, filename="diagrams/sas/mywordpress"):
    
    with Cluster("Auto Scaling Group"):
        with Cluster("AZ1"):
            ec2_1 = EC2Instances("EC2") - EBS("EBS")

        with Cluster("AZ2"):
            ec2_2 = EC2Instances("EC2") - EBS("EBS")
    
    with Cluster("Elastic Load Balancer + Health Check"):
        elb = ELB("ELB")

    
    client = Client("Client")
    
    Route53("DNS") << client >> elb >> [ec2_1, ec2_2] >> EFS("EFS")