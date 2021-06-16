#import response_queue
import sys
import main
import time

client = main.get_sqs_resource()
queue = client.get_queue_by_name(QueueName='response_queue_official')

#infinite loop to continuously poll the response queue
while True:
    for msg in queue.receive_messages(MaxNumberOfMessages=10):
        # save body (the pair) and message attribute (the name)
        response_string = msg.body
        response_name = str(msg.body).split(", ")
        # print so it goes to stdout, which will route it to the response_queue_poller.stdout.on call
        # in test_app.js
        print(str(response_name[0]) + ": (" + str(response_name[0][:-5]) + ", " + str(response_name[1]) + ")")
        sys.stdout.flush()

        # remove message from response queue after processing it
        msg.delete()
        time.sleep(1)
