import pika
import redis, json

redis_connection = redis.Redis(host='localhost', port=6379, db=0)

def send_message(room_id, message, timestamp, userid, sender, receiver):
    content = {
        "user_details": userid,
        "message": message,
        "timestamp": timestamp,
        "room_details": room_id,
        "sender": sender,
        "receiver": receiver
    }
    payload = json.dumps(content)
    time = int(timestamp)
    redis_connection.zadd(room_id, {payload: time})

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        body = json.loads(body)
        # Receive the message and flag for any inappropriate content
        message = body['message']
        bad_words = {"stupid", "wack", "dumb"}
        words_list = message.split(" ")
        print(words_list)
        for word in words_list:
            if word in bad_words:
                message = "This message is flagged due to a cuss word"
                break
        send_message(body['room_details'], message, body['timestamp'], body['user_details'], body['sender'], body['receiver'])
        connection.close()



    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()