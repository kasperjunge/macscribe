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
    
    def test_no_args_shows_help(self):
        """Test that running with no arguments shows help."""
        result = self.runner.invoke(app, [])
        
        assert result.exit_code == 2  # Typer returns exit code 2 for missing required args
        assert "Usage:" in result.stdout


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