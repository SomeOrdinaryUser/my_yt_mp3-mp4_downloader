from __future__ import unicode_literals
import getpass
import youtube_dl

# get users name of computer so you don't need to change any code if you download this source
username = getpass.getuser()

print(
    f"""
    - Welcome {username}, This is a prompt-based youtube downloader that can download audio or video.
    - Made using youtube_dl library.
    - Each file includes metadata and song artwork pulled from the videos thumbnail.
    """
)

# generate file name
def generate_name():
    ext = ".%(ext)s"
    conc_str = (
        "C:/Users/"
        + username
        + "/Music/yt_downloader/audio/"
        + "%(title)s"
        + " - "
        + str(ext)
    )
    return conc_str


# download audio
def download_audio():
    single_url = str(input("Enter single url: "))
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
    with youtube_dl.YoutubeDL(ydl_opts, "-k") as ydl:
        try:
            ydl.download([single_url])
        except:
            print(
                "oof! URL doesn't exist. Please remove the broken link in your playlist :)"
            )
            print("Done!\n")
            menu()


# download video
def download_video():
    single = str(input("Enter a url: "))
    ydl_opts = {
        "outtmpl": "C:/Users/" + username + "Music/yt_downloader/videos/" + "%(title)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([single])
        menu()


# download playlist
def download_playlist():
    enter_playlist_url = str(input("Enter playlist url: "))
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
            ydl.download([enter_playlist_url])
        except:
            print(
                "oof! URL doesn't exist. Please remove the broken link in your playlist :)"
            )
    print("\nDone downloading playlist.")
    menu()


# main menu
def menu():
    while True:
        # download playlist or single url
        p_or_s = str(input("Playlist or single? (p/s): "))
        if p_or_s == "s" or p_or_s == "S":
            audio_or_video = str(input("Audio or video? (a/v): "))
            if audio_or_video == "a":
                download_audio()
            elif audio_or_video == "v":
                download_video()
        elif p_or_s == "p":
            download_playlist()
        else:
            print("\noops! I didn't catch that. Please re-enter a valid option.")
            menu()


if __name__ == "__main__":
    menu()
