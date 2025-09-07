import pytest
from unittest.mock import patch, MagicMock

from macscribe.transcriber import transcribe_audio


class TestTranscriber:
    """Test the transcriber module."""
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_successful_transcription(self, mock_transcribe, mock_clipboard):
        """Test successful audio transcription."""
        # Mock the transcription result
        mock_result = {"text": "This is a test transcription."}
        mock_transcribe.return_value = mock_result
        
        audio_file = "/path/to/audio.mp3"
        model = "test-model"
        
        result = transcribe_audio(audio_file, model)
        
        # Verify the function calls
        mock_transcribe.assert_called_once_with(audio_file, path_or_hf_repo=model)
        mock_clipboard.assert_called_once_with("This is a test transcription.")
        
        # Verify return value
        assert result == "This is a test transcription."
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_empty_transcription(self, mock_transcribe, mock_clipboard):
        """Test handling of empty transcription result."""
        # Mock empty transcription result
        mock_result = {"text": ""}
        mock_transcribe.return_value = mock_result
        
        audio_file = "/path/to/audio.mp3"
        model = "test-model"
        
        # Should raise ValueError for empty transcript
        with pytest.raises(ValueError, match="No transcription result"):
            transcribe_audio(audio_file, model)
        
        # Verify transcription was called but clipboard was not
        mock_transcribe.assert_called_once_with(audio_file, path_or_hf_repo=model)
        mock_clipboard.assert_not_called()
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_missing_text_key(self, mock_transcribe, mock_clipboard):
        """Test handling when transcription result lacks 'text' key."""
        # Mock result without 'text' key
        mock_result = {"duration": 120.0}
        mock_transcribe.return_value = mock_result
        
        audio_file = "/path/to/audio.mp3"
        model = "test-model"
        
        # Should raise ValueError for missing text
        with pytest.raises(ValueError, match="No transcription result"):
            transcribe_audio(audio_file, model)
        
        # Verify transcription was called but clipboard was not
        mock_transcribe.assert_called_once_with(audio_file, path_or_hf_repo=model)
        mock_clipboard.assert_not_called()
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_mlx_whisper_exception(self, mock_transcribe, mock_clipboard):
        """Test handling of mlx_whisper exceptions."""
        # Mock transcription to raise an exception
        mock_transcribe.side_effect = Exception("Model loading failed")
        
        audio_file = "/path/to/audio.mp3"
        model = "invalid-model"
        
        # Should propagate the exception
        with pytest.raises(Exception, match="Model loading failed"):
            transcribe_audio(audio_file, model)
        
        # Verify clipboard was not called
        mock_clipboard.assert_not_called()
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_clipboard_exception(self, mock_transcribe, mock_clipboard):
        """Test handling of clipboard exceptions."""
        # Mock successful transcription but failing clipboard
        mock_result = {"text": "This is a test transcription."}
        mock_transcribe.return_value = mock_result
        mock_clipboard.side_effect = Exception("Clipboard access failed")
        
        audio_file = "/path/to/audio.mp3"
        model = "test-model"
        
        # Should propagate the clipboard exception
        with pytest.raises(Exception, match="Clipboard access failed"):
            transcribe_audio(audio_file, model)
        
        # Verify transcription was successful
        mock_transcribe.assert_called_once_with(audio_file, path_or_hf_repo=model)
    
    @patch('macscribe.transcriber.copy_to_clipboard')
    @patch('macscribe.transcriber.mlx_whisper.transcribe')
    def test_whitespace_only_transcription(self, mock_transcribe, mock_clipboard):
        """Test handling of whitespace-only transcription."""
        # Mock transcription with only whitespace
        mock_result = {"text": "   \n\t  "}
        mock_transcribe.return_value = mock_result
        
        audio_file = "/path/to/audio.mp3"
        model = "test-model"
        
        result = transcribe_audio(audio_file, model)
        
        # Should treat whitespace as valid content (not empty)
        mock_clipboard.assert_called_once_with("   \n\t  ")
        assert result == "   \n\t  "