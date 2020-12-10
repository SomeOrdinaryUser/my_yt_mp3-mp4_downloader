from __future__ import unicode_literals
from pytube import YouTube
from pytube import Playlist
import youtube_dl
import ffmpeg
import random, string

# generate unique name so if you want to download both mp3 and mp4 you can
def generate_name():
    password_length = 4
    possible_characters = "!@#$%^&*()"

    random_character_list = [
        random.choice(possible_characters) for i in range(password_length)
    ]
    kek = ".mp3"
    random_password = "%(title)s" + " - " + "".join(random_character_list) + str(kek)
    return random_password


def downloader():
    # ask user for their playlist url
    p_or_s = str(input("Playlist or single? (p/s): "))
    if p_or_s == "s" or p_or_s == "S":
        audio_or_video = str(input("Audio or video? (a/v): "))
        if audio_or_video == "a":
            single_url = str(input("Enter single url: "))
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
                "outtmpl": generate_name(),
            }
            with youtube_dl.YoutubeDL(ydl_opts, "-k") as ydl:
                try:
                    ydl.download([single_url])
                except:
                    print(
                        "oof! URL doesn't exist. Please remove the broken link in your playlist :)"
                    )
                    downloader()
            downloader()
        elif audio_or_video == "v":
            single_url = str(input("Enter single url: "))
            YouTube(single_url).streams.first().download()
            print("Done!")
            downloader()
    elif p_or_s == "p":
        # ask user for their playlist url
        enter_playlist_url = str(input("Enter playlist url: "))
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": generate_name(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([enter_playlist_url])
            except:
                print(
                    "oof! URL doesn't exist. Please remove the broken link in your playlist :)"
                )
                downloader()

    else:
        print("\noops! I didn't catch that. Please re-enter a valid option.")
        downloader()


if __name__ == "__main__":
    downloader()