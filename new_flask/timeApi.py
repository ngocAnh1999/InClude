# encoding=utf-8

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from ..flask_rak import RAK, session, context, audio, statement, question
from . import api
import os, sys

from ..askTime import askTime
# logging
import logging
import logging.handlers as handlers
import time
import datetime

logger = logging.getLogger('ask_time_app')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Infor log Handler
inforLogHandler = handlers.TimedRotatingFileHandler('./logger/hoi_thoi_gian_infor.log', when="d", interval=1)
inforLogHandler.setLevel(logging.INFO)
inforLogHandler.setFormatter(formatter)

# Erorr log handler
errorLogHandler = handlers.TimedRotatingFileHandler('./logger/hoi_thoi_gian_error.log', when="d", interval=1)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)

logger.addHandler(inforLogHandler)
logger.addHandler(errorLogHandler)


ask_time_app = RAK(
    app_name='ask time',
    app=api,
    route='/time'
)
@ask_time_app.intent('hoi_gio')
def getHour(entities):
    logger.info("Intent: hoi_gio")
    now = datetime.datetime.now()
    speech_text = "Bây giờ là {} giờ {} phút".format(now.hour, now.minute) 
    logger.info(speech_text)
    return statement(ask_time_app.app_name, speech_text)


@ask_time_app.intent('hoi_ngay')
def getDay(entities):
    logger.info("Intent : hoi_ngay , entities : {}".format(entities))
    startDate, day = None, None
    for entity in entities :
        if(entity['entity'] == '$datetime'):
            startDate = entity['real_value']['result']
            day = entity['value']
    logger.info("startDate: {}  day: {}".format(startDate, day))
    try :
        response = askTime.getDay(startDate)
        logger.info("response: {}".format(response))
        speech_text = "{} là ngày {} tháng {} năm {}".format(day ,response['monthDay'], response['month'], response['year'])
        return statement(ask_time_app.app_name, speech_text)
    except ValueError as e:
        logger.error("Error {}".format(e))
        speech_text = "Ngày này không tồn tại"
        return statement(ask_time_app.app_name, speech_text)
    # logger.info("start intent hoi_ngay with entities: {}".format(entities))
    # startDate, day = None, None
    # for entity in entities:
    #     if entity['entity'] == "$datetime":
    #         startDate = entity['real_value']['result']
    #         day = entity['value']

    # logger.info("startDate: {}  day: {}".format(startDate, day))
    # try:
    #     response = askTime.getDay(startDate)
    #     logger.info("response: {}".format(response))
    #     speech_text = "%s là ngày %d tháng %d" % (day ,response['monthDay'], response['month'])
    #     # print speech_text
    #     return statement(ask_time_app.app_name, speech_text)
    

@ask_time_app.intent('hoi_thu')
def getWeekDay(entities):
    logger.info("start intent hoi_thu with entities: {}".format(entities))
    startDate, day = None, None
    for entity in entities:
        if entity['entity'] == "$datetime":
            startDate = entity['real_value']['result']
            day = entity['value']

    logger.info("startDate {} day {}".format(startDate, day))
    try:
        response = askTime.getWeekDay(startDate)
        logger.info("response: {}".format(response))
        if response['weekDay'] == "chủ nhật":
            speech_text = "%s là %s" % (day ,response['weekDay'])
        else:
            speech_text = "%s là thứ %s" % (day ,response['weekDay'])
        # print speech_text
        return statement(ask_time_app.app_name, speech_text)
    except ValueError as e:
        logger.error("Error {}".format(e))
        speech_text = "Ngày này không tồn tại"
        return statement(ask_time_app.app_name, speech_text)

