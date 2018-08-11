from muse import Muse
from time import sleep
from optparse import OptionParser
import os
import json
import tornado.ioloop
import tornado.web
import tornado.websocket
import threading
import logging

PUBLISH_INTERVAL = 100
SUBSCRIBERS = set()
MESSAGE_BUFFER = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class DataHandler(tornado.websocket.WebSocketHandler):
    listeners = set()

    def open(self):
        SUBSCRIBERS.add(self)

    def on_close(self):
        SUBSCRIBERS.remove(self)

def start_eeg_thread(options):
    def handle_packet(data, timestamps):
        for i in range(12):
            j = json.dumps(dict(data=data[:, i].tolist(), timestamp=timestamps[i]))
            MESSAGE_BUFFER.append(j)

    def thread_runner():
        muse = Muse(address=options.address, callback=handle_packet,
                    backend=options.backend, interface=options.interface,
                    name=options.name)

        muse.connect()
        print('Connected')
        muse.start()
        print('Streaming')

        while True:
            try:
                sleep(1)
            except:
                break

        muse.stop()
        muse.disconnect()
        print('Disonnected')

    t = threading.Thread(target=thread_runner)
    t.daemon = True
    t.start()

def start_app():
    def periodic():
        global MESSAGE_BUFFER

        if not MESSAGE_BUFFER:
            return

        message = "\n".join(MESSAGE_BUFFER) + "\n"
        MESSAGE_BUFFER = []

        for subscriber in SUBSCRIBERS:
            try:
                subscriber.write_message(message)
            except:
                logging.error("Error sending message", exc_info=True)

    handlers = [
        (r"/", MainHandler),
        (r"/data", DataHandler),
    ]

    app = tornado.web.Application(handlers, template_path=os.path.join(os.path.dirname(__file__), "templates"))
    app.listen(8888)

    loop = tornado.ioloop.IOLoop.current()
    
    callback = tornado.ioloop.PeriodicCallback(periodic, PUBLISH_INTERVAL)
    callback.start()
    
    loop.start()

def main():
    parser = OptionParser()
    parser.add_option("-a", "--address",
                      dest="address", type='string', default=None,
                      help="device mac adress.")
    parser.add_option("-n", "--name",
                      dest="name", type='string', default=None,
                      help="name of the device.")
    parser.add_option("-b", "--backend",
                      dest="backend", type='string', default="auto",
                      help="pygatt backend to use. can be auto, gatt or bgapi")
    parser.add_option("-i", "--interface",
                      dest="interface", type='string', default=None,
                      help="The interface to use, 'hci0' for gatt or a com port for bgapi")

    (options, _) = parser.parse_args()

    start_eeg_thread(options)
    start_app()

if __name__ == "__main__":
    main()
