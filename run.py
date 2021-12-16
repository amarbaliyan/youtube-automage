from youtube_stat import YtStat
import requests
import json

from clients.youtube_client import YouTubeClient


from PIL import Image,ImageDraw,ImageFont
OPENSANS_FONT_FILE ='./fonts/OpenSans-ExtraBold.ttf'
IMAGE_INPUT_FILE='./image_2.jpeg'
IMAGE_OUTPUT_FILE='./NEW_IMAGE.jpeg'
YOUTUBE_VIDEO_ID='ZUYrnz30_kY'
youtube_data_api_crediantials_location='./creds/client_secret.json'
API_key='AIzaSyB_u-AH7p2gllCUxkmszpnCJ3mu75Pc8YA'
CHANNEL_ID='UC2bvjvcVwslruy-vIqD-YEw'
TITLE="this"
CATOGARY=int("25")



def create_thumbnail(view_counts):
    print("creating the thumbnail")
    image= Image.open(IMAGE_INPUT_FILE)
    font= ImageFont.truetype(OPENSANS_FONT_FILE,80)
    drawing= ImageDraw.Draw(image)
    drawing.text((550,380), str(view_counts), font=font, fill='#FFFFFF')
    image.save(IMAGE_OUTPUT_FILE)


def set_thumbnail_video( video_id , thumbnail):
    youtube_client = YouTubeClient(youtube_data_api_crediantials_location)
    response = youtube_client.set_thumbnail(video_id , thumbnail)
    print(response)

def view_count(API_key, YOUTUBE_VEDIO_ID):
    url =   f'https://www.googleapis.com/youtube/v3/videos?id={YOUTUBE_VEDIO_ID}&key={API_key}&fields=items(statistics(viewCount))&part=statistics'
    json_url = requests.get(url)

    data = json.loads(json_url.text)
    tim=data["items"][0]
    bim=tim["statistics"]
    cim=bim['viewCount']
    return cim


def CHANGE_VIDEO_TITLE(video_id,title,catagory):
    youtube_client=YouTubeClient(youtube_data_api_crediantials_location)
    response_1=youtube_client.change_title(video_id,title,catagory)
    print(response_1)
    print("getting title")









def run():
    #get current view
    #edit the thumbnai
    #upload that thumbnail

    VIEW_COUNT=view_count(API_key,YOUTUBE_VIDEO_ID)
    print("getting view count",VIEW_COUNT)

    create_thumbnail(VIEW_COUNT)
    set_thumbnail_video(YOUTUBE_VIDEO_ID , IMAGE_OUTPUT_FILE)
    CHANGE_VIDEO_TITLE(YOUTUBE_VIDEO_ID, TITLE, CATOGARY)
    print("title changes")



if __name__=='__main__':
    run()