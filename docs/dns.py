from diagrams import Diagram, Cluster
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.digitalocean.network import Domain

from diagrams.aws.general import Client
from diagrams.aws.network import Route53HostedZone, ElbApplicationLoadBalancer
from diagrams.aws.compute import EC2Instances
from diagrams.aws.database import RDS


with Diagram("DNS", show=False, filename="diagrams/dns", direction="LR"):
    client = Mobile("Client")
    local = Rack("Local DNS Resolver")
    Domain('Internet') << client >> local >> [Storage("Root DNS (managed by ICANN)"), 
                                                 Storage("TLD DNS (managed by IANA)"), 
                                                 Storage("SLD DNS (managed by Domain Registrar)")] >> local >> client

with Diagram("Hosted Public Zone", show=False, filename="diagrams/hosted_public_zone", direction="LR"):
    client = Client("Client")
    hostedZone = Route53HostedZone("Hosted Zone")
    
    with Cluster("VPC"):
        ec2 = EC2Instances("EC2")
        alb = ElbApplicationLoadBalancer("ALB")
    
    client >> hostedZone >> client
    hostedZone >> [ec2, alb] >> hostedZone
    

with Diagram("Hosted Private Zone", show=False, filename="diagrams/hosted_private_zone", direction="LR"):
    
    with Cluster("VPC"):
        hostedZone = Route53HostedZone("Hosted Zone")
        ec2 = EC2Instances("EC2")
        db = RDS('RDS')
    
    ec2 >> hostedZone >> ec2 >> db 
    
    