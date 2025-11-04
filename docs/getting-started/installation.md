# Installation

This guide will walk you through installing Macscribe on your system.

## Prerequisites

Before installing Macscribe, ensure you have:

- **Python 3.12 or later** installed on your system
- **macOS** (required for MLX hardware acceleration on Apple Silicon)
- **pip** package manager (usually comes with Python)

## Installation Methods

### Using pip (Recommended)

The easiest way to install Macscribe is using pip:

```bash
pip install macscribe
```

This will install Macscribe along with all its dependencies, including:

- `yt-dlp` for downloading audio from URLs
- `mlx-whisper` for transcription
- `typer` for the CLI interface

### Installing from Source

If you want to install the latest development version or contribute to the project:

1. Clone the repository:

```bash
git clone https://github.com/kasperjunge/macscribe.git
cd macscribe
```

2. Install using pip in editable mode:

```bash
pip install -e .
```

Or if you're using `uv` (recommended for development):

```bash
uv sync
```

### Verifying Installation

After installation, verify that Macscribe is installed correctly by running:

```bash
macscribe --help
```

You should see the help message with available commands and options.

## Dependencies

Macscribe automatically installs the following dependencies:

- **yt-dlp** (≥2025.1.12): For downloading audio from YouTube, Apple Podcasts, and X
- **mlx-whisper** (≥0.4.1): For audio transcription using Apple's MLX framework
- **typer** (≥0.15.1): For the command-line interface

## Optional Dependencies

### For Development

If you plan to contribute to Macscribe, install the test dependencies:

```bash
pip install "macscribe[test]"
```

This includes:

- pytest
- pytest-mock

### For Documentation

To build the documentation locally:

```bash
pip install "macscribe[docs]"
```

This includes:

- mkdocs
- mkdocs-material

## Troubleshooting

### Python Version Issues

If you encounter issues with Python version compatibility:

```bash
# Check your Python version
python --version

# Or use python3 explicitly
python3 --version
```

Make sure you're using Python 3.12 or later.

### Permission Issues

If you encounter permission errors during installation, you can install for your user only:

```bash
pip install --user macscribe
```

### MLX Installation Issues

If you have issues with `mlx-whisper`, ensure you're running on macOS with Apple Silicon. MLX is optimized for Apple Silicon chips (M1, M2, M3, etc.).

## Next Steps

Once installation is complete, proceed to the [Quick Start Guide](quick-start.md) to learn how to use Macscribe.
