#!/bin/sh
aws sqs create-queue --queue-name dev-user-queue-v1 --endpoint-url ${AWS_SQS_ENDPOINT_URL};
aws kinesis create-stream --stream-name dev-user-stream-v1 --shard-count 1 --endpoint-url ${AWS_KINESIS_ENDPOINT_URL};