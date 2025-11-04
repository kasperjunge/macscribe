# Examples

## Basic Workflows

### Meeting Notes

```bash
macscribe meeting.m4a --output meetings/2024-01-15.txt
```

### Research Transcripts

```bash
macscribe https://youtube.com/watch?v=VIDEO_ID --output research/lecture.txt
```

### Interview Transcription

```bash
macscribe interview.mp3 --output interviews/john-doe.txt
```

## Batch Processing

Transcribe multiple files:

```bash
#!/bin/bash
for file in audio/*.mp3; do
    name=$(basename "$file" .mp3)
    macscribe "$file" --output "transcripts/${name}.txt"
done
```

## Archive Organization

```bash
#!/bin/bash
# Organize by date
DATE=$(date +%Y-%m-%d)
macscribe recording.m4a --output "archive/$DATE/transcript.txt"
```

## Integration

### Save and Search

```bash
# Transcribe and save
macscribe video.mp4 --output transcript.txt

# Search content
grep -i "keyword" transcript.txt
```

### Slack Notification

```bash
#!/bin/bash
macscribe "$1" --output transcript.txt
curl -X POST "$SLACK_WEBHOOK" \
  -H 'Content-Type: application/json' \
  -d '{"text":"Transcript ready: '"$(cat transcript.txt | head -c 500)"'..."}'
```

### Email Transcript

```bash
macscribe audio.mp3 --output transcript.txt
mail -s "Transcript" user@example.com < transcript.txt
```

## Language Learning

```bash
# Transcribe foreign language content
macscribe lesson.mp4 --output "language-study/lesson-01.txt"
```

## Content Creation

```bash
# Generate show notes
macscribe podcast-ep42.mp3 --output "show-notes/ep42-transcript.txt"

# Blog post from video
macscribe https://youtube.com/watch?v=VIDEO --output blog/post-transcript.txt
```

## Accessibility

```bash
# Create text alternative
macscribe training-video.mp4 --output "accessible/training-transcript.txt"
```

## Next Steps

- [Basic Usage](basic-usage.md)
- [Advanced Options](advanced-options.md)
