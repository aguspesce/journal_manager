#!/usr/bin/env python
"""
Script to manage my low-friction task management system
"""
import datetime
import subprocess
import click
from pathlib import Path

# Path to journal directory
PATH_JOURNAL = Path.home() / "Documentos/journal"

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
    Function to create task and project files.

    If `-p` option is used, the project name must be given.

    """
    # For project
    if project_name:
        project = _create_project(project_name)
        _open_nvim(project)
    else:
        task = _create_task()
        _open_nvim(task)


def _get_parent_dir(dirname):
    """
    Return path to a new custom directory or create directory if missing
    """
    # Define the year
    year = datetime.date.today().year
    # Create path to the year directory
    dirpath = PATH_JOURNAL / f"{year}" / dirname

    if not dirpath.exists():
        dirpath.mkdir(parents=True)
    return dirpath


def _create_project(project_name):
    """
    Create a new project entry
    """
    # Define project path
    path_projects = _get_parent_dir("projects")
    # Create project file
    file_project = path_projects / f"{project_name}.md"
    # Set today's date
    today = datetime.date.today()

    # Create a new entry in the project file
    if not file_project.exists():
        file_project.write_text(
            PROJECT_TEMPLATE.format(project_name=project_name, today=today)
        )
    else:
        # If the project file exist, first save the file content
        content = file_project.read_text().split(sep="\n")
        # If today's date doesn't exist, it is added to the file
        if f"## {today}" not in content:
            content = content[:2] + [f"## {today}", ""] + content[2:]
            file_project.write_text("\n".join(content))

    return file_project


def _create_task():
    """
    Create new task entry
    """
    # Set today's date
    today = datetime.date.today()
    # Set the start date of the week
    start_week = today - datetime.timedelta(days=today.weekday())
    # Create a week dictionary with the week dates
    week = {
        name: (today + datetime.timedelta(days=-today.weekday() + i)).strftime(
            "%a | %d %b"
        )
        for i, name in enumerate(["mon", "tue", "wed", "thu", "fri"])
    }
    # Define task path
    path_task = _get_parent_dir("tasks")
    # Create the task file for the  week
    file_task = path_task / f"{start_week}.md"
    # Create a new entry in the task file
    if not file_task.exists():
        file_task.write_text(
            TASK_TEMPLATE.format(
                weekof=start_week.strftime("%a, %b %d"),
                **week,
            )
        )
    return file_task


def _open_nvim(*fnames):
    """
    Open the files with neovim.
    """
    # -O opens multiple files with vertical splits
    args = ["nvim", "-O"]
    args.extend(fnames)
    subprocess.run(args, check=True)


if __name__ == "__main__":
    # Create the journal directory
    if not PATH_JOURNAL.exists():
        PATH_JOURNAL.mkdir(parents=True)
    # Run the function to manage the task and projects files
    manager()
