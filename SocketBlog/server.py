import logging

__author__ = 'jawaad'

import tornado
import tornado.websocket


class Blog(tornado.websocket.WebSocketHandler):
    pass


class BlogWebSocketHandler(tornado.websocket.WebSocketHandler):
    """
    Make your blog and the changes done to it available over websockets.
    """
    def open(self):
        logging.info('new connection')
        self.write_message("Hello World")

    def on_close(self):
        logging.info('connection closed')

    def on_message(self, message):
        logging.info('Test Module Message Received: %s' % message)
        self.write('test1')
