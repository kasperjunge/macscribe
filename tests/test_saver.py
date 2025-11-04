import os
import pytest
from pathlib import Path

from macscribe.saver import save_transcript_to_file


class TestSaveTranscriptToFile:
    """Test the save_transcript_to_file function."""

    def test_save_to_specific_file(self, temp_dir):
        """Test saving transcript to a specific file path."""
        transcript = "This is a test transcript."
        output_file = os.path.join(temp_dir, "transcript.txt")
        audio_filename = "test_audio.mp3"

        saved_path = save_transcript_to_file(transcript, output_file, audio_filename)

        # Verify file was created
        assert os.path.exists(saved_path)
        assert saved_path == str(Path(output_file).resolve())

        # Verify content
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript

    def test_save_to_directory_with_auto_naming(self, temp_dir):
        """Test saving transcript to a directory with auto-generated filename."""
        transcript = "This is another test transcript."
        audio_filename = "my_video_abc123.mp3"

        saved_path = save_transcript_to_file(transcript, temp_dir, audio_filename)

        # Verify filename matches audio file (with .txt extension)
        assert saved_path.endswith("my_video_abc123.txt")
        assert os.path.exists(saved_path)

        # Verify content
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript

    def test_save_to_directory_with_trailing_slash(self, temp_dir):
        """Test saving to directory path with trailing slash."""
        transcript = "Test with trailing slash."
        output_dir = temp_dir + "/"
        audio_filename = "audio_file.mp3"

        saved_path = save_transcript_to_file(transcript, output_dir, audio_filename)

        # Verify it treats it as a directory
        assert saved_path.endswith("audio_file.txt")
        assert os.path.exists(saved_path)

        # Verify content
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript

    def test_create_nested_directories(self, temp_dir):
        """Test that parent directories are created if they don't exist."""
        transcript = "Test nested directories."
        nested_path = os.path.join(temp_dir, "level1", "level2", "level3", "transcript.txt")
        audio_filename = "audio.mp3"

        saved_path = save_transcript_to_file(transcript, nested_path, audio_filename)

        # Verify file was created in nested path
        assert os.path.exists(saved_path)
        assert saved_path == str(Path(nested_path).resolve())

        # Verify content
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript

    def test_handles_audio_with_multiple_extensions(self, temp_dir):
        """Test handling audio filenames with multiple dots."""
        transcript = "Test multiple dots."
        audio_filename = "my.video.file.mp4"

        saved_path = save_transcript_to_file(transcript, temp_dir, audio_filename)

        # Should use the stem (everything before the last extension)
        assert saved_path.endswith("my.video.file.txt")
        assert os.path.exists(saved_path)

    def test_overwrite_existing_file(self, temp_dir):
        """Test that existing file is overwritten."""
        transcript1 = "First transcript."
        transcript2 = "Second transcript."
        output_file = os.path.join(temp_dir, "transcript.txt")
        audio_filename = "audio.mp3"

        # Save first transcript
        saved_path1 = save_transcript_to_file(transcript1, output_file, audio_filename)

        # Verify first content
        with open(saved_path1, "r", encoding="utf-8") as f:
            content1 = f.read()
        assert content1 == transcript1

        # Save second transcript to same path
        saved_path2 = save_transcript_to_file(transcript2, output_file, audio_filename)

        # Verify it's the same path
        assert saved_path1 == saved_path2

        # Verify content was overwritten
        with open(saved_path2, "r", encoding="utf-8") as f:
            content2 = f.read()
        assert content2 == transcript2

    def test_handles_unicode_content(self, temp_dir):
        """Test saving transcript with unicode characters."""
        transcript = "Test with unicode: 你好世界 🎉 émojis and accénts"
        output_file = os.path.join(temp_dir, "unicode_transcript.txt")
        audio_filename = "audio.mp3"

        saved_path = save_transcript_to_file(transcript, output_file, audio_filename)

        # Verify file exists and content is correct
        assert os.path.exists(saved_path)
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript

    def test_handles_empty_transcript(self, temp_dir):
        """Test saving empty transcript."""
        transcript = ""
        output_file = os.path.join(temp_dir, "empty.txt")
        audio_filename = "audio.mp3"

        saved_path = save_transcript_to_file(transcript, output_file, audio_filename)

        # Verify file exists and is empty
        assert os.path.exists(saved_path)
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == ""

    def test_handles_long_transcript(self, temp_dir):
        """Test saving very long transcript."""
        # Create a long transcript (10000 words)
        transcript = " ".join(["word"] * 10000)
        output_file = os.path.join(temp_dir, "long.txt")
        audio_filename = "audio.mp3"

        saved_path = save_transcript_to_file(transcript, output_file, audio_filename)

        # Verify file exists and content matches
        assert os.path.exists(saved_path)
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == transcript
        assert len(content.split()) == 10000

    def test_returns_absolute_path(self, temp_dir):
        """Test that function returns absolute path."""
        transcript = "Test absolute path."
        output_file = os.path.join(temp_dir, "transcript.txt")
        audio_filename = "audio.mp3"

        saved_path = save_transcript_to_file(transcript, output_file, audio_filename)

        # Verify path is absolute
        assert os.path.isabs(saved_path)
        assert Path(saved_path).is_absolute()
