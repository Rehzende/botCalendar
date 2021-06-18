import datetime
from utils.google_calendar.cal_setup import get_calendar_service
from utils import config as cfg
import logging
from dateutil import tz

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def getEvents():
   service = get_calendar_service()
   # Call the Calendar API
   dt = datetime.datetime.now()
   BR = tz.gettz('America/Sao_Paulo')  
   start_date = datetime.datetime(dt.year, dt.month, dt.day, 6, 00, 00,0 ,tzinfo=BR).isoformat() 
   end_date = datetime.datetime(dt.year,  dt.month,  dt.day, 23, 30, 59, 0,tzinfo=BR).isoformat() 

   events_result = service.events().list(
       calendarId=cfg.config[1]['calendar_id'], timeMin=start_date, timeMax=end_date,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])
   return events