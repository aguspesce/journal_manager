import datetime
from utilities import get_parent_dir

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


def create_task(today, start_current_week):
    """
    Create a new that file for the current_week or create a new task entry if the file
    already exists.

    Parameters:
    ----------
    today: :class: `datetime.date`
        Current date.
    start_current_week: :class: `datetime.date`
       Start date of the current week (Monday).

    Return:
    ------
    file_task:
        Path to the task file.
    """
    # Create a week dictionary with the week dates
    week = {
        name: (today + datetime.timedelta(days=-today.weekday() + i)).strftime(
            "%a | %d %b"
        )
        for i, name in enumerate(["mon", "tue", "wed", "thu", "fri"])
    }
    # Set the path to the current week's task file
    file_task = get_parent_dir("tasks", today.year) / f"{start_current_week}.md"
    # Create the current week's task file if it doesn't exist
    if not file_task.exists():
        file_task.write_text(
            TASK_TEMPLATE.format(
                weekof=start_current_week.strftime("%a, %b %d"),
                **week,
            )
        )
    return file_task
