import os
import tempfile
import typer

from macscribe.downloader import validate_input, prepare_audio
from macscribe.transcriber import transcribe_audio

app = typer.Typer()

@app.command(no_args_is_help=True)
def main(
    input_source: str = typer.Argument(..., help="URL of a YouTube/Apple Podcast/X video, or path to local audio/video file"),
    model: str = typer.Option(
        "mlx-community/whisper-large-v3-mlx",
        help="Hugging Face model to use for transcription. Defaults to the large model."
    )
):
    if not validate_input(input_source):
        typer.echo("Invalid input. Please provide a valid URL (YouTube, Apple Podcast, X) or path to a local audio/video file.")
        raise typer.Exit(code=1)

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            if os.path.isfile(input_source):
                typer.echo("Preparing local file for transcription...")
            else:
                typer.echo("Downloading audio...")
            audio_file = prepare_audio(input_source, tmpdir)
        except Exception as e:
            typer.echo(f"Error preparing audio: {e}")
            raise typer.Exit(code=1)

        try:
            typer.echo("Transcribing audio...")
            transcribe_audio(audio_file, model)
        except Exception as e:
            typer.echo(f"Error during transcription: {e}")
            raise typer.Exit(code=1)

        typer.echo("Transcription copied to clipboard.")