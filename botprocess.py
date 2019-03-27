# -*- coding: utf-8 -*-
#

from google.appengine.ext import ndb
import datetime

import botmsg
import etheraddr_check
import email_check

class DBSTATUS(ndb.Model):
    mode = ndb.IntegerProperty(required=True, indexed=True, default=0)
    msg = ndb.StringProperty()
    etheraddr = ndb.StringProperty()
    email = ndb.StringProperty()
    username = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    date = ndb.DateTimeProperty()


def process(msg_id, chat_id, msg, initmode):
    u"""process: 사용자의 메시지를 따라서 답장
    msg_id: (integer) msg ID
    chat_id:  (integer) 채팅 ID
    text:     (string)  사용자가 보낸 메시지 내용
    initmode: (integer) chat 시작 시 0 
    """
    username = 'username'
    first_name = 'first_name'
    last_name = 'last_name'
    if 'username' in msg['chat']:
        username = msg['chat']['username']
    if 'first_name' in msg['chat']:
        first_name = msg['chat']['first_name']
    if 'last_name' in msg['chat']:
        last_name = msg['chat']['last_name']
    text = msg.get('text')

    if text == 'resetme':
        status = DBSTATUS.get_by_id(str(chat_id))
        status.mode = 1
        status.put()
        return []

    if initmode == 0:
        status = DBSTATUS.get_or_insert(str(chat_id))
        if status.mode == 3:
            return [botmsg.MSG_COMPLETE]
        status.mode = 1
        status.msg = text
        status.username = username
        status.first_name = first_name
        status.last_name = last_name
        status.date = datetime.datetime.now()
        status.put()
        return [botmsg.MSG_SET_ETHER_ADDR]
    else:
        status = DBSTATUS.get_by_id(str(chat_id))
        mode = status.mode

# etheraddr
    if mode == 1:
        if etheraddr_check.ethereum_addr_check(text):
            status.mode = 2
            status.msg = text
            status.etheraddr = text
            status.username = username
            status.first_name = first_name
            status.last_name = last_name
            status.date = datetime.datetime.now()
            status.put()
            return [botmsg.MSG_SET_ETHER_ADDR_SUCESSE, botmsg.MSG_SET_EMAIL]
        else:
            status.mode = 1
            status.msg = text
            status.username = username
            status.first_name = first_name
            status.last_name = last_name
            status.date = datetime.datetime.now()
            status.put()
            return [botmsg.MSG_WRONGINPUT, botmsg.MSG_RESET_ETHER_ADDR]
# email
    if mode == 2:
        if email_check.email_check(text):
            status.mode = 3
            status.msg = text
            status.email = text
            status.username = username
            status.first_name = first_name
            status.last_name = last_name
            status.date = datetime.datetime.now()
            status.put()
            return [botmsg.MSG_SET_EMAIL_SUCESSE, botmsg.MSG_COMPLETE]
        else:
            status.mode = 2
            status.msg = text
            status.username = username
            status.first_name = first_name
            status.last_name = last_name
            status.date = datetime.datetime.now()
            status.put()
            return [botmsg.MSG_WRONGINPUT, botmsg.MSG_RESET_EMAIL]

    return [botmsg.MSG_COMPLETE]


def getData(handler):
    return
