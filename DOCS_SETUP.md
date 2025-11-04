# Documentation Setup Guide

This document explains the MkDocs documentation setup for Macscribe.

## Overview

The Macscribe documentation is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. It's automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Documentation Structure

```
docs/
├── index.md                      # Home page
├── getting-started/
│   ├── installation.md          # Installation guide
│   └── quick-start.md           # Quick start guide
├── usage/
│   ├── basic-usage.md           # Basic usage guide
│   ├── advanced-options.md      # Advanced features
│   └── examples.md              # Real-world examples
├── api-reference.md             # API documentation
├── contributing.md              # Contributing guide
└── license.md                   # License information
```

## Local Development

### Prerequisites

Install MkDocs and Material theme:

```bash
pip install mkdocs mkdocs-material
```

Or install with the docs extra:

```bash
pip install ".[docs]"
```

### Building the Documentation

Build the static site:

```bash
mkdocs build
```

This creates a `site/` directory with the generated HTML files.

### Serving Locally

Start a local development server with live reload:

```bash
mkdocs serve
```

Then visit http://127.0.0.1:8000/ in your browser.

### Cleaning Build Files

```bash
# The site/ directory is in .gitignore and will be ignored by git
rm -rf site/
```

## Configuration

The documentation is configured in `mkdocs.yml`:

- **Theme**: Material for MkDocs with custom colors
- **Features**: Navigation tabs, search, code highlighting
- **Extensions**: Syntax highlighting, admonitions, emoji support

## GitHub Pages Deployment

### Automatic Deployment

The documentation is automatically deployed using GitHub Actions:

1. When you push to the `main` branch
2. GitHub Actions runs the workflow in `.github/workflows/docs.yml`
3. It builds the documentation using `mkdocs build`
4. Deploys to the `gh-pages` branch
5. GitHub Pages serves the site

### Manual Deployment

You can also deploy manually:

```bash
mkdocs gh-deploy
```

This builds the documentation and pushes it to the `gh-pages` branch.

### Enabling GitHub Pages

To enable GitHub Pages for your repository:

1. Go to your repository on GitHub
2. Navigate to **Settings** > **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Select the **gh-pages** branch
5. Click **Save**

The site will be available at: `https://<username>.github.io/<repository>/`

For Macscribe: **https://kasperjunge.github.io/macscribe/**

## Writing Documentation

### Markdown Format

Documentation is written in Markdown with additional features from Python-Markdown extensions:

- **Code blocks with syntax highlighting**
- **Admonitions** (notes, warnings, tips)
- **Tables**
- **Emoji** :rocket:
- **Task lists**

### Adding a New Page

1. Create a new `.md` file in the appropriate `docs/` subdirectory
2. Add the page to the `nav` section in `mkdocs.yml`:

```yaml
nav:
  - New Section:
    - Page Title: path/to/file.md
```

### Code Examples

Use fenced code blocks with language specification:

````markdown
```bash
macscribe audio.mp3
```

```python
from macscribe import transcribe_audio
```
````

### Admonitions

Create callout boxes:

```markdown
!!! note
    This is a note.

!!! warning
    This is a warning.

!!! tip
    This is a tip.
```

### Internal Links

Link to other documentation pages:

```markdown
See the [Installation Guide](getting-started/installation.md) for details.
```

## Customization

### Theme Colors

Edit `mkdocs.yml` to change colors:

```yaml
theme:
  palette:
    primary: indigo  # Change this
    accent: indigo   # And this
```

### Adding Features

Enable additional Material features in `mkdocs.yml`:

```yaml
theme:
  features:
    - navigation.instant
    - navigation.tracking
    - toc.integrate
```

See [Material for MkDocs Features](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/) for options.

### Custom CSS

To add custom styles:

1. Create `docs/stylesheets/extra.css`
2. Add to `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```

## Maintenance

### Updating Documentation

When updating docs:

1. Edit the relevant `.md` files in `docs/`
2. Test locally with `mkdocs serve`
3. Commit and push to main
4. GitHub Actions will automatically deploy

### Checking for Broken Links

```bash
# Use mkdocs strict mode
mkdocs build --strict
```

This will fail the build if there are any warnings (like broken links).

### Updating Dependencies

Update MkDocs and Material theme:

```bash
pip install --upgrade mkdocs mkdocs-material
```

## Troubleshooting

### Build Fails

If the build fails:

1. Check `mkdocs.yml` for syntax errors
2. Ensure all files referenced in `nav` exist
3. Check for broken internal links
4. Run `mkdocs build --strict` locally

### GitHub Actions Fails

If deployment fails:

1. Check the Actions tab on GitHub
2. Review the workflow logs
3. Ensure the `gh-pages` branch exists
4. Verify GitHub Pages is enabled in repository settings

### Pages Not Updating

If changes don't appear:

1. Wait a few minutes (GitHub Pages can take time to update)
2. Clear your browser cache
3. Check that the workflow ran successfully
4. Verify you pushed to the main branch

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Python-Markdown Extensions](https://python-markdown.github.io/extensions/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## Contributing to Documentation

See [Contributing Guide](docs/contributing.md) for information on contributing to the documentation.

## License

The documentation is part of the Macscribe project and is licensed under the MIT License.
