import os
import pytest
from unittest.mock import patch, MagicMock
from typer.testing import CliRunner
from pathlib import Path

from macscribe.cli import app


class TestCLI:
    """Test the CLI interface."""
    
    def setup_method(self):
        """Set up test runner."""
        self.runner = CliRunner()
    
    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_local_audio_file_success(self, mock_prepare, mock_transcribe, mock_audio_file):
        """Test successful transcription of local audio file."""
        # Mock the functions
        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = "Test transcription"
        
        result = self.runner.invoke(app, [mock_audio_file])
        
        assert result.exit_code == 0
        assert "Preparing local file for transcription..." in result.stdout
        assert "Transcribing audio..." in result.stdout
        assert "Transcription copied to clipboard." in result.stdout
        
        # Verify mocks were called correctly
        mock_prepare.assert_called_once()
        mock_transcribe.assert_called_once_with(mock_audio_file, "mlx-community/whisper-large-v3-mlx")
    
    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_url_download_success(self, mock_prepare, mock_transcribe):
        """Test successful transcription of URL."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        mock_audio_file = "/tmp/downloaded_audio.mp3"
        
        # Mock the functions
        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = "Test transcription"
        
        result = self.runner.invoke(app, [url])
        
        assert result.exit_code == 0
        assert "Downloading audio..." in result.stdout
        assert "Transcribing audio..." in result.stdout
        assert "Transcription copied to clipboard." in result.stdout
        
        # Verify mocks were called correctly
        mock_prepare.assert_called_once()
        mock_transcribe.assert_called_once_with(mock_audio_file, "mlx-community/whisper-large-v3-mlx")
    
    def test_invalid_input(self):
        """Test CLI with invalid input."""
        result = self.runner.invoke(app, ["invalid_input"])
        
        assert result.exit_code == 1
        assert "Invalid input" in result.stdout
    
    def test_custom_model(self, mock_audio_file):
        """Test CLI with custom model parameter."""
        with patch('macscribe.cli.transcribe_audio') as mock_transcribe, \
             patch('macscribe.cli.prepare_audio') as mock_prepare:
            
            mock_prepare.return_value = mock_audio_file
            mock_transcribe.return_value = "Test transcription"
            
            custom_model = "custom/whisper-model"
            result = self.runner.invoke(app, [mock_audio_file, "--model", custom_model])
            
            assert result.exit_code == 0
            mock_transcribe.assert_called_once_with(mock_audio_file, custom_model)
    
    @patch('macscribe.cli.prepare_audio')
    def test_prepare_audio_error(self, mock_prepare, mock_audio_file):
        """Test CLI when prepare_audio fails."""
        mock_prepare.side_effect = Exception("Download failed")
        
        result = self.runner.invoke(app, [mock_audio_file])
        
        assert result.exit_code == 1
        assert "Error preparing audio: Download failed" in result.stdout
    
    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_transcribe_error(self, mock_prepare, mock_transcribe, mock_audio_file):
        """Test CLI when transcription fails."""
        mock_prepare.return_value = mock_audio_file
        mock_transcribe.side_effect = Exception("Transcription failed")
        
        result = self.runner.invoke(app, [mock_audio_file])
        
        assert result.exit_code == 1
        assert "Error during transcription: Transcription failed" in result.stdout
    
    def test_help_message(self):
        """Test that help message is displayed correctly."""
        result = self.runner.invoke(app, ["--help"])

        assert result.exit_code == 0
        assert "YouTube/Apple Podcast/X video, or path" in result.stdout
        assert "Hugging Face model to use for" in result.stdout and "transcription" in result.stdout
        assert "--output" in result.stdout or "-o" in result.stdout
        assert "save the transcript" in result.stdout.lower()
    
    def test_no_args_shows_help(self):
        """Test that running with no arguments shows help."""
        result = self.runner.invoke(app, [])

        # no_args_is_help=True shows help, exit code may vary by platform (0 or 2)
        assert result.exit_code in [0, 2]
        assert "Usage:" in result.stdout


class TestCLIOutputFlag:
    """Test the --output flag functionality."""

    def setup_method(self):
        """Set up test runner."""
        self.runner = CliRunner()

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_to_specific_file(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test --output flag with specific file path."""
        transcript = "Test transcript content"
        output_file = os.path.join(temp_dir, "output.txt")

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [mock_audio_file, "--output", output_file])

        assert result.exit_code == 0
        assert "Transcription copied to clipboard." in result.stdout
        assert "Transcript saved to:" in result.stdout
        assert output_file in result.stdout

        # Verify file was created with correct content
        assert os.path.exists(output_file)
        with open(output_file, 'r') as f:
            content = f.read()
        assert content == transcript

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_to_directory(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test --output flag with directory path."""
        transcript = "Test transcript for directory"

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [mock_audio_file, "--output", temp_dir])

        assert result.exit_code == 0
        assert "Transcript saved to:" in result.stdout

        # Verify file was created in directory with auto-generated name
        expected_filename = Path(mock_audio_file).stem + ".txt"
        expected_path = os.path.join(temp_dir, expected_filename)
        assert os.path.exists(expected_path)
        with open(expected_path, 'r') as f:
            content = f.read()
        assert content == transcript

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_short_flag(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test -o short flag variant."""
        transcript = "Test with short flag"
        output_file = os.path.join(temp_dir, "short_flag.txt")

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [mock_audio_file, "-o", output_file])

        assert result.exit_code == 0
        assert os.path.exists(output_file)
        with open(output_file, 'r') as f:
            content = f.read()
        assert content == transcript

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_creates_nested_directories(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test that --output creates nested directories if they don't exist."""
        transcript = "Test nested directories"
        nested_output = os.path.join(temp_dir, "level1", "level2", "output.txt")

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [mock_audio_file, "--output", nested_output])

        assert result.exit_code == 0
        assert os.path.exists(nested_output)
        with open(nested_output, 'r') as f:
            content = f.read()
        assert content == transcript

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_with_custom_model(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test --output flag combined with --model flag."""
        transcript = "Test with custom model"
        output_file = os.path.join(temp_dir, "custom_model.txt")
        custom_model = "custom/whisper-model"

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [
            mock_audio_file,
            "--model", custom_model,
            "--output", output_file
        ])

        assert result.exit_code == 0
        assert os.path.exists(output_file)
        mock_transcribe.assert_called_once_with(mock_audio_file, custom_model)

    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_no_output_flag_does_not_save(self, mock_prepare, mock_transcribe, mock_audio_file, temp_dir):
        """Test that without --output flag, no file is saved."""
        transcript = "Test without output flag"

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript

        result = self.runner.invoke(app, [mock_audio_file])

        assert result.exit_code == 0
        assert "Transcription copied to clipboard." in result.stdout
        assert "Transcript saved to:" not in result.stdout

        # Verify no transcript files were created in temp_dir
        txt_files = list(Path(temp_dir).glob("*.txt"))
        assert len(txt_files) == 0

    @patch('macscribe.cli.save_transcript_to_file')
    @patch('macscribe.cli.transcribe_audio')
    @patch('macscribe.cli.prepare_audio')
    def test_output_save_error_handling(self, mock_prepare, mock_transcribe, mock_save, mock_audio_file):
        """Test error handling when saving transcript fails."""
        transcript = "Test save error"

        mock_prepare.return_value = mock_audio_file
        mock_transcribe.return_value = transcript
        mock_save.side_effect = Exception("Permission denied")

        result = self.runner.invoke(app, [mock_audio_file, "--output", "/invalid/path/file.txt"])

        assert result.exit_code == 1
        assert "Error saving transcript: Permission denied" in result.stdout


class TestCLIIntegration:
    """Integration tests for CLI with actual file operations."""

    def setup_method(self):
        """Set up test runner."""
        self.runner = CliRunner()

    def test_nonexistent_local_file(self):
        """Test CLI behavior with non-existent local file."""
        nonexistent_file = "/path/to/nonexistent/file.mp3"

        result = self.runner.invoke(app, [nonexistent_file])

        assert result.exit_code == 1
        assert "Invalid input" in result.stdout

    def test_unsupported_file_extension(self, mock_unsupported_file):
        """Test CLI behavior with unsupported file extension."""
        result = self.runner.invoke(app, [mock_unsupported_file])

        assert result.exit_code == 1
        assert "Invalid input" in result.stdout