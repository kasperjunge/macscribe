# Macscribe

Transcribe audio from YouTube, podcasts, and local files using Whisper on Apple Silicon.

## What It Does

Macscribe transcribes YouTube videos, Apple Podcasts, X posts, and local audio/video files. Transcripts are automatically copied to your clipboard and optionally saved to a file.

## Quick Start

```bash
# Install
pip install macscribe

# Transcribe
macscribe https://youtube.com/watch?v=VIDEO_ID
macscribe audio.mp3
macscribe video.mp4 --output transcript.txt
```

## Features

- YouTube, Apple Podcasts, X (Twitter) support
- Local audio (MP3, WAV, FLAC, M4A, OGG, WMA) and video (MP4, MOV, AVI, MKV, WEBM, M4V, WMV)
- MLX-accelerated Whisper for fast transcription on Apple Silicon
- Automatic clipboard integration
- Optional file output
- Custom model support

## Requirements

- Python 3.12+
- macOS with Apple Silicon

## Next Steps

- [Installation Guide](getting-started/installation.md)
- [Quick Start](getting-started/quick-start.md)
- [Usage Examples](usage/examples.md)

## Support

- [GitHub Repository](https://github.com/kasperjunge/macscribe)
- [Report Issues](https://github.com/kasperjunge/macscribe/issues)

## License

MIT License - [View Details](license.md)
