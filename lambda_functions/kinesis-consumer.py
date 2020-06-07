import base64
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Starting process record')
    for record in event['Records']:
        try:
            # Decode Kinesis record
            sequence_number = record['kinesis']['sequenceNumber']
            record_data = record['kinesis']['data']
            payload = base64.b64decode(record_data)
            json_data = str(payload.decode('utf-8'))
            event_payload = json.loads(json_data)

            logger.info('Process sequence number: {}'.format(sequence_number))

            # Warning: You mustn't log the sensitive content.
            # You can log the payload if the payload doesn't contain the sensitive data. Such as patient information
            logger.info('Event data: {}'.format(json_data))

            # Do something
            logger.info('Process:')
            logger.info(event_payload)

            logger.info('Process successful')
        except Exception as ex:
            logger.error('Process event failed: {}'.format(str(ex)))
            raise ex

    return "Process records successful"
