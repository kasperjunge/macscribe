# Macscribe

Transcribe YouTube videos, podcasts, and local audio/video files using Whisper. Transcripts are copied to your clipboard automatically.

## Quick Start

```bash
# Install
pip install macscribe

# Transcribe a YouTube video
macscribe https://youtube.com/watch?v=VIDEO_ID

# Transcribe a local file
macscribe audio.mp3

# Save to file
macscribe audio.mp3 --output transcript.txt
```

## What It Does

- Transcribes YouTube, Apple Podcasts, X (Twitter), and local files
- Supports common audio/video formats (MP3, WAV, MP4, MOV, etc.)
- Uses MLX-optimized Whisper for fast transcription on Apple Silicon
- Copies results to clipboard automatically
- Optionally saves to file with `--output`

## Requirements

- Python 3.12+
- macOS with Apple Silicon (for MLX acceleration)

## Usage

```bash
macscribe <URL_OR_FILE> [OPTIONS]

Options:
  --model    Whisper model to use (default: whisper-large-v3-mlx)
  --output   Save transcript to file or directory
```

## Documentation

Full docs: **https://kasperjunge.github.io/macscribe/**

## License

MIT License - see [LICENSE](LICENSE)