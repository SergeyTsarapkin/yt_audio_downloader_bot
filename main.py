import youtube_dl
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

load_dotenv('.token')
TOKEN = token = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token = TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class DownloadStates(StatesGroup):
    WaitingForURL = State()


# Handler for the start command
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "Welcome to the YouTube audio downloader bot! Send me a YouTube video URL to download its audio.")
    await DownloadStates.WaitingForURL.set()


@dp.message_handler(state=DownloadStates.WaitingForURL)
async def process_url(message: types.Message):
    video_url = message.text
    await message.reply("Processing the URL and downloading the audio...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            title = ydl.extract_info(video_url, download=False)['title'] + '.mp3'
            ydl.download([video_url])
            with open(title, 'rb') as audio_file:
                await message.reply_document(audio_file)
            os.remove(title)
        except Exception as e:
            logging.error(f"Error occurred during download: {e}")
            await message.reply("Sorry, an error occurred during the download."
                                " Please make sure you provided a valid YouTube video URL.")


if __name__ == '__main__':
    logging.info("Starting the bot...")
    executor.start_polling(dp, skip_updates=True)