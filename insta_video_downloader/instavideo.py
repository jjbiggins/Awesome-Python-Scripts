import urllib.request
import requests
import json
import re
import sys

def download(post_id):
    videos = []
    data = requests.get(f"https://instagram.com/p/{post_id}")
    if data.status_code == 404:
        print("Specified post not found")
        sys.exit()
    json_data = json.loads(re.findall(r'window._sharedData\s=\s(\{.*\});</script>', data.text)[0])
    data = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    multiple_posts = 'edge_sidecar_to_children' in data.keys()
    caption = data['edge_media_to_caption']['edges'][0]['node']['text']
    media_url = data['display_resources'][2]['src']
    is_video = data['is_video']
    if not is_video and not multiple_posts:
        print("No Videos found")
        sys.exit()
    if is_video:
        videos.append(data['video_url'])
    if multiple_posts:
        videos.extend(
            post['node']['video_url']
            for post in data['edge_sidecar_to_children']['edges']
            if post['node']['is_video']
        )

    print(f"Found total {len(videos)} videos")
    for no, video in zip(list(range(len(videos))), videos):
        print(f"Downloading video {no}")
        urllib.request.urlretrieve(video, f"{post_id}_{no}.mp4")

if len(sys.argv) == 1:
    print("Please provide instagram post id")
else:
    download(sys.argv[1])