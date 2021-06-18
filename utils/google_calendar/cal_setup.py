import datetime
import pickle
import os.path
from utils import config as cfg
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import logging

logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

SCOPES = [cfg.config[1]["scopes"]]
CREDENTIALS_FILE = cfg.config[1]["credentials"]


def get_calendar_service():
    creds = None

    if os.path.exists(cfg.config[1]["token.pickle"]):
        with open(cfg.config[1]["token.pickle"], 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(cfg.config[1]["token.pickle"], 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
    return service
