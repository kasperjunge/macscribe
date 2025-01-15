import mlx_whisper
from macscribe.clipboard import copy_to_clipboard

def transcribe_audio(audio_file: str, model: str) -> str:
    """Transcribe the audio file using mlx_whisper, copy the result to clipboard, and return the transcript."""
    result = mlx_whisper.transcribe(audio_file, path_or_hf_repo=model)
    transcript = result.get("text", "")
    if not transcript:
        raise ValueError("No transcription result.")

    # Use the clipboard module to copy transcript
    copy_to_clipboard(transcript)
    return transcript