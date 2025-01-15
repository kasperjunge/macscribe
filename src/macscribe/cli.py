import os
import tempfile
import typer

from macscribe.downloader import validate_url, download_audio
from macscribe.transcriber import transcribe_audio

app = typer.Typer()

@app.command(no_args_is_help=True)
def main(
    url: str = typer.Argument(..., help="URL of an Apple Podcast episode or YouTube video"),
    model: str = typer.Option(
        "mlx-community/whisper-large-v3-mlx",
        help="Hugging Face model to use for transcription. Defaults to the large model."
    )
):
    if not validate_url(url):
        typer.echo("Invalid URL. Only Apple Podcast and YouTube video URLs are allowed.")
        raise typer.Exit(code=1)

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            typer.echo("Downloading audio...")
            audio_file = download_audio(url, tmpdir)
        except Exception as e:
            typer.echo(f"Error downloading audio: {e}")
            raise typer.Exit(code=1)

        try:
            typer.echo("Transcribing audio...")
            transcribe_audio(audio_file, model)
        except Exception as e:
            typer.echo(f"Error during transcription: {e}")
            raise typer.Exit(code=1)

        typer.echo("Transcription copied to clipboard.")