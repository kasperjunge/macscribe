# API Reference

Technical reference for Macscribe's internal modules and functions.

## Command Line Interface

### Main Command

```bash
macscribe <INPUT> [--model MODEL]
```

#### Arguments

**`input_source`** (positional, required)

- **Type**: `str`
- **Description**: URL of a YouTube/Apple Podcast/X video, or path to local audio/video file
- **Examples**:
  - `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
  - `/path/to/audio.mp3`
  - `./video.mp4`

**`--model`** (optional)

- **Type**: `str`
- **Default**: `mlx-community/whisper-large-v3-mlx`
- **Description**: Hugging Face model to use for transcription
- **Examples**:
  - `mlx-community/whisper-medium-mlx`
  - `mlx-community/whisper-small-mlx`

#### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Invalid input, download error, or transcription error |

## Python Modules

### `macscribe.cli`

Main CLI module using Typer.

#### `main(input_source: str, model: str) -> None`

Main entry point for the CLI application.

**Parameters:**

- `input_source` (str): URL or file path to transcribe
- `model` (str): Hugging Face model name

**Returns:** None

**Raises:**

- `typer.Exit(code=1)`: On invalid input, download failure, or transcription error

**Example:**

```python
from macscribe.cli import app

if __name__ == "__main__":
    app()
```

### `macscribe.downloader`

Handles downloading audio from URLs and preparing local files.

#### `validate_input(input_source: str) -> bool`

Validates whether the input is a supported URL or existing local file.

**Parameters:**

- `input_source` (str): URL or file path to validate

**Returns:** `bool` - True if valid, False otherwise

**Supported URLs:**

- YouTube: `youtube.com`, `youtu.be`
- Apple Podcasts: `podcasts.apple.com`
- X/Twitter: `x.com`, `twitter.com`

**Supported File Extensions:**

- Audio: `.mp3`, `.wav`, `.flac`, `.m4a`, `.ogg`, `.wma`
- Video: `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`, `.m4v`, `.wmv`

**Example:**

```python
from macscribe.downloader import validate_input

# Valid URL
is_valid = validate_input("https://youtube.com/watch?v=abc123")
# Returns: True

# Valid file
is_valid = validate_input("/path/to/audio.mp3")
# Returns: True if file exists

# Invalid input
is_valid = validate_input("https://unsupported-site.com")
# Returns: False
```

#### `prepare_audio(input_source: str, output_dir: str) -> str`

Downloads audio from URL or prepares local file for transcription.

**Parameters:**

- `input_source` (str): URL or file path
- `output_dir` (str): Directory for temporary audio files

**Returns:** `str` - Path to the prepared audio file

**Raises:**

- `Exception`: On download failure or file processing error

**Example:**

```python
from macscribe.downloader import prepare_audio
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    audio_file = prepare_audio(
        "https://youtube.com/watch?v=abc123",
        tmpdir
    )
    # Returns: "/tmp/tmpdir/audio.mp3"
```

### `macscribe.transcriber`

Handles audio transcription using MLX Whisper.

#### `transcribe_audio(audio_file: str, model: str) -> None`

Transcribes audio file and copies result to clipboard.

**Parameters:**

- `audio_file` (str): Path to audio file
- `model` (str): Hugging Face model name

**Returns:** None (copies result to clipboard)

**Raises:**

- `Exception`: On transcription failure

**Example:**

```python
from macscribe.transcriber import transcribe_audio

transcribe_audio(
    "/path/to/audio.mp3",
    "mlx-community/whisper-large-v3-mlx"
)
# Transcription is now in clipboard
```

### `macscribe.clipboard`

Handles clipboard operations.

#### `copy_to_clipboard(text: str) -> None`

Copies text to system clipboard.

**Parameters:**

- `text` (str): Text to copy

**Returns:** None

**Platform Support:**

- macOS: Uses `pbcopy`

**Example:**

```python
from macscribe.clipboard import copy_to_clipboard

copy_to_clipboard("Hello, world!")
# Text is now in clipboard
```

## Dependencies

### Core Dependencies

#### yt-dlp

Used for downloading audio from URLs.

**Version:** ≥2025.1.12

**Usage in Macscribe:**

```python
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

#### mlx-whisper

MLX-accelerated Whisper for transcription.

**Version:** ≥0.4.1

**Usage in Macscribe:**

```python
import mlx_whisper

result = mlx_whisper.transcribe(
    audio_file,
    path_or_hf_repo=model
)
transcript = result["text"]
```

#### typer

CLI framework.

**Version:** ≥0.15.1

**Usage in Macscribe:**

```python
import typer

app = typer.Typer()

@app.command()
def main(input_source: str, model: str = "default"):
    # CLI logic
    pass
```

## File Formats

### Supported Audio Formats

| Format | Extension | MIME Type | Notes |
|--------|-----------|-----------|-------|
| MP3 | `.mp3` | `audio/mpeg` | Most common |
| WAV | `.wav` | `audio/wav` | Uncompressed |
| FLAC | `.flac` | `audio/flac` | Lossless |
| M4A | `.m4a` | `audio/mp4` | Apple format |
| OGG | `.ogg` | `audio/ogg` | Open source |
| WMA | `.wma` | `audio/x-ms-wma` | Windows Media |

### Supported Video Formats

| Format | Extension | MIME Type | Notes |
|--------|-----------|-----------|-------|
| MP4 | `.mp4` | `video/mp4` | Most common |
| MOV | `.mov` | `video/quicktime` | Apple format |
| AVI | `.avi` | `video/x-msvideo` | Legacy |
| MKV | `.mkv` | `video/x-matroska` | Container |
| WEBM | `.webm` | `video/webm` | Web format |
| M4V | `.m4v` | `video/x-m4v` | Apple variant |
| WMV | `.wmv` | `video/x-ms-wmv` | Windows Media |

## Error Handling

### Common Errors

#### Invalid Input Error

```
Invalid input. Please provide a valid URL (YouTube, Apple Podcast, X)
or path to a local audio/video file.
```

**Cause:** Input validation failed

**Solution:** Check URL format or file path

#### Download Error

```
Error preparing audio: [error details]
```

**Causes:**

- Network issues
- Invalid URL
- Protected/private content
- Rate limiting

**Solution:** Check internet connection and URL validity

#### Transcription Error

```
Error during transcription: [error details]
```

**Causes:**

- Corrupted audio file
- Insufficient memory
- Model loading failure

**Solution:** Check file integrity and available resources

## Environment

### System Requirements

- **Operating System**: macOS (required for MLX)
- **Python Version**: ≥3.12
- **Hardware**: Apple Silicon (M1, M2, M3, etc.)
- **RAM**: 4-8GB (depends on model size)
- **Disk Space**: ~5GB for models and temporary files

### Environment Variables

Currently, Macscribe does not use environment variables for configuration.

## Extending Macscribe

### Custom Clipboard Handlers

Extend clipboard support for other platforms:

```python
# macscribe/clipboard.py

import platform
import subprocess

def copy_to_clipboard(text: str) -> None:
    system = platform.system()

    if system == "Darwin":  # macOS
        process = subprocess.Popen(
            ['pbcopy'],
            stdin=subprocess.PIPE
        )
        process.communicate(text.encode('utf-8'))
    elif system == "Linux":
        # Add Linux support
        process = subprocess.Popen(
            ['xclip', '-selection', 'clipboard'],
            stdin=subprocess.PIPE
        )
        process.communicate(text.encode('utf-8'))
    elif system == "Windows":
        # Add Windows support
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
```

### Custom Output Formats

Add support for different output formats:

```python
# macscribe/formatters.py

def format_as_srt(transcript: str, segments: list) -> str:
    """Format transcript as SRT subtitles."""
    srt_content = []
    for i, segment in enumerate(segments, 1):
        start = format_timestamp(segment['start'])
        end = format_timestamp(segment['end'])
        text = segment['text']

        srt_content.append(f"{i}")
        srt_content.append(f"{start} --> {end}")
        srt_content.append(text)
        srt_content.append("")

    return "\n".join(srt_content)
```

## Next Steps

- See [Examples](usage/examples.md) for practical use cases
- Read [Contributing](contributing.md) to extend Macscribe
- Check the [GitHub repository](https://github.com/kasperjunge/macscribe) for source code
