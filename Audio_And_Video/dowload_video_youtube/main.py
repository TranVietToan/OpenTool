import yt_dlp
from pytube import YouTube
import logging
import sys

log_file = str(sys.argv[0]).replace('.py', '') + '_log.txt'
logging.basicConfig(filename=log_file, format='%(asctime)s - %(message)s', level=logging.INFO)

video_url = "https://youtu.be/ySE68bz6VYQ"
output_path = "D:\LogOpenTool\Audio_And_Video\Video\dowload_video_from_youtube"
def dowload_youtube_video_using_pytube(video_url, output_path):
    youtube = YouTube(video_url, output_path)

    logging.info(f"Title video: {youtube.title}")
    try:
        video_stream = youtube.streams.get_highest_resolution() #videos have the best quality
        video_stream.download(output_path)
        return True
    
    except Exception as e:
        logging.error("There was an error during the download, try another way")
        return False

def download_youtube_video_using_yt_dlp(video_url, output_path):
    try:
        ydl_opts = {
            'format': 'best',  #videos have the best quality
            'outtmpl': f'{output_path}/%(title)s.%(ext)s'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return True
    
    except Exception as e:
        logging.error("Unable to load now, please try again later")
        return False

def run(video_url, output_path):
    logging.info("Start downloading videos")

    if dowload_youtube_video_using_pytube(video_url, output_path):
        logging.info("Complete the download process...!")
    elif download_youtube_video_using_yt_dlp(video_url, output_path):
        logging.info("Complete the download process...!")
    else:
        logging.error('End of program')

run(video_url, output_path)
