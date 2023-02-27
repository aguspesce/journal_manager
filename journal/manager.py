import click
from utilities import date, get_parent_dir, open_editor, PATH_JOURNAL
from project import create_project
from task import create_task


@click.group()
def journal():
    """
    Open or create a task file or a project file.
    All the file will be save it in `Documentos/journal`
    """
    # Create the journal directory
    if not PATH_JOURNAL.exists():
        PATH_JOURNAL.mkdir(parents=True)


@journal.command()
@click.option("-n", "--name", help="Project name")
@click.option(
    "-l",
    "--list_names",
    is_flag=True,
    help="List the projects names existing in the directory",
)
def project(name, list_names):
    """
    Create a new entry for a given project file or create it.

    `name` option creates a new entry in the given project. If the file doesn't exist,
    it is created.

    `list_names` flag lists the different project names existing in the directory.
    """
    # # Set today's date and the start day of current and last week
    # today, _, _ = date()
    # # Create and open a project file or task file
    # if name:
    #     project = create_project(name, today)
    #     open_editor(project)
    # if list_names:
    pass


mensage_flag = (
    "Open the task file for the current week along with the task file for last week"
)


@journal.command()
@click.option("-lw", "--last_week", is_flag=True, help=mensage_flag)
def task(last_week):
    """
    Create a new task file for the current week.

    `last_week` flag opens the task file for the current week along with
    the task file for last week.
    """
    # Set today's date and the start day of current and last week
    today, start_current_week, start_last_week = dates()
    # Create a new task
    current_week_task = create_task(today, start_current_week)
    # If the flag is used, open the current week's file and last week's file
    if last_week:
        # Set the path to the last week's task file.
        last_week_task = (
            get_parent_dir("tasks", start_last_week.year) / f"{start_last_week}.md"
        )
        if last_week_task.exists():
            open_editor(current_week_task, last_week_task)
    else:
        open_editor(current_week_task)


if __name__ == "__main__":
    journal()
