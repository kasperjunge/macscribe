# Macscribe

Welcome to the Macscribe documentation! Macscribe is a powerful command-line tool for transcribing audio from various sources.

## What is Macscribe?

Macscribe is a command-line tool that makes it easy to transcribe audio from YouTube videos, Apple Podcast episodes, X (Twitter) posts, and local audio/video files. It downloads audio from URLs or processes local files, transcribes them using state-of-the-art machine learning models, and copies the transcription directly to your clipboard for easy use.

## Key Features

- **Multi-Platform Support**: Accepts YouTube, Apple Podcast, and X URLs
- **Local File Support**: Transcribes local audio files (MP3, WAV, FLAC, M4A, OGG, WMA) and video files (MP4, MOV, AVI, MKV, WEBM, M4V, WMV)
- **Automated Audio Processing**: Downloads high-quality audio from URLs or processes local files directly
- **State-of-the-Art Transcription**: Utilizes `mlx-whisper` for accurate and fast transcription
- **Clipboard Integration**: Automatically copies the transcript to your clipboard
- **Customizable Models**: Option to specify a different Hugging Face model for transcription
- **Simple CLI Interface**: Easy-to-use command-line interface built with Typer

## Quick Example

```bash
# Transcribe a YouTube video
macscribe https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Transcribe a local audio file
macscribe /path/to/your/audio.mp3

# Use a custom model
macscribe https://podcasts.apple.com/... --model some/alternative-model
```

## Requirements

- Python 3.12 or later
- macOS (uses MLX for hardware acceleration on Apple Silicon)

## Get Started

Ready to get started? Check out the [Installation Guide](getting-started/installation.md) or jump straight to the [Quick Start Guide](getting-started/quick-start.md).

## Support

If you encounter any issues or have questions, please:

- Check the documentation sections on the left
- Visit the [GitHub repository](https://github.com/kasperjunge/macscribe)
- Open an issue on GitHub

## License

Macscribe is licensed under the MIT License. See the [License](license.md) page for details.
