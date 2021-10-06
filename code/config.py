import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings['VERSION']
    SECRET_KEY = None


    # Supported types with rules
    CCT_OBSERVABLE_TYPES = {
        'ip': {},
        'user': {}
    }

    CTR_HEADERS = {
        'User-Agent': ('SecureX Threat Response Integrations '
                       '<tr-integrations-support@cisco.com>')
    }
