#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import codecs
class MyWXBot(WXBot):
    
    def handle_msg_all(self, msg):      
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if 'detail' in msg['content']:
                print(msg)
                if msg['content']['data'] == "BotStart1":
                    print("I'm setting group1 to " + msg['user']['id'])
                    global group1
                    group1 = msg['user']['id']
                elif msg['content']['data'] == "BotStart2":
                    global group2
                    group2 = msg['user']['id']
                if msg['user']['id'] == group1:
                    self.send_msg_by_uid(msg['content']['data'] + ' (From: ' + msg['content']['user']['name'] + ')', group2)
                elif msg['user']['id'] == group2:
                    self.send_msg_by_uid(msg['content']['data'] + ' (From: ' + msg['content']['user']['name'] + ')', group1)
                else:
                    print(msg['user']['id'])


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()