import os
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

from macscribe.downloader import validate_input, prepare_audio


class TestValidateInput:
    """Test the validate_input function."""
    
    def test_valid_local_audio_files(self, mock_audio_file):
        """Test validation of valid local audio files."""
        # Test various audio extensions
        audio_extensions = ['.mp3', '.wav', '.flac', '.m4a', '.ogg', '.wma']
        
        for ext in audio_extensions:
            # Create a mock file with the extension
            audio_path = mock_audio_file.replace('.mp3', ext)
            Path(audio_path).touch()
            
            assert validate_input(audio_path) is True
    
    def test_valid_local_video_files(self, mock_video_file):
        """Test validation of valid local video files."""
        # Test various video extensions
        video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.wmv']
        
        for ext in video_extensions:
            # Create a mock file with the extension
            video_path = mock_video_file.replace('.mp4', ext)
            Path(video_path).touch()
            
            assert validate_input(video_path) is True
    
    def test_invalid_local_files(self, mock_unsupported_file):
        """Test validation of invalid local files."""
        assert validate_input(mock_unsupported_file) is False
    
    def test_nonexistent_file(self):
        """Test validation of non-existent files."""
        assert validate_input("/path/to/nonexistent/file.mp3") is False
    
    def test_valid_urls(self, valid_urls):
        """Test validation of valid URLs."""
        for url in valid_urls:
            assert validate_input(url) is True
    
    def test_invalid_urls(self, invalid_urls):
        """Test validation of invalid URLs."""
        for url in invalid_urls:
            assert validate_input(url) is False
    
    def test_case_insensitive_extensions(self, temp_dir):
        """Test that file extensions are case insensitive."""
        # Test uppercase extension
        audio_path = os.path.join(temp_dir, "test_audio.MP3")
        Path(audio_path).touch()
        
        assert validate_input(audio_path) is True
    
    def test_edge_cases(self):
        """Test edge cases for validation."""
        # Empty string
        assert validate_input("") is False
        
        # None (should not crash)
        with pytest.raises(TypeError):
            validate_input(None)


class TestPrepareAudio:
    """Test the prepare_audio function."""
    
    def test_local_file_preparation(self, mock_audio_file):
        """Test that local files are returned as-is."""
        result = prepare_audio(mock_audio_file, "/tmp")
        assert result == mock_audio_file
    
    @patch('macscribe.downloader.yt_dlp.YoutubeDL')
    def test_url_download_preparation(self, mock_ydl):
        """Test that URLs are processed through yt-dlp."""
        # Mock the YoutubeDL behavior
        mock_ydl_instance = MagicMock()
        mock_ydl.return_value.__enter__.return_value = mock_ydl_instance
        mock_ydl_instance.extract_info.return_value = {'id': 'test_video_id'}
        
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        temp_path = "/tmp/test"
        
        result = prepare_audio(url, temp_path)
        
        # Should call yt-dlp
        mock_ydl_instance.extract_info.assert_called_once_with(url, download=True)
        
        # Should return the expected audio file path
        expected_path = os.path.join(temp_path, "test_video_id.mp3")
        assert result == expected_path
    
    @patch('macscribe.downloader.yt_dlp.YoutubeDL')
    def test_nonexistent_local_file(self, mock_ydl):
        """Test behavior with non-existent local file."""
        # Mock yt-dlp to handle the nonexistent file as a URL
        mock_ydl_instance = MagicMock()
        mock_ydl.return_value.__enter__.return_value = mock_ydl_instance
        mock_ydl_instance.extract_info.side_effect = Exception("Not a valid URL")
        
        nonexistent_file = "/path/to/nonexistent/file.mp3"
        
        # Should try yt-dlp and fail since it's not a valid URL
        with pytest.raises(Exception, match="Not a valid URL"):
            prepare_audio(nonexistent_file, "/tmp")
    
    @patch('macscribe.downloader.yt_dlp.YoutubeDL')
    def test_ydl_download_error(self, mock_ydl):
        """Test handling of yt-dlp download errors."""
        # Mock yt-dlp to raise an exception
        mock_ydl_instance = MagicMock()
        mock_ydl.return_value.__enter__.return_value = mock_ydl_instance
        mock_ydl_instance.extract_info.side_effect = Exception("Download failed")
        
        url = "https://www.youtube.com/watch?v=invalid"
        temp_path = "/tmp/test"
        
        # Should propagate the exception
        with pytest.raises(Exception, match="Download failed"):
            prepare_audio(url, temp_path)