# Installation

## Prerequisites

- Python 3.12+
- macOS with Apple Silicon (M1/M2/M3+)
- pip

## Install

```bash
pip install macscribe
```

Verify installation:

```bash
macscribe --help
```

## Install from Source

For development or the latest features:

```bash
git clone https://github.com/kasperjunge/macscribe.git
cd macscribe
pip install -e .
```

Or with `uv`:

```bash
uv sync
```

## Dependencies

Automatically installed:

- `yt-dlp` - Downloads audio from URLs
- `mlx-whisper` - MLX-accelerated transcription
- `typer` - CLI interface

## Optional: Development Tools

```bash
# Testing
pip install "macscribe[test]"

# Documentation
pip install "macscribe[docs]"
```

## Troubleshooting

**Python version issues**: Check you're using Python 3.12+

```bash
python --version
```

**Permission errors**: Install for your user only

```bash
pip install --user macscribe
```

**MLX issues**: Ensure you're on macOS with Apple Silicon. MLX doesn't work on Intel Macs.

## Next Steps

[Quick Start Guide](quick-start.md)
