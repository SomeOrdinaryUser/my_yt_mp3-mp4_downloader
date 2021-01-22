# from __future__ import unicode_literals # Uncomment this if you use python2
import getpass
import youtube_dl

# Get name of computer so user doesn't need to change any code.
username = getpass.getuser()

print(
    f"""
    - Welcome {username}, This is a prompt-based youtube downloader that can download audio or video.
    - Made using youtube_dl library.
    - Each file includes metadata and song artwork pulled from the videos thumbnail.
    """
)


def generate_name():
    if cust == "":
        ext = ".%(ext)s"
        conc_str = (
            "C:/Users/"
            + username
            + "/Music/yt_downloader/audio/"
            + "%(title)s"
            + str(ext)
        )
        return conc_str
    else:
        ext = ".%(ext)s"
        conc_str = (
            "C:/Users/"
            + username
            + f"/Music/yt_downloader/audio/{cust}/"
            + "%(title)s"
            + str(ext)
        )
        return conc_str


# Download audio [single/playlist]
def download_audio():
    single_url = str(input("Enter url: "))
    ydl_opts = {
        "writethumbnail": True,
        "ignoreerrors": True,
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "EmbedThumbnail"},
            {"key": "FFmpegMetadata"},
        ],
        "outtmpl": generate_name(),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([single_url])
        except:
            print(
                "URL doesn't exist. Please remove the broken link in your playlist :)"
            )
            menu()


# download video
def download_video():
    single = str(input("Enter url: "))
    ydl_opts = {
        "outtmpl": "C:/Users/"
        + username
        + "/Music/yt_downloader/videos/"
        + "%(title)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([single])
        menu()


# Main menu
def menu():
    global cust
    while True:
        cust = input(
            """Enter custom location path or leave blank for default (/Music/yt_downloader/audio): """
        )
        audio_or_video = str(input("Audio or video? (a/v): "))
        if audio_or_video == "a":
            download_audio()
        elif audio_or_video == "v":
            download_video()
        else:
            print("oops! I didn't catch that. Please re-enter a valid option.")
            menu()


if __name__ == "__main__":
    menu()
