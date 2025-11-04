# Contributing

Thank you for considering contributing to Macscribe! This guide will help you get started.

## Getting Started

### Prerequisites

- Python 3.12 or later
- macOS with Apple Silicon (M1, M2, M3, etc.)
- Git
- Basic knowledge of Python and command-line tools

### Setting Up Development Environment

1. **Fork and clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/macscribe.git
cd macscribe
```

2. **Install dependencies:**

Using pip:

```bash
pip install -e ".[test,docs]"
```

Using uv (recommended):

```bash
uv sync
```

3. **Verify installation:**

```bash
macscribe --help
```

## Development Workflow

### Making Changes

1. **Create a new branch:**

```bash
git checkout -b feature/your-feature-name
```

or

```bash
git checkout -b fix/your-bug-fix
```

2. **Make your changes:**

Edit the relevant files in `src/macscribe/`

3. **Test your changes:**

```bash
# Run tests
pytest

# Test CLI manually
macscribe test-file.mp3
```

4. **Commit your changes:**

```bash
git add .
git commit -m "Add: description of your changes"
```

### Commit Message Guidelines

Follow these conventions:

- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for improvements to existing features
- `Docs:` for documentation changes
- `Test:` for test-related changes
- `Refactor:` for code refactoring

Examples:

```bash
git commit -m "Add: support for Spotify podcast URLs"
git commit -m "Fix: handle corrupted audio files gracefully"
git commit -m "Update: improve transcription accuracy"
git commit -m "Docs: add batch processing examples"
```

## Code Style

### Python Style Guide

Macscribe follows PEP 8 style guidelines:

- Use 4 spaces for indentation
- Maximum line length of 88 characters (Black formatter)
- Use descriptive variable names
- Add docstrings to functions and classes

Example:

```python
def validate_input(input_source: str) -> bool:
    """
    Validate whether the input is a supported URL or existing local file.

    Args:
        input_source: URL or file path to validate

    Returns:
        True if valid, False otherwise
    """
    # Implementation
    pass
```

### Type Hints

Use type hints for function parameters and return values:

```python
from typing import Optional

def process_audio(
    audio_file: str,
    model: str,
    output_format: Optional[str] = None
) -> dict:
    """Process audio file with specified model."""
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=macscribe

# Run specific test file
pytest tests/test_downloader.py

# Run specific test
pytest tests/test_downloader.py::test_validate_input
```

### Writing Tests

Create tests in the `tests/` directory:

```python
# tests/test_downloader.py

from macscribe.downloader import validate_input

def test_validate_youtube_url():
    """Test validation of YouTube URLs."""
    assert validate_input("https://youtube.com/watch?v=abc123")
    assert validate_input("https://youtu.be/abc123")

def test_validate_invalid_url():
    """Test validation rejects invalid URLs."""
    assert not validate_input("https://invalid-site.com")

def test_validate_local_file(tmp_path):
    """Test validation of local files."""
    # Create temporary file
    test_file = tmp_path / "test.mp3"
    test_file.write_text("test")

    assert validate_input(str(test_file))
```

## Project Structure

```
macscribe/
├── src/
│   └── macscribe/
│       ├── __init__.py
│       ├── cli.py           # CLI interface
│       ├── clipboard.py     # Clipboard operations
│       ├── downloader.py    # URL and file handling
│       └── transcriber.py   # Transcription logic
├── tests/                   # Test files
├── docs/                    # Documentation
├── pyproject.toml          # Project configuration
└── README.md
```

## Adding New Features

### Example: Adding Support for a New Platform

1. **Update `validate_input` in `downloader.py`:**

```python
def validate_input(input_source: str) -> bool:
    # Existing code...

    # Add new platform
    if "newplatform.com" in input_source.lower():
        return True

    # Existing code...
```

2. **Add tests:**

```python
def test_validate_newplatform_url():
    """Test validation of NewPlatform URLs."""
    assert validate_input("https://newplatform.com/video/123")
```

3. **Update documentation:**

Edit relevant docs files to mention the new platform.

4. **Submit a pull request:**

See "Submitting Pull Requests" section below.

## Documentation

### Building Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build static site
mkdocs build
```

Documentation is available at `http://127.0.0.1:8000/` when serving locally.

### Writing Documentation

- Use clear, concise language
- Include code examples
- Add links to related sections
- Use proper Markdown formatting

Example:

```markdown
## Feature Name

Brief description of the feature.

### Usage

\`\`\`bash
macscribe example-command
\`\`\`

### Options

- `--option`: Description of option
```

## Submitting Pull Requests

### Before Submitting

1. **Ensure tests pass:**

```bash
pytest
```

2. **Update documentation:**

Add or update relevant documentation files.

3. **Update CHANGELOG (if exists):**

Document your changes.

4. **Rebase on main:**

```bash
git fetch origin
git rebase origin/main
```

### Creating a Pull Request

1. **Push your branch:**

```bash
git push origin feature/your-feature-name
```

2. **Open a pull request on GitHub:**

- Go to the repository on GitHub
- Click "New Pull Request"
- Select your branch
- Fill out the PR template

3. **PR Description Template:**

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing

Describe how you tested your changes.

## Checklist

- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code follows style guidelines
- [ ] Commits are properly formatted
```

### Code Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## Areas for Contribution

### High Priority

- [ ] Support for additional platforms (Spotify, SoundCloud, etc.)
- [ ] Cross-platform clipboard support (Linux, Windows)
- [ ] Output format options (SRT, VTT, JSON)
- [ ] Progress indicators for long transcriptions
- [ ] Configuration file support

### Medium Priority

- [ ] Batch processing improvements
- [ ] Audio preprocessing options
- [ ] Custom model management
- [ ] Language detection
- [ ] Translation support

### Documentation

- [ ] More usage examples
- [ ] Video tutorials
- [ ] API documentation improvements
- [ ] Troubleshooting guides

## Reporting Bugs

### Before Reporting

1. Check if the issue already exists
2. Verify you're using the latest version
3. Collect relevant information

### Bug Report Template

```markdown
## Description

Clear description of the bug.

## Steps to Reproduce

1. Step 1
2. Step 2
3. Step 3

## Expected Behavior

What you expected to happen.

## Actual Behavior

What actually happened.

## Environment

- Macscribe version:
- Python version:
- OS version:
- Chip: M1/M2/M3

## Additional Context

Any other relevant information.
```

## Feature Requests

### Suggesting Features

1. Check if the feature is already requested
2. Clearly describe the feature and its benefits
3. Provide use cases and examples

### Feature Request Template

```markdown
## Feature Description

Clear description of the proposed feature.

## Use Case

Describe why this feature would be useful.

## Proposed Implementation

If you have ideas about how to implement it.

## Alternatives

Other ways to achieve similar results.
```

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on what's best for the project

### Getting Help

- Open an issue for bugs or questions
- Join discussions in existing issues
- Check documentation first

## Recognition

Contributors will be recognized in:

- GitHub contributors list
- Release notes (for significant contributions)
- Documentation (for doc improvements)

## License

By contributing to Macscribe, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with your question
- Contact the maintainers
- Check existing documentation

Thank you for contributing to Macscribe!
