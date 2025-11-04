"""Module for saving transcripts to text files."""

import os
from pathlib import Path


def save_transcript_to_file(
    transcript: str, output_path: str, audio_filename: str
) -> str:
    """
    Save transcript to a text file.

    Args:
        transcript: The transcript text to save
        output_path: User-specified output path (file or directory)
        audio_filename: Name of the audio file (used for auto-naming)

    Returns:
        The full path where the transcript was saved
    """
    output = Path(output_path)

    # Determine the final file path
    if output.is_dir() or output_path.endswith("/"):
        # If it's a directory, use audio filename with .txt extension
        base_name = Path(audio_filename).stem
        final_path = output / f"{base_name}.txt"
    else:
        # If it's a file path, use it directly
        final_path = output

    # Create parent directories if they don't exist
    final_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the transcript to the file
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    return str(final_path.resolve())
