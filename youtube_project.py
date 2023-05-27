import pandas as pd
import seaborn as sns 
import numpy as np
from googleapiclient.discovery import build
import pymongo
import mysql.connector
import re
import isodate


channel_ids = ['UCpNUYWW0kiqyh0j5Qy3aU7w','UCnz-ZXXER4jOvuED5trXfEA','UCc8_LsRYszE9-T-BkIcS7jw','UC1RhziSm9jDbXwlcXMfEB7w','UCDwynAD0hf96TQ-7ATS4hYg']

api_key = 'AIzaSyCYfsYTMGua8jL8paIoIy5biijwBRYQpE4'
channel_id = channel_ids[0]
youtube = build('youtube','v3',developerKey=api_key)

def get_channel_details(youtube,channel_ids):
    all_data = []
    request = youtube.channels().list(
            part = 'snippet,contentDetails,statistics',
            id = ','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(
            channel_id = response['items'][i]['id'],
            channel_name = response['items'][i]['snippet']['title'],
            channel_type = response['items'][i]['kind'],
            channel_views = response['items'][i]['statistics']['viewCount'],
            channel_description = response['items'][i]['snippet']['description'],
            channel_subscibers = response['items'][i]['statistics']['subscriberCount'],
            channel_videos = response['items'][i]['statistics']['videoCount'],
            playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'] )
        all_data.append(data)
    return all_data
channels_details = get_channel_details(youtube,channel_ids)
channel_data = pd.DataFrame(channels_details)


playlist_ids = list(channel_data['playlist_id'])
def get_playlists(youtube,channel_ids):
    all_data = []
    request = youtube.channels().list(
            part = 'snippet,contentDetails,statistics',
            id = ','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(
            playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'],
            channel_id = response['items'][i]['id']  )
        all_data.append(data)
    return all_data
playlists = get_playlists(youtube,channel_ids)
playlist_data = pd.DataFrame(playlists)
# print(playlist_ids)


playlist_id = playlist_ids[4]
def get_videos(youtube,playlist_id):
    video_ids = []
    request = youtube.playlistItems().list(
        part = 'snippet,contentDetails',
        playlistId = playlist_id,
        maxResults = 50 )
    response = request.execute()
    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])
    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
        part = 'snippet,contentDetails',
        playlistId = playlist_id,
        maxResults = 50,
        pageToken = next_page_token )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = response.get('nextPageToken')
    return video_ids
video_ids = get_videos(youtube,playlist_id)
# print(video_ids)


def get_playlists(youtube,channel_ids):
    request = youtube.channels().list(
            part = 'snippet,contentDetails,statistics',
            id = ','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
            playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
    return playlist_id
playlist_id = get_playlists(youtube,channel_ids)
def get_video_details(youtube, video_ids):
    all_data = []
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=','.join(video_ids[i:i+50]))
        response = request.execute()
        for video in response['items']:
            data = {
                'video_id': video['id'],
                'playlist_id':playlist_id,
                'video_title': video['snippet']['title'],
                'video_description': video['snippet']['description'],
                'video_tags': video['snippet'].get('tags', []),
                'video_published': video['snippet']['publishedAt'],
                'video_views': video['statistics']['viewCount'],
                'video_likes': video['statistics']['likeCount'],
                'video_favour': video['statistics']['favoriteCount'],
                'video_comments': video['statistics']['commentCount'],
                'video_thumbnail': video['snippet']['thumbnails']['default']['url'],
                'video_duration': video['contentDetails']['duration'],
                'video_status': video['contentDetails'].get('caption', '')
            }
            all_data.append(data)
    return all_data
video_details=get_video_details(youtube,video_ids)
video_data = pd.DataFrame(video_details)


def comment_in_videos(youtube,video_ids):
    all_comments = []
    for video_id in video_ids:
        request = youtube.commentThreads().list(
            part = 'id,replies,snippet',
            videoId = video_id )
        response = request.execute()
        for comment in response['items']:
            data = {
                'comment_id':comment['snippet']['topLevelComment']['etag'],
                'video_id':comment['snippet']['topLevelComment']['snippet']['videoId'],
                'comment_author':comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                'comment_published':comment['snippet']['topLevelComment']['snippet']['publishedAt'],
                'comment':comment['snippet']['topLevelComment']['snippet']['textDisplay']
            }
            all_comments.append(data)
    return all_comments
comment_details=comment_in_videos(youtube,video_ids)
comment_df = pd.DataFrame(comment_details)




client = pymongo.MongoClient('mongodb://localhost:27017')
mongo_db = client['youtube']
channels = mongo_db['channels']
channels.drop()
channels = mongo_db['channels']
channels.insert_many(channels_details)

playlists_mongo = mongo_db['playlists_mongo']
playlists_mongo.drop()
playlists_mongo = mongo_db['playlists_mongo']
playlists_mongo.insert_many(playlists)

videos = mongo_db['videos']
videos.drop()
videos = mongo_db['videos']
videos.insert_many(video_details)

comments = mongo_db['comments']
comments.drop()
comments = mongo_db['comments']
comments.insert_many(comment_details)





db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Samy@1007",
    database="youtube"
)

csr = db.cursor()
csr.execute('drop table comments')
csr.execute('drop table videos')
csr.execute('drop table playlist')
csr.execute('drop table channels')

csr.execute("create table channels(channel_id varchar(255) primary key, channel_name varchar(255), channel_type varchar(255), channel_view int, channel_description text, channel_subscriber int, channel_videos int )")
for doc in channels.find():
    c_id = doc['channel_id']
    c_name = doc['channel_name']
    c_type = doc['channel_type']
    c_view = int(doc['channel_views'])
    c_description = doc['channel_description']
    c_subscriber = int(doc['channel_subscibers'])
    c_videos = int(doc['channel_videos'])
    csr.execute(f"INSERT INTO channels(channel_id, channel_name, channel_type, channel_view, channel_description, channel_subscriber, channel_videos ) VALUES ('{c_id}', '{c_name}', '{c_type}', {c_view}, '{c_description}', {c_subscriber}, {c_videos})")
db.commit()

csr.execute("create table playlist( playlist_id varchar(255) primary key, channel_id varchar(255), foreign key(channel_id) references channels(channel_id) )")
for doc in playlists_mongo.find():
    p_id = doc['playlist_id']
    c_id = doc['channel_id']
    csr.execute(f"INSERT INTO playlist(playlist_id, channel_id ) VALUES ('{p_id}', '{c_id}')")
db.commit()

csr.execute("create table videos( video_id varchar(255) primary key, playlist_id varchar(255), video_name varchar(255), video_description text, published_date datetime, view_count int, like_count int, favour_count int, comment_count int, duration varchar(255), thumbnail varchar(255), caption_status varchar(255), year int, duration_int int, foreign key(playlist_id) references playlist(playlist_id) )")
v_published = [] 
video_duration = []
for doc in videos.find():
    v_id = doc['video_id']
    p_id = doc['playlist_id']
    v_name = doc['video_title']
    clean_name = re.sub(r'\W+', ' ', v_name)
    v_description = doc['video_description']
    clean_text = re.sub(r'\W+', ' ', v_description)
    v_published.append(doc['video_published'])
    publish_df = pd.DataFrame({'publish': v_published})
    publish_df['published']=pd.to_datetime(publish_df['publish'])
    for i in publish_df['published']:
        v_published_date = str(i)  
    v_views = doc['video_views']
    v_likes = doc['video_likes']
    v_favour = doc['video_favour']
    v_comments = doc['video_comments']
    v_duration = doc['video_duration']
    v_thumbnail = doc['video_thumbnail']
    v_status = doc['video_status']
    publish_df['year']=publish_df['published'].dt.year
    for j in publish_df['year']:
        v_year = int(j)
    video_duration.append(doc['video_duration'])
    duration_df = pd.DataFrame({'duration': video_duration})
    duration_df['durations']=duration_df['duration'].apply(lambda a : isodate.parse_duration(a))
    duration_df['durations']=duration_df['durations'].astype('timedelta64[s]')
    duration_df['Durations']=duration_df['durations'].astype('int')
    for k in duration_df['Durations']:
        v_duration_int = k
    csr.execute(f" insert into videos(video_id, playlist_id, video_name, video_description, published_date, view_count, like_count, favour_count, comment_count, duration, thumbnail, caption_status, year, duration_int) values('{v_id}', '{p_id}', '{clean_name}', '{clean_text}', '{v_published_date}', {v_views}, {v_likes}, {v_favour}, '{v_comments}', '{v_duration}', '{v_thumbnail}', '{v_status}', {v_year}, {v_duration_int} )")
db.commit()

csr.execute("create table comments( comment_id varchar(255) primary key , video_id varchar(255), comment_author varchar(255), comment_published datetime, comment text, foreign key(video_id) references videos(video_id) )")
c_published = [] 
for doc in comments.find():
    c_id = doc['comment_id']
    v_id = doc['video_id']
    c_author = doc['comment_author']
    comment_author = re.sub(r'\W+', ' ', c_author)
    c_published.append(doc['comment_published'])
    comment_df = pd.DataFrame({'comment_published': c_published})
    comment_df['c_published']=pd.to_datetime(comment_df['comment_published'])
    for i in comment_df['c_published']:
        c_published_date = str(i)
    c_text = doc['comment']
    clean_text = re.sub(r'\W+', ' ', c_text)
    csr.execute(f"insert into comments(comment_id, video_id, comment_author, comment_published, comment) values('{c_id}', '{v_id}', '{comment_author}', '{c_published_date}', '{clean_text}' )")
db.commit()