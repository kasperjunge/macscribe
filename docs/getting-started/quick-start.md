# Quick Start

## Basic Usage

```bash
macscribe <INPUT> [OPTIONS]
```

`<INPUT>`: URL (YouTube, Apple Podcast, X) or local file path
`[OPTIONS]`: `--model`, `--output`

## Examples

### YouTube Video

```bash
macscribe https://youtube.com/watch?v=VIDEO_ID
```

Downloads audio, transcribes, copies to clipboard.

### Local Audio

```bash
macscribe audio.mp3
```

Supports: MP3, WAV, FLAC, M4A, OGG, WMA

### Local Video

```bash
macscribe video.mp4
```

Supports: MP4, MOV, AVI, MKV, WEBM, M4V, WMV

### Apple Podcast

```bash
macscribe https://podcasts.apple.com/us/podcast/...
```

### X (Twitter)

```bash
macscribe https://x.com/user/status/123
```

### Save to File

```bash
# Specific file
macscribe audio.mp3 --output transcript.txt

# Directory (auto-generates filename)
macscribe audio.mp3 --output ./transcripts/
```

## Custom Models

Default: `mlx-community/whisper-large-v3-mlx`

```bash
macscribe video.mp4 --model mlx-community/whisper-medium-mlx
```

**Available models** (from Hugging Face):

- `whisper-large-v3-mlx` - Most accurate
- `whisper-medium-mlx` - Balanced
- `whisper-small-mlx` - Faster
- `whisper-base-mlx` - Fastest

## What Happens

1. Downloads/processes audio
2. Transcribes using Whisper
3. Copies to clipboard
4. Saves to file (if `--output` specified)

## Get Help

```bash
macscribe --help
```

## Next Steps

- [Examples](../usage/examples.md) - Real-world use cases
- [Advanced Options](../usage/advanced-options.md) - Customization
