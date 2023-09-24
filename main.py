from requests           import get
from concurrent.futures import ThreadPoolExecutor
from utils.userinfo     import Api
from os                 import makedirs
from random             import randint



def download(url):
    makedirs(name, exist_ok=True)
    id       = f"{randint(1000000, 9999999)}.mp4"
    filename = f"{name}/{id}"

    print("[~] Downloading", id)

    r = get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024 * 1024):
            f.write(chunk)
            
    print("[+] Downloaded ", id)


def scrape(secid):
    max_cursor  = 0

    while True:
        try:
            params = {
                "source"        : "0",
                "max_cursor"    : max_cursor,
                "sec_user_id"   : secid,
                "count"         : "20",
                "iid"           : randint(7000000000000000000, 7999999999999999999),
                "device_id"     : randint(7000000000000000000, 7999999999999999999),
                "channel"       : "googleplay",
                "aid"           : "1233",
            }

            response = get("https://api31-core-useast2a.tiktokv.com/aweme/v1/aweme/post/", params=params).json()
            for vid in response["aweme_list"]:
                video = vid['video']['bit_rate'][0]["play_addr"]["url_list"][0]
                exc.submit(download, video)

            if not response["has_more"] or response["has_more"] == 0:
                return

            max_cursor = response["max_cursor"]
        except Exception as e:
            print(e)
            continue

def name2sec(name):
    res = Api().user_info(name).json()
    return res["userInfo"]["user"]["secUid"]

if __name__ == "__main__":

    exc = ThreadPoolExecutor(20) # threads

    name    = input("[?] Enter username >>> @")
    sec     = name2sec(name)
    print("[+] Got secId:", sec)
    scrape(sec)
    exc.shutdown(wait=True)