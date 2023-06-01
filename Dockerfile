FROM python:3.10-slim
WORKDIR /app
COPY main.py /app
COPY requirements.txt /app
RUN apt update && apt install -y git ffmpeg
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
CMD ["python", "main.py"]
