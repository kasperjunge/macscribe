import os
from urllib.parse import urlparse
import yt_dlp

def validate_input(input_source: str) -> bool:
    """Check if the input is a valid URL or local file path."""
    # Check if it's a local file
    if os.path.isfile(input_source):
        # Check if it has a supported file extension
        supported_extensions = {
            '.mp3', '.wav', '.flac', '.m4a', '.ogg', '.wma',  # audio formats
            '.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.wmv'  # video formats
        }
        _, ext = os.path.splitext(input_source.lower())
        return ext in supported_extensions
    
    # Check if it's a valid URL
    try:
        parsed = urlparse(input_source)
        domain = parsed.netloc.lower()
        return (
            'youtube.com' in domain or 
            'youtu.be' in domain or 
            'podcasts.apple.com' in domain or
            "x.com" in domain
        )
    except:
        return False

def prepare_audio(input_source: str, temp_path: str) -> str:
    """Prepare audio file from URL or local file path. Return path to audio file for transcription."""
    # If it's a local file, just return the path (mlx-whisper handles various formats)
    if os.path.isfile(input_source):
        return input_source
    
    # If it's a URL, download it
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(temp_path, '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(input_source, download=True)
        base_filename = os.path.join(temp_path, f"{info['id']}")
        audio_file = base_filename + '.mp3'
        return audio_file