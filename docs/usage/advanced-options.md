# Advanced Options

## Models

All MLX-compatible Whisper models from Hugging Face are supported.

### Available Models

| Model | Size | Accuracy | Speed | RAM |
|-------|------|----------|-------|-----|
| `whisper-large-v3-mlx` (default) | ~3GB | Excellent | Slow | ~8GB |
| `whisper-large-v2-mlx` | ~3GB | Excellent | Slow | ~8GB |
| `whisper-medium-mlx` | ~1.5GB | Very Good | Medium | ~4GB |
| `whisper-small-mlx` | ~500MB | Good | Fast | ~2GB |
| `whisper-base-mlx` | ~150MB | Fair | Very Fast | ~1GB |
| `whisper-tiny-mlx` | ~75MB | Basic | Fastest | ~512MB |

All models prefixed with `mlx-community/`

```bash
macscribe video.mp4 --model mlx-community/whisper-medium-mlx
```

### When to Use Each Model

- **Large**: Accented/technical content, maximum accuracy
- **Medium**: General purpose, good balance
- **Small**: Clear audio, need speed
- **Base/Tiny**: Quick drafts, limited resources

## Batch Processing

Process multiple files:

```bash
# All files in directory
for file in audio/*.mp3; do
    macscribe "$file" --output "transcripts/$(basename "$file" .mp3).txt"
done

# Save to directory with auto-generated names
for file in *.mp3; do
    macscribe "$file" --output transcripts/
done
```

## Long Content

For videos >2 hours, use a faster model:

```bash
macscribe long-video.mp4 --model mlx-community/whisper-medium-mlx
```

## Workflows

### Transcription Pipeline

```bash
#!/bin/bash
INPUT="$1"
OUTPUT="$2"
MODEL="${3:-mlx-community/whisper-large-v3-mlx}"

macscribe "$INPUT" --model "$MODEL" --output "$OUTPUT"
```

### Text Processing

```bash
# Word count
macscribe audio.mp3 --output transcript.txt
wc -w transcript.txt

# Search keywords
macscribe video.mp4 --output transcript.txt
grep -i "keyword" transcript.txt
```

### Version Control

```bash
macscribe meeting.mp3 --output transcripts/2024-01-01.txt
git add transcripts/2024-01-01.txt
git commit -m "Add meeting transcript"
```

## Optimization

**Speed**: Use smaller models

```bash
macscribe audio.mp3 --model mlx-community/whisper-small-mlx
```

**Accuracy**: Use default (large) model, ensure high-quality audio

## Shell Aliases

Add to `.bashrc` or `.zshrc`:

```bash
# Fast transcription
alias qscribe='macscribe --model mlx-community/whisper-medium-mlx'

# Auto-save
tsave() {
    macscribe "$1" --output "${1%.*}.txt"
}
```

## Troubleshooting

**URLs with special characters**: Use quotes

```bash
macscribe "https://youtube.com/watch?v=id&t=30s"
```

**Corrupted files**: Convert first

```bash
ffmpeg -i problematic.mp3 fixed.wav
macscribe fixed.wav
```

## Next Steps

- [Examples](examples.md)
- [API Reference](../api-reference.md)
