import sys
from datetime import datetime
import time
import re
import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()
def since_epcoh(date_string):
    return (inttime.mktime(datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()) * 1000)

def search_yt():
    client = gdata.youtube.service.YouTubeService()
    v_id = '8rSH8-pbHZ0'
    #vid_pat = re.compile(r'videos/(.*?)/comments')
    #vid_list = []
    #entry = yt_service.GetYouTubeVideoEntry(v_id)
    comment_list = []
    comment_feed =yt_service.GetYouTubeVideoCommentFeed(video_id=v_id)
    for comment in comment_feed:
        if ':' in comment:
            comment_list.append(comment)

    print(comment_list)

search_yt()

