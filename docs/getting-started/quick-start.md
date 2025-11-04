# Quick Start

Get up and running with Macscribe in minutes!

## Basic Command Structure

The basic syntax for Macscribe is:

```bash
macscribe <INPUT> [OPTIONS]
```

Where:

- `<INPUT>` is either a URL (YouTube, Apple Podcast, X) or a path to a local audio/video file
- `[OPTIONS]` are optional flags to customize behavior

## Your First Transcription

### Transcribe a YouTube Video

The simplest way to use Macscribe is to transcribe a YouTube video:

```bash
macscribe https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

What happens:

1. Macscribe downloads the audio from the YouTube video
2. The audio is transcribed using the default Whisper model
3. The transcription is automatically copied to your clipboard
4. You can paste it anywhere with `Cmd+V` (macOS)

### Transcribe a Local Audio File

You can also transcribe audio files on your computer:

```bash
macscribe /path/to/your/audio.mp3
```

Supported audio formats:

- MP3
- WAV
- FLAC
- M4A
- OGG
- WMA

### Transcribe a Local Video File

Macscribe can extract and transcribe audio from video files:

```bash
macscribe /path/to/your/video.mp4
```

Supported video formats:

- MP4
- MOV
- AVI
- MKV
- WEBM
- M4V
- WMV

### Transcribe an Apple Podcast Episode

```bash
macscribe https://podcasts.apple.com/us/podcast/example-episode-url
```

### Transcribe from X (Twitter)

```bash
macscribe https://x.com/username/status/1234567890
```

## Using a Different Model

By default, Macscribe uses `mlx-community/whisper-large-v3-mlx`, but you can specify a different model:

```bash
macscribe https://www.youtube.com/watch?v=dQw4w9WgXcQ --model mlx-community/whisper-medium-mlx
```

### Available Models

You can use any MLX-compatible Whisper model from Hugging Face, such as:

- `mlx-community/whisper-large-v3-mlx` (default, most accurate)
- `mlx-community/whisper-medium-mlx` (good balance)
- `mlx-community/whisper-small-mlx` (faster, less accurate)
- `mlx-community/whisper-base-mlx` (fastest, basic accuracy)

## Understanding the Output

When you run Macscribe, you'll see progress messages:

```bash
$ macscribe https://www.youtube.com/watch?v=example
Downloading audio...
Transcribing audio...
Transcription copied to clipboard.
```

The transcription is now in your clipboard and ready to paste!

## Common Use Cases

### Meeting Notes

Record a meeting and transcribe it:

```bash
macscribe /path/to/meeting-recording.m4a
```

### YouTube Research

Quickly get transcripts of YouTube videos for research:

```bash
macscribe https://www.youtube.com/watch?v=educational-video
```

### Podcast Episodes

Get transcripts of podcast episodes:

```bash
macscribe https://podcasts.apple.com/us/podcast/episode-url
```

### Interview Transcription

Transcribe recorded interviews:

```bash
macscribe /path/to/interview.mp3
```

## What's Next?

- Learn about [Basic Usage](../usage/basic-usage.md) for more details
- Explore [Advanced Options](../usage/advanced-options.md) for customization
- See more [Examples](../usage/examples.md) for specific scenarios

## Getting Help

If you need help at any time, run:

```bash
macscribe --help
```

This will show you all available options and commands.
