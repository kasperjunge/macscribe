import os
import sys
import tempfile
import pytest
from pathlib import Path

from pathlib import Path as _Path

# Ensure local src/ is imported before any installed package
_ROOT = _Path(__file__).resolve().parents[1]
_SRC = _ROOT / "src"
if _SRC.exists():
    sys.path.insert(0, str(_SRC))


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def mock_audio_file(temp_dir):
    """Create a mock audio file for testing."""
    audio_path = os.path.join(temp_dir, "test_audio.mp3")
    Path(audio_path).touch()
    return audio_path


@pytest.fixture
def mock_video_file(temp_dir):
    """Create a mock video file for testing."""
    video_path = os.path.join(temp_dir, "test_video.mp4")
    Path(video_path).touch()
    return video_path


@pytest.fixture
def mock_unsupported_file(temp_dir):
    """Create a mock file with unsupported extension."""
    unsupported_path = os.path.join(temp_dir, "test_file.txt")
    Path(unsupported_path).touch()
    return unsupported_path


@pytest.fixture
def valid_urls():
    """Return a list of valid URLs for testing."""
    return [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://podcasts.apple.com/us/podcast/test/id123456789",
        "https://x.com/user/status/123456789",
    ]


@pytest.fixture
def invalid_urls():
    """Return a list of invalid URLs for testing."""
    return [
        "https://www.example.com/video.mp4",
        "https://vimeo.com/123456789",
        "not-a-url",
        "",
    ]