import datetime
import os
import subprocess
from pathlib import Path

# Path to journal directory to save the files
PATH_JOURNAL = Path.home() / "Documentos/journal"

# Set editor variable.
# If the environment variable doesn't exist, it will use neovim as editor
if os.getenv("EDITOR") is None:
    editor = "nvim"
else:
    editor = os.getenv("EDITOR")


def dates() -> tuple:
    """
    Return a tuple with the today's date, the start date of the current week
    (Monday) and the start date of the last week (last Monday).
    """
    # Set today's date
    today = datetime.date.today()
    # Set the start date of the current week
    start_current_week = today - datetime.timedelta(days=today.weekday())
    # Set the start date of the last week
    start_last_week = start_current_week - datetime.timedelta(weeks=1)

    return today, start_current_week, start_last_week


def get_parent_dir(dirname: str, year: int) -> Path:
    """
    Return path to a new custom directory or create directory if missing.
    """
    # Create path to the year directory
    dirpath = PATH_JOURNAL / f"{year} / {dirname}"

    # Create directory
    if not dirpath.exists():
        dirpath.mkdir(parents=True)
    return dirpath


def open_editor(*fnames):
    """
    Open files with the system editor.
    If it doesn't exist, it will use neovim.
    """
    # -O opens multiple files with vertical splits
    if editor == "nvim":
        args = [editor, "-O"]
    else:
        args = [editor]
    args.extend(fnames)
    subprocess.run(args, check=True)
