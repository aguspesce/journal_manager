from utilities import get_parent_dir
import os

# Template for a new project
PROJECT_TEMPLATE = """
# Note of {project_name} project
## {today}
""".strip()


def create_project(project_name, today):
    """
    Create a new project file if it doesn't exist.
    If it exists, a new entry is created on it.

    Parameters:
        project_name (str): The name of the project.
        today (datetime.date): The current date.

    Returns:
        pathlib.Path: Path to de project file.
    """
    # Set path to the project file
    file_project = get_parent_dir("projects", today.year) / f"{project_name}.md"
    # Create a new project file if it doesn't exit using the template
    if not file_project.exists():
        file_project.write_text(
            PROJECT_TEMPLATE.format(project_name=project_name, today=today)
        )
    else:
        # If the project file exist, it create a new entry on it.
        # To do that, first save the file content and then write the new lines
        # Save content of the file in a variable
        content = file_project.read_text().split(sep="\n")
        # If the current date doesn't exist, it is added to the file in a new line
        if f"## {today}" not in content:
            content = content[:2] + [f"## {today}", ""] + content[2:]
            # Write the previous content in the file
            file_project.write_text("\n".join(content))
    return file_project


def get_project_names(today):
    """
    Return a list with the name of all the project files that are in the project
    directory.

    Parameters:
        today (datetime.date): Current date.

    Returns:
        list: A list with the names of all project files.
    """
    # Set path to the project directory
    project_path = get_parent_dir("projects", today.year)
    # Return a list with the project names
    return os.listdir(project_path)
