import os
from urllib.parse import urlparse
import yt_dlp

def validate_url(url: str) -> bool:
    """Check if the URL is a valid YouTube or Apple Podcast URL."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    return ('youtube.com' in domain or 'youtu.be' in domain or 'podcasts.apple.com' in domain)

def download_audio(url: str, download_path: str) -> str:
    """Download audio from a URL using yt_dlp and return the path to the downloaded MP3 file."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        base_filename = os.path.join(download_path, f"{info['id']}")
        audio_file = base_filename + '.mp3'
        return audio_file