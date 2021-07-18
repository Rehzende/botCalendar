import http.client, json
from datetime import date
from datetime import datetime,timedelta
import datetime


dt = datetime.datetime.now()

startTime = dt.replace(hour=6, minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
endTime  = dt.replace(day=9, hour=23, minute=30, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

def agenda():
    conn = http.client.HTTPSConnection("api.calendly.com")
    headers = {
        'authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjIyNTgwMTU5LCJqdGkiOiJjZjZjMTEzNC02NGZhLTRkNTEtYjM0MC1kZWZmMDBkODlhNTciLCJ1c2VyX3V1aWQiOiJFQ0dHUVU2WTVaRldZRkVIIn0.8Xm2RsfezOsnB4Qc6WQ_tDectplwICeUX1WIujCq6Kw",
        'Prefer': "code=200, dynamic=true, example=Example"
        }

    conn.request("GET", "/scheduled_events?user=https%3A%2F%2Fapi.calendly.com%2Fusers%2FECGGQU6Y5ZFWYFEH&organization=https%3A%2F%2Fapi.calendly.com%2Forganizations%2FADCERYAHBHZMLH5E&sort=start_time%3Aasc&min_start_time=" + startTime + "&max_start_time=" + endTime , headers=headers)
    res = conn.getresponse()
    return json.load(res)
