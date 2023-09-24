#credit to xtekky
from urllib.parse  import urlencode
from random        import randint
from tls_client    import Session, response
from utils.bogus   import Signer

class Api:
    def __init__(self, userAgent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'):
        self.userAgent  = userAgent
        self.client     = Session(client_identifier='chrome_109')
        self.signer     = Signer
    
    
    def sign(self, params: str, ua: str) -> str:
        return params + '&X-Bogus=' + self.signer.sign(params, ua)

    
    def get_params(self, extra: dict = {}, device_id: int = randint(7000000000000000000, 7999999999999999999)) -> str:
        return urlencode({
            **extra,
            'aid'               : 1988,
            'app_language'      : 'en',
            'app_name'          : 'tiktok_web',
            'battery_info'      : 1,
            'browser_language'  : 'en',
            'browser_name'      : 'Mozilla',
            'browser_online'    : 'true',
            'browser_platform'  : 'Win32',
            'browser_version'   : self.userAgent,
            'channel'           : 'tiktok_web',
            'cookie_enabled'    : 'true',
            'device_id'         : device_id,
            'device_platform'   : 'web_pc',
            'focus_state'       : 'true',
            'from_page'         : 'user',
            'history_len'       : '3',
            'is_fullscreen'     : 'false',
            'is_page_visible'   : 'true',
            'os'                : 'windows',
            'priority_region'   : 'FR',
            'referer'           : '',
            'region'            : 'FR',
            'screen_height'     : '1080',
            'screen_width'      : '1920',
            'tz_name'           : 'Africa/Casablanca',
            'webcast_language'  : 'en',
        })
    
    def get_headers(self, extra: dict = {}) -> dict:
        return {
            **extra,
            'authority'          : 'www.tiktok.com',
            'accept'             : '*/*',
            'accept-language'    : 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
            'referer'            : 'https://www.tiktok.com/',
            'sec-ch-ua'          : '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile'   : '?0',
            'sec-ch-ua-platform' : '"Windows"',
            'sec-fetch-dest'     : 'empty',
            'sec-fetch-mode'     : 'cors',
            'sec-fetch-site'     : 'same-origin',
            'user-agent'         : self.userAgent
        }

    def user_info(self, uniqueId: str) -> response:
        params = self.get_params({
            'uniqueId': uniqueId
        })

        return self.client.get(f'https://www.tiktok.com/api/user/detail/?{self.sign(params, self.userAgent)}', headers = self.get_headers())
