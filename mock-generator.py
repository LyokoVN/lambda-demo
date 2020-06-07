import base64
import json
import uuid


KINESIS_STREAM_NAME = 'dev-user-stream-v1'
SQS_QUEUE_URL = 'http://localhost:9324/queue/dev-user-queue-v1'


def generate_kinesis(raw_events, file_name, stream_name):
    kinesis_events = []
    for raw_event in raw_events:
        json_data = json.dumps(raw_event)
        encodedBytes = base64.b64encode(json_data.encode('utf-8'))
        encodedStr = str(encodedBytes, 'utf-8')

        kinesis_events.append({
            'Data': encodedStr,
            'PartitionKey': str(uuid.uuid4())
        })

    with open(f'mocking/kinesis/{file_name}.json', 'w') as data_file:
        kinesis_input = {
            "Records": kinesis_events,
            "StreamName": stream_name
        }

        json_text = json.dumps(kinesis_input, indent=4, sort_keys=True)
        data_file.write(json_text)


def generate_sqs(raw_messages, file_name, queue_url):
    sqs_messages = []
    for raw_event in raw_messages:
        json_data = json.dumps(raw_event)
        encodedBytes = base64.b64encode(json_data.encode('utf-8'))
        encodedStr = str(encodedBytes, 'utf-8')

        sqs_messages.append({
            'MessageBody': encodedStr,
            'Id': str(uuid.uuid4())
        })

    with open(f'mocking/sqs/{file_name}.json', 'w') as data_file:
        sqs_input = {
            "Entries": sqs_messages,
            "QueueUrl": queue_url
        }

        json_text = json.dumps(sqs_input, indent=4, sort_keys=True)
        data_file.write(json_text)

if __name__ == '__main__':
    raw_events = [
        {
            'id': 1,
            'name': 'Kary Lyoko',
            'gender': 'MALE',
            'available': True,
            'target': 'PRETTY_GIRL'
        },
        {
            'id': 2,
            'name': 'Emiri Suzuhara',
            'gender': 'FEMALE',
            'available': False,
            'target': 'COOL_BOY'
        }
    ]

    generate_kinesis(raw_events, 'user_created', KINESIS_STREAM_NAME)
    generate_sqs(raw_events, 'user_created', SQS_QUEUE_URL)




