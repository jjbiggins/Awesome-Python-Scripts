import boto3
import json
import sys
from multiprocessing import Pool

file = '/path/to/file_with_records_as_jsonl'
queue_url = 'your-queue-url'
region = 'your-region'
processor_count = int(sys.argv[1])


def send_message(data):
    sqs_client = boto3.client('sqs', region_name=region)
    sqs_client.send_message_batch(
        QueueUrl=queue_url,
        Entries=[{'MessageBody': json.dumps(x)} for x in data]
    )


def main(file):
    with open(file) as f:
        data = [json.loads(line) for line in f]
        batched_data = []
    batched_data.extend(
        data[i : i + int(len(data) / processor_count)]
        for i in range(0, len(data), int(len(data) / processor_count))
    )

    temp = list(
        Pool(processes=processor_count).imap_unordered(
            send_message, batched_data
        )
    )

    total_records_sent = sum(temp)


if __name__ == "__main__":
    main(file)
