"""
- Welcome to my youtube searcher/downloader.
- Made using youtube_dl library and selenium.
- Each file includes metadata and song artwork pulled from the videos thumbnail.
"""
# from __future__ import unicode_literals  # Uncomment this if you use python2
import os
import youtube_dl
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import webbrowser
import pyperclip

# Get name of computer so user doesn't need to change any code
username = os.getlogin()

choice = None


def search_song():
    global choice
    song_name = input("Enter song name: ")
    new_song_name = song_name.replace(" ", "+")

    options = Options()
    options.headless = True
    print("booting up selenium")
    driver = webdriver.Firefox(
        executable_path=r"C:\\webdriver\\geckodriver.exe", options=options
    )
    print("\033c")

    driver.get(f"https://www.youtube.com/results?search_query={new_song_name}")
    print("Getting first 6 songs...")
    data = ""
    stop = 2
    start = 0
    index = 1
    links = []
    for title in driver.find_elements_by_xpath('//*[@id="video-title"]')[0:6]:
        data += f"{index}. " + title.text
        link = title.get_attribute("href")
        links.append(link)
        index += 1
        for channel in driver.find_elements_by_css_selector("div.ytd-channel-name a")[
            start:stop
        ]:
            data += channel.text + "\n"
            stop += 1
            start += 1
    print(data)
    driver.quit()
    menyoo = input("Enter song number (1-6): ")
    choice = links[int(menyoo) - 1]
    pyperclip.copy(choice)
    print("url copied to clipboard.")
    if menyoo == "":
        search_song()
    while True:
        try:
            play_or_not = input(
                """
1. Play song
2. Download song
\nChoice: """
            )
            play_or_not = int(play_or_not)
            if play_or_not == 1:
                choice = links[int(menyoo) - 1]
                webbrowser.open(choice, new=0)
                good = input("happy with your choice? (y/n): ")
                if good == "y":
                    a_or_v()
                elif good == "n":
                    search_song()
            if play_or_not == 2:
                a_or_v()
            elif play_or_not == "":
                search_song()
            else:
                print("must be between 1 and 2")
                continue
        except:
            print("ValueError: must be between 1 and 2")


def generate_audio_name():
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


def generate_videos_name():
    if cust == "":
        ext = ".%(ext)s"
        conc_str = (
            "C:/Users/"
            + username
            + "/Music/yt_downloader/videos/"
            + "%(title)s"
            + str(ext)
        )
        return conc_str
    else:
        ext = ".%(ext)s"
        conc_str = (
            "C:/Users/"
            + username
            + f"/Music/yt_downloader/videos/{cust}/"
            + "%(title)s"
            + str(ext)
        )
        return conc_str


# Download audio [single/playlist]
def download_audio():
    global choice
    if choice is None:
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
            "outtmpl": generate_audio_name(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([single_url])
                main_menu()
            except:
                print("")
                main_menu()

    else:
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
            "outtmpl": generate_audio_name(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([choice])
                choice = None
                main_menu()
            except:
                print("Something went wrong, try again...")
                main_menu()


# Download video [single/playlist]
def download_video():
    global choice
    if choice is None:
        single = str(input("Enter url: "))
        ydl_opts = {
            "outtmpl": generate_videos_name(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([single])
        main_menu()
    else:
        ydl_opts = {
            "outtmpl": generate_videos_name(),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([choice])
                choice = None
                main_menu()
            except:
                print("Something went wrong, try again...")
                main_menu()


# Main menu
def a_or_v():
    global cust
    while True:
        audio_or_video = str(input("Audio or video? (a/v): "))
        if audio_or_video == "a":
            cust = input(
                """Enter new folder name to create/save to or leave blank for default (/Music/yt_downloader/audio): """
            )
            download_audio()
        elif audio_or_video == "v":
            cust = input(
                """Enter new folder name to create/save to or leave blank for default (/Music/yt_downloader/videos): """
            )
            download_video()
        else:
            print("Please re-enter a valid option.")
            main_menu()


def main_menu():
    while True:
        menyu = input(
            """
1. Search
2. Download
3. Exit
\nEnter Choice: """
        )
        menyu = int(menyu)
        if menyu == 1:
            search_song()
        elif menyu == 2:
            a_or_v()
        elif menyu == 3:
            exit()
        else:
            print("Unknown option.")
            continue


if __name__ == "__main__":
    main_menu()
