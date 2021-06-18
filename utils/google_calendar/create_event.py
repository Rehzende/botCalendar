from datetime import timedelta
from utils.google_calendar.cal_setup import get_calendar_service
from utils import config as cfg



def createEvent(eventName, eventDate, EventLocation):
   service = get_calendar_service()

   data = eventDate 
   start = data.isoformat()
   end = (data + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId=cfg.config[1]['calendar_id'],
       body={
           "summary": eventName,
           "description": 'Esse é um Happy Hour da comunidade Mentoria IAC, fique a vontade para participar e conhecer a galera!',
           "location": EventLocation,
           "start": {"dateTime": start, "timeZone": 'America/Sao_Paulo'},
           "end": {"dateTime": end, "timeZone": 'America/Sao_Paulo'},
       }
   ).execute()
   return event_result
