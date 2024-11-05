# Security Group Command Line

## Create 
```bash
export AWS_SG=$(aws ec2 create-security-group \
    --group-name MySecurityGroup \
    --description "My security group" \
    --vpc-id vpc-0b4c4660c021f2189 \
    --query 'GroupId' \
    --output text)
```

## Describe
```bash
aws ec2 describe-security-groups --group-ids $AWS_SG
```

## Delete
```bash
aws ec2 delete-security-group --group-id $AWS_SG
```