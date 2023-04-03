import click
from .utilities import dates, get_parent_dir, open_editor, PATH_JOURNAL
from .project import create_project, get_project_names
from .task import create_task


@click.group()
def main() -> None:
    """
    CLI tool to create and open project and task files for journaling.
    All files are saved in the `Documentos/journal` directory.
    """
    # Create the journal directory if it doesn't exist
    if not PATH_JOURNAL.exists():
        PATH_JOURNAL.mkdir(parents=True)


@main.command()
@click.option("-n", "--name", help="Specify the name of the project to create or open.")
@click.option(
    "-l",
    "--list_names",
    is_flag=True,
    help="List the name of all projects that exist in the directory.",
)
def project(name: str, list_names: bool) -> None:
    """
    Create a new entry for a given project file or create it.

    You have 2 options to choose:
    * `--name` option requires specifying the project name.
    * `--list_names` option will display a list of project names that exist in
        the directory.
    """
    # Get current date
    today, _, _ = dates()
    # List the names of the project in the directory

    if list_names:
        list_names = get_project_names(today)
        print("Project names: \n", list_names)

    # Create and open a project file
    if name:
        project = create_project(name, today)
        open_editor(project)


@main.command()
@click.option(
    "-lw",
    "--last_week",
    is_flag=True,
    help="Open the task file for the current week along with the file for last week.",
)
def task(last_week: bool) -> None:
    """
    Create a new task file for the current week.

    If --last_week option is used, it will open the task file for the current
    week along with the file for the last week.
    """
    # Get current date and the start day of current and last week
    today, start_current_week, start_last_week = dates()

    # Create a new task for the current week
    current_week_task = create_task(today, start_current_week)

    # If the flag is used, open the current week's file and last week's file
    if last_week:
        # Set the path to the last week's task file.
        last_week_task = (
            get_parent_dir("tasks", start_last_week.year) / f"{start_last_week}.md"
        )
        if last_week_task.exists():
            open_editor(current_week_task, last_week_task)
        # If the last week's file doesn't exist, open only the file of the
        # current week
        else:
            print("Doesn't exist a task file for the last week to show")
            open_editor(current_week_task)

    # If the flag isn't used, the task file of the current week is opened
    else:
        open_editor(current_week_task)
