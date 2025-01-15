import subprocess

def copy_to_clipboard(text: str) -> None:
    """Copy the given text to the system clipboard using pbcopy."""
    subprocess.run('pbcopy', input=text.encode(), check=True)