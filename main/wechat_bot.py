import datetime
import logging
import threading
import time
import urllib
import itchat
from itchat.content import *

from config import LOG_FILE,CMD_QR,UNKNOWN_MSG,KEYWORDS_RANDOM,KEYWORDS_SALMON_RUN,KEYWORDS_LEAGUE,KEYWORDS_RANKED,KEYWORDS_REGULAR

import sys
sys.path.append('../splatoon2_bot_core/')
from base_config import API_RANKED, API_REGULAR, API_LEAGUE,TMP_IMG,TMP_DIR

from reply import replySalmonRun,replyBattle,replyRandom,replyUnknown

# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send(UNKNOWN_MSG)

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True, isFriendChat=True)
def reply(msg):
    # logging.info(str(msg))
    request_input: str = msg.text
    request_time = msg.createTime
    requester = msg.user

    def any_in(keywords: [str]) -> bool:
        return any(keyword in request_input for keyword in keywords)
    
    if not request_input.startswith("查询"):
        return

    if len(request_input)==2:
        t = threading.Thread(target=replyUnknown,args=[requester])
        t.start()
    
    elif any_in(KEYWORDS_RANDOM):
        t = threading.Thread(target=replyRandom,args=[requester,request_input])
        t.start()
    elif any_in(KEYWORDS_SALMON_RUN):
        t = threading.Thread(target=replySalmonRun,args=[requester, request_time])
        t.start()
    else:
        mode = None
        if any_in(KEYWORDS_LEAGUE):
            mode = API_LEAGUE
        elif any_in(KEYWORDS_RANKED):
            mode = API_RANKED
        elif any_in(KEYWORDS_REGULAR):
            mode = API_REGULAR
        if mode is None:
            t = threading.Thread(target=replyUnknown,args=[requester])
            t.start()
        else:
            t = threading.Thread(target=replyBattle,args=[requester, mode, request_time, request_input])
            t.start()


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, filemode="a", level=logging.INFO)
    if CMD_QR:
        itchat.auto_login(enableCmdQR=2)
    else:
        itchat.auto_login()
    t = threading.Thread(itchat.run())
    t.start()