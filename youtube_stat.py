import requests
import json


class YtStat:
    def __init__(self, api_key, vedio_id):
        self.api_key = api_key
        self.vedio_id = vedio_id
        self.channel_stat = None

    def get_channel_stat(self):
        url = 'https://www.googleapis.com/youtube/v3/videos?id=oBImb0PDcnA&key=AIzaSyB_u-AH7p2gllCUxkmszpnCJ3mu75Pc8YA&fields=items(statistics(viewCount))&part=statistics'
        json_url = requests.get(url)

        data = json.loads(json_url.text)
        tim = data["items"][0]
        bim = tim["statistics"]
        cim = bim['viewCount']
        return cim;




