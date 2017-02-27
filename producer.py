import nsq

def handler(message):
    print message
    print type(message)
    return True

r = nsq.Reader(message_handler=handler,
        lookupd_http_addresses=['http://172.17.0.1:4161'],
        topic='test', channel='asdf', lookupd_poll_interval=15)
nsq.run()

