# Macscribe

Macscribe is a command-line tool for transcribing audio from YouTube videos and Apple Podcast episodes. It downloads the audio, transcribes it using a state-of-the-art ML model, and copies the transcription directly to your clipboard for easy use.

## Features

- **Multi-Platform Support:** Accepts YouTube and Apple Podcast URLs.
- **Automated Audio Processing:** Downloads high-quality audio from the provided URL.
- **State-of-the-Art Transcription:** Utilizes `mlx-whisper` for accurate and fast transcription.
- **Clipboard Integration:** Automatically copies the transcript to your clipboard.
- **Customizable Models:** Option to specify a different Hugging Face model for transcription.
- **Simple CLI Interface:** Easy-to-use command-line interface built with Typer.

## Installation

Macscribe can be installed using `pip`. Ensure you have Python 3.12 or later installed, then run:

```bash
pip install macscribe
```

This will install Macscribe along with its dependencies, including `yt-dlp`, `mlx-whisper`, and `typer`.

## Usage

Once installed, you can run Macscribe directly from the command line. The basic usage is:

```bash
macscribe <URL> [--model MODEL]
```

**Arguments:**

- `<URL>`: The URL of a YouTube video or an Apple Podcast episode.
- `--model MODEL`: *(Optional)* The Hugging Face model to use for transcription.  
  Defaults to `"mlx-community/whisper-large-v3-mlx"` if not specified.

**Examples:**

1. Transcribe a YouTube video using the default model:

   ```bash
   macscribe https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

2. Transcribe an Apple Podcast episode with a specific model:

   ```bash
   macscribe https://podcasts.apple.com/us/podcast/example-episode-url --model some/alternative-model
   ```

After transcription, the resulting text is automatically copied to your clipboard.

## Contributing

Contributions are welcome! If you'd like to contribute to Macscribe, please follow these steps:

1. **Fork the repository** on GitHub.
2. **Clone your fork** and create a new branch for your feature or bugfix.
3. Make your changes, ensuring code quality and consistency.
4. **Test** your changes thoroughly.
5. Submit a **pull request** describing your changes and why they should be merged.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README provides an introduction, key features, installation instructions, usage examples, contribution guidelines, and licensing information, offering a comprehensive guide to using and contributing to Macscribe.