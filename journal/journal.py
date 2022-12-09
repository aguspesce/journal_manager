#!/usr/bin/env python
"""
Script to manage my low-friction task management system
"""
import datetime
import subprocess
import click
from pathlib import Path
import os

# Path to journal directory to save the files
PATH_JOURNAL = Path.home() / "Documentos/journal"

# Set editor variable
# If the environment variable doesn't exist, it will use nvim as editor
if os.getenv("EDITOR") is None:
    editor = "nvim"
else:
    editor = os.getenv("EDITOR")


# Template for a new project
PROJECT_TEMPLATE = """
# Note of {project_name} project

## {today}
""".strip()

# Template for a new task
TASK_TEMPLATE = """
# Week of {weekof}

## Reminders

### {mon}

### {tue}

### {wed}

### {tue}

### {fri}

---

## For the next week

---

## Notes

---

**Instructions:**
- (x) Past event
- ( ) Upcoming event
- [ ] Incomplete task
- [x] Completed task
""".strip()


@click.command()
@click.option("-p", "--project_name", help="Project name")
def manager(project_name):
    """
    Function to create a task or a project files.

    All the file will be save it in `Docuentos/journal`.

    If `-p` option is used, the project name must be given.
    """
    # Set today's date
    today = datetime.date.today()
    # Set the start date of the week
    start_week = today - datetime.timedelta(days=today.weekday())
    # Create the journal directory
    if not PATH_JOURNAL.exists():
        PATH_JOURNAL.mkdir(parents=True)
    # Create and open a project file or task file
    if project_name:
        project = _create_project(project_name, today)
        _open_editor(project)
    else:
        # Create a new task
        task = _create_task(today, start_week)
        # Set the start date of the last week
        start_last_week = start_week - datetime.timedelta(weeks=1)
        # If today is the first day of the week,
        # Open the last task file and the new one if today is Monday
        if today == start_week:
            # Set the path to the last week's task file
            path_last_task = _get_parent_dir("tasks")
            last_task = path_last_task / f"{start_last_week}.md"
            if last_task.exists():
                _open_editor(task, last_task)
        else:
            _open_editor(task)


def _get_parent_dir(dirname):
    """
    Return path to a new custom directory or create directory if missing
    """
    # Set the year
    year = datetime.date.today().year
    # Create path to the year directory
    dirpath = PATH_JOURNAL / f"{year}" / dirname
    # Create directory
    if not dirpath.exists():
        dirpath.mkdir(parents=True)
    return dirpath


def _create_project(project_name, today):
    """
    Create a new project entry
    """
    # Set project path
    path_projects = _get_parent_dir("projects")
    # Create project file
    file_project = path_projects / f"{project_name}.md"
    # Create a new entry in the project file
    if not file_project.exists():
        file_project.write_text(
            PROJECT_TEMPLATE.format(project_name=project_name, today=today)
        )
    else:
        # If the project file exist, first save the file content and then write
        # the new lines
        content = file_project.read_text().split(sep="\n")
        # If today's date doesn't exist, it is added to the file
        if f"## {today}" not in content:
            content = content[:2] + [f"## {today}", ""] + content[2:]
            file_project.write_text("\n".join(content))
    return file_project


def _create_task(today, start_week):
    """
    Create a new task entry
    """
    # Create a week dictionary with the week dates
    week = {
        name: (today + datetime.timedelta(days=-today.weekday() + i)).strftime(
            "%a | %d %b"
        )
        for i, name in enumerate(["mon", "tue", "wed", "thu", "fri"])
    }
    # Set task path
    path_task = _get_parent_dir("tasks")
    # Create task file for the week
    file_task = path_task / f"{start_week}.md"
    # Create a new entry in the task file if it doesn't exist
    if not file_task.exists():
        file_task.write_text(
            TASK_TEMPLATE.format(
                weekof=start_week.strftime("%a, %b %d"),
                **week,
            )
        )
    return file_task


def _open_editor(*fnames):
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


if __name__ == "__main__":

    manager()
