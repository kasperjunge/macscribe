import os
import tempfile
import typer
from typing import Optional

from macscribe.downloader import validate_input, prepare_audio
from macscribe.transcriber import transcribe_audio
from macscribe.saver import save_transcript_to_file

app = typer.Typer()

@app.command(no_args_is_help=True)
def main(
    input_source: str = typer.Argument(..., help="URL of a YouTube/Apple Podcast/X video, or path to local audio/video file"),
    model: str = typer.Option(
        "mlx-community/whisper-large-v3-mlx",
        help="Hugging Face model to use for transcription. Defaults to the large model."
    ),
    output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Path to save the transcript as a text file. Can be a directory or a file path."
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
            transcript = transcribe_audio(audio_file, model)
        except Exception as e:
            typer.echo(f"Error during transcription: {e}")
            raise typer.Exit(code=1)

        typer.echo("Transcription copied to clipboard.")

        # Save transcript to file if output path is specified
        if output:
            try:
                saved_path = save_transcript_to_file(transcript, output, audio_file)
                typer.echo(f"Transcript saved to: {saved_path}")
            except Exception as e:
                typer.echo(f"Error saving transcript: {e}")
                raise typer.Exit(code=1)