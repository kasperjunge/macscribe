# Examples

Real-world examples of using Macscribe for various transcription tasks.

## Content Research

### Transcribing Educational Videos

Research a topic by transcribing multiple educational videos:

```bash
# Transcribe a lecture
macscribe https://www.youtube.com/watch?v=educational-video-id

# Save the transcript
pbpaste > lecture-notes.txt

# Search for specific topics
cat lecture-notes.txt | grep -i "quantum mechanics"
```

### Academic Research

Process multiple podcast episodes for research:

```bash
#!/bin/bash
# research-podcasts.sh

EPISODES=(
    "https://podcasts.apple.com/episode1"
    "https://podcasts.apple.com/episode2"
    "https://podcasts.apple.com/episode3"
)

mkdir -p research-transcripts

for i in "${!EPISODES[@]}"; do
    echo "Processing episode $((i+1))..."
    macscribe "${EPISODES[$i]}"
    pbpaste > "research-transcripts/episode-$((i+1)).txt"
    sleep 2
done

echo "All episodes transcribed!"
```

## Meeting Documentation

### Recording and Transcribing Meetings

Document team meetings:

```bash
# After recording a meeting with voice recorder
macscribe ~/Recordings/team-meeting-2024-01-15.m4a

# Save with meeting date
pbpaste > ~/Documents/meetings/2024-01-15-team-meeting.txt
```

### Meeting Minutes Template

Create a script to generate formatted meeting minutes:

```bash
#!/bin/bash
# meeting-minutes.sh

RECORDING="$1"
DATE=$(date +%Y-%m-%d)
OUTPUT="meeting-minutes-$DATE.md"

echo "# Meeting Minutes - $DATE" > "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## Attendees" >> "$OUTPUT"
echo "- " >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## Transcript" >> "$OUTPUT"

macscribe "$RECORDING"
pbpaste >> "$OUTPUT"

echo "Meeting minutes saved to $OUTPUT"
open "$OUTPUT"
```

Usage:

```bash
./meeting-minutes.sh meeting-recording.m4a
```

## Content Creation

### YouTube Video Scripts

Transcribe your own videos to create blog posts:

```bash
# Transcribe your video
macscribe https://www.youtube.com/watch?v=your-video-id

# Create a blog post
cat > blog-post.md << 'EOF'
---
title: "My Video Title"
date: 2024-01-15
---

# My Video Title

Here's the transcript of my recent video:

EOF

pbpaste >> blog-post.md
```

### Podcast Show Notes

Generate show notes from podcast episodes:

```bash
#!/bin/bash
# generate-show-notes.sh

EPISODE_URL="$1"
EPISODE_NUM="$2"
TITLE="$3"

OUTPUT="show-notes-ep${EPISODE_NUM}.md"

cat > "$OUTPUT" << EOF
# Episode ${EPISODE_NUM}: ${TITLE}

## Summary

[Add episode summary here]

## Full Transcript

EOF

macscribe "$EPISODE_URL"
pbpaste >> "$OUTPUT"

echo "Show notes generated: $OUTPUT"
```

Usage:

```bash
./generate-show-notes.sh "https://podcasts.apple.com/..." 42 "Amazing Episode"
```

## Accessibility

### Creating Subtitles

Convert transcripts to basic subtitle format:

```bash
# Transcribe video
macscribe video.mp4

# Save transcript
pbpaste > transcript.txt

# Convert to SRT format (requires additional processing)
# This is a simplified example
python3 << 'EOF'
with open('transcript.txt', 'r') as f:
    text = f.read()

# Split into sentences
sentences = text.replace('.', '.\n').split('\n')

with open('subtitles.srt', 'w') as f:
    for i, sentence in enumerate(sentences, 1):
        if sentence.strip():
            f.write(f"{i}\n")
            f.write(f"00:00:{i*2:02d},000 --> 00:00:{(i+1)*2:02d},000\n")
            f.write(f"{sentence.strip()}\n\n")

print("Basic subtitles created: subtitles.srt")
EOF
```

### Audio Description Documentation

Document audio descriptions for accessibility:

```bash
# Transcribe video content
macscribe training-video.mp4

# Create accessibility document
cat > accessibility-doc.md << 'EOF'
# Training Video Transcript

**Purpose**: Provide text alternative for accessibility

**Duration**: [Add duration]

## Transcript

EOF

pbpaste >> accessibility-doc.md
```

## Journalism and Interviews

### Interview Transcription Workflow

Professional interview transcription:

```bash
#!/bin/bash
# interview-workflow.sh

AUDIO_FILE="$1"
INTERVIEWEE="$2"
DATE=$(date +%Y-%m-%d)

OUTPUT_DIR="interviews/$INTERVIEWEE"
mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="$OUTPUT_DIR/interview-$DATE.txt"

echo "Transcribing interview with $INTERVIEWEE..."
macscribe "$AUDIO_FILE" --model mlx-community/whisper-large-v3-mlx

echo "==================================" > "$OUTPUT_FILE"
echo "Interview with $INTERVIEWEE" >> "$OUTPUT_FILE"
echo "Date: $DATE" >> "$OUTPUT_FILE"
echo "==================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

pbpaste >> "$OUTPUT_FILE"

echo "Interview transcribed: $OUTPUT_FILE"
echo "Word count: $(wc -w < "$OUTPUT_FILE")"
```

Usage:

```bash
./interview-workflow.sh interview-audio.mp3 "John Doe"
```

### Quote Extraction

Extract quotes from interviews:

```bash
# Transcribe
macscribe interview.mp3

# Extract potential quotes (lines with quotation marks or key phrases)
pbpaste | grep -E '\".*\"|said|stated|explained' > quotes.txt
```

## Language Learning

### Transcribe Practice Materials

Create study materials from videos:

```bash
#!/bin/bash
# language-practice.sh

VIDEO_URL="$1"
LANGUAGE="$2"

OUTPUT="practice-$LANGUAGE-$(date +%Y%m%d).txt"

echo "Transcribing $LANGUAGE practice material..."
macscribe "$VIDEO_URL"

pbpaste > "$OUTPUT"

echo "Practice material saved: $OUTPUT"
echo "Lines: $(wc -l < "$OUTPUT")"
echo "Words: $(wc -w < "$OUTPUT")"
```

## Archive and Documentation

### Building a Transcript Archive

Create an organized archive of transcripts:

```bash
#!/bin/bash
# build-archive.sh

ARCHIVE_DIR="transcript-archive"
mkdir -p "$ARCHIVE_DIR"/{youtube,podcasts,meetings,interviews}

# Process YouTube videos
process_youtube() {
    local url="$1"
    local category="$2"

    # Extract video ID
    video_id=$(echo "$url" | grep -oP '(?<=v=)[^&]+')

    echo "Processing YouTube: $video_id"
    macscribe "$url"

    pbpaste > "$ARCHIVE_DIR/youtube/${category}-${video_id}.txt"
}

# Process podcasts
process_podcast() {
    local url="$1"
    local name="$2"

    echo "Processing podcast: $name"
    macscribe "$url"

    pbpaste > "$ARCHIVE_DIR/podcasts/${name}-$(date +%Y%m%d).txt"
}

# Example usage
process_youtube "https://youtube.com/watch?v=abc123" "tech-talk"
process_podcast "https://podcasts.apple.com/..." "daily-news"
```

### Search Across Transcripts

Build a searchable transcript database:

```bash
#!/bin/bash
# search-transcripts.sh

KEYWORD="$1"
TRANSCRIPT_DIR="transcript-archive"

echo "Searching for: $KEYWORD"
echo "================================"

grep -r -i -n "$KEYWORD" "$TRANSCRIPT_DIR" | while read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    line_num=$(echo "$line" | cut -d: -f2)
    content=$(echo "$line" | cut -d: -f3-)

    echo "File: $file (Line $line_num)"
    echo "Context: $content"
    echo "---"
done
```

## Batch Processing

### Process Multiple Files

Transcribe all audio files in a directory:

```bash
#!/bin/bash
# batch-transcribe.sh

INPUT_DIR="$1"
OUTPUT_DIR="${2:-transcripts}"

mkdir -p "$OUTPUT_DIR"

# Supported formats
FORMATS=("mp3" "m4a" "wav" "mp4" "mov")

for format in "${FORMATS[@]}"; do
    for file in "$INPUT_DIR"/*."$format"; do
        if [ -f "$file" ]; then
            basename=$(basename "$file" ."$format")
            echo "Processing: $basename"

            macscribe "$file"

            if [ $? -eq 0 ]; then
                pbpaste > "$OUTPUT_DIR/${basename}.txt"
                echo "✓ Saved: $OUTPUT_DIR/${basename}.txt"
            else
                echo "✗ Failed: $basename"
            fi

            # Small delay between files
            sleep 1
        fi
    done
done

echo "Batch processing complete!"
echo "Transcripts saved in: $OUTPUT_DIR"
```

Usage:

```bash
./batch-transcribe.sh ./audio-files ./transcripts
```

### Progress Tracking for Large Batches

```bash
#!/bin/bash
# batch-with-progress.sh

INPUT_DIR="$1"
OUTPUT_DIR="transcripts"

mkdir -p "$OUTPUT_DIR"

FILES=("$INPUT_DIR"/*.{mp3,mp4,m4a})
TOTAL=${#FILES[@]}
CURRENT=0

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        CURRENT=$((CURRENT + 1))
        echo "[$CURRENT/$TOTAL] Processing: $(basename "$file")"

        basename=$(basename "$file")
        name="${basename%.*}"

        macscribe "$file" --model mlx-community/whisper-medium-mlx
        pbpaste > "$OUTPUT_DIR/${name}.txt"

        PROGRESS=$((CURRENT * 100 / TOTAL))
        echo "Progress: $PROGRESS%"
        echo "---"
    fi
done

echo "All files processed!"
```

## Integration Examples

### Slack Integration

Post transcripts to Slack:

```bash
#!/bin/bash
# transcribe-to-slack.sh

AUDIO_FILE="$1"
SLACK_WEBHOOK="$2"

macscribe "$AUDIO_FILE"
TRANSCRIPT=$(pbpaste)

curl -X POST "$SLACK_WEBHOOK" \
  -H 'Content-Type: application/json' \
  -d "{\"text\":\"New Transcript:\\n\\n$TRANSCRIPT\"}"
```

### Email Transcripts

Send transcripts via email:

```bash
#!/bin/bash
# transcribe-and-email.sh

AUDIO_FILE="$1"
EMAIL="$2"

macscribe "$AUDIO_FILE"
pbpaste | mail -s "Transcript: $(basename "$AUDIO_FILE")" "$EMAIL"

echo "Transcript emailed to $EMAIL"
```

## Next Steps

- Review [Basic Usage](basic-usage.md) for fundamentals
- Explore [Advanced Options](advanced-options.md) for customization
- Check the [API Reference](../api-reference.md) for technical details
