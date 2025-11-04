# Basic Usage

## Command Syntax

```bash
macscribe <INPUT> [--model MODEL] [--output OUTPUT]
```

### Arguments

**`<INPUT>`** (required): URL or local file path
- YouTube: `https://youtube.com/watch?v=...`
- Apple Podcasts: `https://podcasts.apple.com/...`
- X/Twitter: `https://x.com/username/status/...`
- Local file: `./audio.mp3` or `/path/to/video.mp4`

**`--model`** (optional): Whisper model
- Default: `mlx-community/whisper-large-v3-mlx`
- Example: `--model mlx-community/whisper-medium-mlx`

**`--output` / `-o`** (optional): Save to file
- File path: `transcript.txt`
- Directory: `./transcripts/` (auto-generates filename)
- Creates parent directories automatically

## Supported Formats

**Audio**: MP3, WAV, FLAC, M4A, OGG, WMA
**Video**: MP4, MOV, AVI, MKV, WEBM, M4V, WMV

```bash
macscribe audio.mp3
macscribe video.mp4
```

## Output

Transcripts are automatically copied to clipboard. Use `Cmd+V` to paste.

Save to file:

```bash
# Specific file
macscribe audio.mp3 --output transcript.txt

# Directory (auto-generates filename)
macscribe audio.mp3 --output ./transcripts/
```

## How It Works

**URL sources**: Downloads audio → Transcribes → Copies to clipboard → Cleans up temp files

**Local files**: Validates file → Extracts audio (if video) → Transcribes → Copies to clipboard

## Model Performance

| Model | Accuracy | Speed | RAM |
|-------|----------|-------|-----|
| Large (default) | Excellent | ~5-10x real-time | ~8GB |
| Medium | Very Good | ~3-5x real-time | ~4GB |
| Small | Good | ~2-3x real-time | ~2GB |
| Base | Fair | ~1-2x real-time | ~1GB |

```bash
macscribe audio.mp3 --model mlx-community/whisper-medium-mlx
```

## Requirements

- Apple Silicon (M1/M2/M3+) for MLX acceleration
- RAM varies by model (2-8GB)

## Next Steps

- [Advanced Options](advanced-options.md)
- [Examples](examples.md)
