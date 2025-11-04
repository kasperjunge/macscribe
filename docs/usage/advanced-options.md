# Advanced Options

This guide covers advanced usage patterns and customization options for Macscribe.

## Custom Models

### Choosing a Model

Macscribe supports any MLX-compatible Whisper model from Hugging Face. The model choice affects accuracy, speed, and resource usage.

```bash
macscribe <INPUT> --model <MODEL_NAME>
```

### Available Models

#### Official MLX Whisper Models

| Model | Size | Accuracy | Speed | Memory |
|-------|------|----------|-------|--------|
| `mlx-community/whisper-large-v3-mlx` | ~3GB | Excellent | Slow | ~8GB |
| `mlx-community/whisper-large-v2-mlx` | ~3GB | Excellent | Slow | ~8GB |
| `mlx-community/whisper-medium-mlx` | ~1.5GB | Very Good | Medium | ~4GB |
| `mlx-community/whisper-small-mlx` | ~500MB | Good | Fast | ~2GB |
| `mlx-community/whisper-base-mlx` | ~150MB | Fair | Very Fast | ~1GB |
| `mlx-community/whisper-tiny-mlx` | ~75MB | Basic | Fastest | ~512MB |

#### Example Usage

```bash
# Use medium model for faster processing
macscribe video.mp4 --model mlx-community/whisper-medium-mlx

# Use small model for quick transcripts
macscribe podcast.mp3 --model mlx-community/whisper-small-mlx
```

### Model Selection Guidelines

Choose your model based on your needs:

**Use Large (default) when:**

- Accuracy is critical
- You have time to wait
- Transcribing accented or technical content
- Processing professional content

**Use Medium when:**

- You need a balance of speed and accuracy
- Processing clear audio with minimal background noise
- General purpose transcription

**Use Small when:**

- Speed is important
- Audio quality is good
- Content is straightforward (no heavy accents or jargon)

**Use Base/Tiny when:**

- You need very quick results
- Doing rough transcription for review
- Working with limited resources

## Working with Different Audio Sources

### YouTube Videos

#### Handling Playlists

Currently, Macscribe processes single videos. For playlists, you'll need to transcribe each video individually:

```bash
macscribe https://www.youtube.com/watch?v=VIDEO_ID_1
macscribe https://www.youtube.com/watch?v=VIDEO_ID_2
```

#### Long Videos

For very long videos (>2 hours), transcription may take significant time:

```bash
# Consider using a faster model for long content
macscribe https://youtube.com/long-video --model mlx-community/whisper-medium-mlx
```

### Local Files

#### Batch Processing

To transcribe multiple files, use shell scripting with the `--output` flag:

```bash
# Process all MP3 files in a directory
for file in *.mp3; do
    echo "Processing $file"
    macscribe "$file" --output "${file%.mp3}.txt"
done
```

Or save to a dedicated transcripts directory:

```bash
# Create transcripts directory
mkdir -p transcripts

# Process all MP3 files and save to transcripts/
for file in *.mp3; do
    echo "Processing $file"
    macscribe "$file" --output transcripts/
done
```

#### Large Files

For large audio/video files:

1. Ensure you have sufficient disk space for temporary files
2. Consider using a smaller/faster model
3. Be patient - processing time scales with file length

```bash
# Process a 2-hour podcast with medium model
macscribe long-podcast.mp3 --model mlx-community/whisper-medium-mlx
```

## Advanced Workflows

### Transcription Pipeline

Create a complete transcription pipeline using the `--output` flag:

```bash
#!/bin/bash
# transcribe-and-save.sh

INPUT="$1"
OUTPUT="$2"
MODEL="${3:-mlx-community/whisper-large-v3-mlx}"

echo "Transcribing $INPUT with $MODEL..."
macscribe "$INPUT" --model "$MODEL" --output "$OUTPUT"

if [ $? -eq 0 ]; then
    echo "Transcription saved to $OUTPUT"
else
    echo "Transcription failed"
    exit 1
fi
```

Usage:

```bash
chmod +x transcribe-and-save.sh
./transcribe-and-save.sh video.mp4 transcript.txt
# Or with custom model
./transcribe-and-save.sh video.mp4 transcript.txt mlx-community/whisper-medium-mlx
```

### Automated Transcript Organization

```bash
#!/bin/bash
# organize-transcripts.sh

MEDIA_DIR="./media"
TRANSCRIPT_DIR="./transcripts"

mkdir -p "$TRANSCRIPT_DIR"

for file in "$MEDIA_DIR"/*.{mp3,mp4,m4a}; do
    if [ -f "$file" ]; then
        basename=$(basename "$file")
        name="${basename%.*}"

        echo "Transcribing $basename..."
        macscribe "$file" --output "$TRANSCRIPT_DIR/${name}.txt"
        echo "Saved to $TRANSCRIPT_DIR/${name}.txt"
    fi
done
```

### Integration with Other Tools

#### Combine with Text Processing

```bash
# Transcribe and count words
macscribe audio.mp3
pbpaste | wc -w

# Transcribe and search for keywords
macscribe video.mp4
pbpaste | grep -i "important keyword"

# Transcribe and format with prettier
macscribe podcast.mp3
pbpaste | prettier --parser markdown > formatted.md
```

#### Use with Git for Version Control

```bash
# Transcribe and commit
macscribe meeting.mp3 --output transcripts/meeting-2024-01-01.txt
git add transcripts/meeting-2024-01-01.txt
git commit -m "Add meeting transcript"
```

## Performance Optimization

### Optimizing for Speed

1. **Use smaller models**: Trade accuracy for speed
2. **Pre-process audio**: Convert to a standard format
3. **Batch processing**: Process multiple files in sequence

```bash
# Fast transcription with small model
macscribe audio.mp3 --model mlx-community/whisper-small-mlx
```

### Optimizing for Accuracy

1. **Use the largest model**: Default is already optimal
2. **Improve audio quality**: Use high-quality source material
3. **Clean audio**: Remove background noise before transcription

### Resource Management

Monitor resource usage during transcription:

```bash
# In another terminal, monitor resources
top -pid $(pgrep -f macscribe)
```

## Troubleshooting Advanced Scenarios

### Handling Special Characters in URLs

Always quote URLs with special characters:

```bash
macscribe "https://youtube.com/watch?v=id&t=30s"
```

### Processing Protected Content

Some content may be protected or region-locked:

```bash
# If download fails, check yt-dlp output for details
macscribe https://protected-video-url
```

### Dealing with Corrupted Files

If transcription fails with local files:

1. Check file integrity
2. Try converting to a different format
3. Use audio editing software to repair

```bash
# Convert to WAV first (requires ffmpeg)
ffmpeg -i problematic.mp3 fixed.wav
macscribe fixed.wav
```

## Tips and Tricks

### Quick Clipboard Management

```bash
# Save current clipboard before transcription
pbpaste > saved-clipboard.txt

# Run transcription
macscribe audio.mp3

# Restore previous clipboard if needed
cat saved-clipboard.txt | pbcopy
```

### Creating Transcription Aliases

Add to your `.bashrc` or `.zshrc`:

```bash
# Quick transcription with medium model
alias qscribe='macscribe --model mlx-community/whisper-medium-mlx'

# Transcribe and save
tsave() {
    macscribe "$1"
    pbpaste > "${1%.*}.txt"
    echo "Saved to ${1%.*}.txt"
}
```

### Comparing Models

Test different models on the same audio:

```bash
#!/bin/bash
AUDIO="test-audio.mp3"

for model in tiny base small medium large; do
    echo "Testing mlx-community/whisper-${model}-mlx"
    time macscribe "$AUDIO" --model "mlx-community/whisper-${model}-mlx"
    pbpaste > "transcript-${model}.txt"
done
```

## Next Steps

- See [Examples](examples.md) for real-world use cases
- Check the [API Reference](../api-reference.md) for technical details
- Read about [Contributing](../contributing.md) to improve Macscribe
