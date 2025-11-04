# Basic Usage

This guide covers the fundamental usage patterns of Macscribe.

## Command Syntax

```bash
macscribe <INPUT> [--model MODEL] [--output OUTPUT]
```

### Required Arguments

#### `<INPUT>`

The input source for transcription. This can be:

1. **A URL** from supported platforms:
   - YouTube (e.g., `https://www.youtube.com/watch?v=...`)
   - Apple Podcasts (e.g., `https://podcasts.apple.com/...`)
   - X/Twitter (e.g., `https://x.com/username/status/...`)

2. **A local file path**:
   - Absolute path (e.g., `/Users/username/audio.mp3`)
   - Relative path (e.g., `./recordings/meeting.mp4`)

### Optional Arguments

#### `--model`

Specify a Hugging Face model for transcription.

- **Type**: String
- **Default**: `mlx-community/whisper-large-v3-mlx`
- **Example**: `--model mlx-community/whisper-medium-mlx`

#### `--output` or `-o`

Save the transcript to a text file.

- **Type**: String (file path or directory path)
- **Default**: None (transcript is only copied to clipboard)
- **Behavior**:
  - If a file path is provided (e.g., `transcript.txt`), saves to that exact file
  - If a directory path is provided (e.g., `./transcripts/`), auto-generates filename based on the audio file name
  - Creates parent directories if they don't exist
- **Examples**:
  - `--output transcript.txt` - Save to specific file
  - `-o ./transcripts/` - Save to directory with auto-generated name
  - `--output ~/Documents/my-transcript.txt` - Save to specific path

## Input Sources

### YouTube Videos

Macscribe supports various YouTube URL formats:

```bash
# Standard format
macscribe https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Short format
macscribe https://youtu.be/dQw4w9WgXcQ

# With timestamp
macscribe "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s"
```

!!! tip
    Always wrap URLs with parameters in quotes to avoid shell interpretation issues.

### Apple Podcasts

```bash
macscribe https://podcasts.apple.com/us/podcast/podcast-name/id123456789
```

### X (Twitter)

```bash
macscribe https://x.com/username/status/1234567890
```

### Local Audio Files

Macscribe supports the following audio formats:

| Format | Extension | Notes |
|--------|-----------|-------|
| MP3 | `.mp3` | Most common format |
| WAV | `.wav` | Uncompressed, high quality |
| FLAC | `.flac` | Lossless compression |
| M4A | `.m4a` | Apple audio format |
| OGG | `.ogg` | Open source format |
| WMA | `.wma` | Windows Media Audio |

```bash
macscribe /path/to/audio.mp3
```

### Local Video Files

Macscribe can extract audio from video files:

| Format | Extension | Notes |
|--------|-----------|-------|
| MP4 | `.mp4` | Most common video format |
| MOV | `.mov` | Apple video format |
| AVI | `.avi` | Legacy video format |
| MKV | `.mkv` | Matroska container |
| WEBM | `.webm` | Web video format |
| M4V | `.m4v` | Apple video variant |
| WMV | `.wmv` | Windows Media Video |

```bash
macscribe /path/to/video.mp4
```

## How Macscribe Works

### For URL Sources

1. **Validation**: Checks if the URL is from a supported platform
2. **Download**: Uses `yt-dlp` to download the audio stream
3. **Temporary Storage**: Saves audio to a temporary directory
4. **Transcription**: Processes the audio with the Whisper model
5. **Clipboard**: Copies the result to your clipboard
6. **Cleanup**: Removes temporary files

### For Local Files

1. **Validation**: Checks if the file exists and has a supported extension
2. **Preparation**: If it's a video file, extracts the audio track
3. **Transcription**: Processes the audio with the Whisper model
4. **Clipboard**: Copies the result to your clipboard

## Output

The transcription is automatically copied to your system clipboard. You can:

- Paste it into any application with `Cmd+V` (macOS)
- Use it immediately in your workflow
- Save it to a file using the `--output` flag

### Saving to a File

#### Using the `--output` Flag (Recommended)

The easiest way to save transcripts is using the `--output` flag:

```bash
# Save to a specific file
macscribe audio.mp3 --output transcript.txt

# Save to a directory (auto-generates filename based on audio file)
macscribe audio.mp3 --output ./transcripts/

# Save with absolute path
macscribe https://youtube.com/video -o ~/Documents/transcripts/video.txt
```

#### Manual Clipboard Save

Alternatively, you can paste the clipboard contents:

```bash
# Run transcription
macscribe audio.mp3

# Then paste to a file (macOS)
pbpaste > transcript.txt
```

Or redirect using shell:

```bash
macscribe audio.mp3 && pbpaste > transcript.txt
```

## Progress Indicators

Macscribe provides feedback during operation:

```
Downloading audio...        # When downloading from URL
Preparing local file...     # When processing local files
Transcribing audio...       # During transcription
Transcription copied to clipboard.  # Success!
```

## Error Handling

If something goes wrong, Macscribe will display an error message:

```bash
# Invalid URL
$ macscribe https://invalid-url.com
Invalid input. Please provide a valid URL (YouTube, Apple Podcast, X) or path to a local audio/video file.

# File not found
$ macscribe nonexistent.mp3
Invalid input. Please provide a valid URL (YouTube, Apple Podcast, X) or path to a local audio/video file.

# Download error
$ macscribe https://youtube.com/invalid
Error preparing audio: [error details]

# Transcription error
$ macscribe corrupted-audio.mp3
Error during transcription: [error details]
```

## Performance Considerations

### Model Size vs Speed

Larger models are more accurate but slower:

- **Large** (default): Best accuracy, slower (~5-10x real-time)
- **Medium**: Good balance (~3-5x real-time)
- **Small**: Faster, less accurate (~2-3x real-time)
- **Base**: Fastest, basic accuracy (~1-2x real-time)

### Hardware Requirements

- Macscribe uses Apple's MLX framework for hardware acceleration
- Requires Apple Silicon (M1, M2, M3, etc.) for optimal performance
- RAM usage varies with model size (2-8GB)

## Best Practices

1. **Use appropriate models**: Choose the model based on your needs for speed vs accuracy
2. **Check audio quality**: Better audio quality leads to better transcriptions
3. **Manage clipboard**: Be aware that transcription overwrites your clipboard
4. **Handle errors gracefully**: Check error messages for troubleshooting guidance

## Next Steps

- Learn about [Advanced Options](advanced-options.md) for more control
- See [Examples](examples.md) for real-world scenarios
- Check the [API Reference](../api-reference.md) for technical details
