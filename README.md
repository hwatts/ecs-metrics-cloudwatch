# ECS Metrics Cloudwatch

Simple serverless function to log task stopped events to Cloudwatch metrics from the associated Cloudwatch event.

Deployed using Serverless Application Model - this creates a cloudwatch event rule, a lambda function and a minimal IAM role with permission to put metrics only:

First package the application to an S3 bucket that you own:

```sh
aws cloudformation package \
    --template-file template.yaml \
    --output-template-file ecs-metrics-deploy.yaml \
    --s3-bucket mys3bucketname
```

Then deploy using the output template:

```sh
aws cloudformation deploy \
    --template-file ecs-metrics-deploy.yaml \
    --stack-name ecs-metrics \
    --capabilities CAPABILITY_IAM
```
