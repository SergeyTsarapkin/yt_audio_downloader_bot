# Youtube Audio Downloader Bot

The Youtube Audio Downloader Bot is a simple Telegram bot that allows you to send a YouTube video link and receive the corresponding audio in MP3 format. Please note that this project is still a work in progress.

## Purpose

The purpose of this bot is to provide an easy way to extract audio from YouTube videos. By sending a YouTube video link to the bot, it will process the video and send back the audio in MP3 format. However, there are a few known issues that are being addressed:

1. **User Interface**: The bot currently lacks some user interface elements in the chat. This is a planned improvement that will be implemented in the near future.
2. **File Size Limitation**: Due to limitations in the Telegram API, the bot is currently unable to send files larger than 50MB. This limitation will be addressed, likely through the implementation of file chunking.
3. **Video Name Issue**: Some videos with names containing a combination of Cyrillic and English letters may exhibit strange behavior. While the bot successfully saves the file under the correct name, an error occurs when attempting to send it.

## Dependencies

Dependencies are listed in the requirements.txt

## Docker Container

The Youtube Audio Downloader Bot is available as a Docker container. You can find the Docker image on [Docker Hub](https://hub.docker.com/r/sergeytsarapkin/yt_loader_bot/tags).

To use the Docker image, you can pull it using the following command:

```shell
docker pull sergeytsarapkin/yt_loader_bot:latest
