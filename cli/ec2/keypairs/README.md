# KeyPairs Command Line

# Create 
```bash
aws ec2 create-key-pair \
--key-name MyKeyPair \
--query 'Material' \
--output text > cli/ec2/keypairs/keys/MyKeyPair.pem
```

# Describe
```bash
aws ec2 describe-key-pairs --key-name MyKeyPair
```

# Delete 
```bash
aws ec2 delete-key-pair --key-name MyKeyPair
```