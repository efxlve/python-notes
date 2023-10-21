from pytube import YouTube
from pytube.cli import on_progress


def download_video_with_progress(url, path):
    video = YouTube(url, on_progress_callback=on_progress)

    print("******************** Video Title ********************")
    print(video.title)

    print("******************** Thumbnail Image ********************")
    print(video.thumbnail_url)

    print("******************** Download Video ********************")
    video_stream = video.streams.get_highest_resolution()
    video_stream.download(path)


if __name__ == "__main__":
    url = input("Enter video URL: ")
    path = input("Enter the file path: ")
    download_video_with_progress(url, path)
