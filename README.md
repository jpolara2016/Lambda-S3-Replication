# Lambda-S3-Replication

These two different lambda functions will allow you to **copy objects** to another bucket when there is a put event, and **delete objects** when there is a delete event in the source bucket.

There are 2 functions for copying and deleting objects so use it accordingly however it meets your needs.  

### Requirements
1. IAM Role
  Policy:
  ```json
{
    "Version": "2012-10-17",
    "Id": "Policy1591045332632",
    "Statement": [
        {
            "Sid": "Stmt1618270933950",
            "Action": "s3:*",
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::jpolara1-*/*"
        },
        {
            "Sid": "Stmt1617806794444",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
  ```
2. AWS Lambda fucntion copy_objects (Python3.8)
3. AWS Lambda fucntion delete_objects (Python3.8)
4. Configure Trigger for the funciton you created
