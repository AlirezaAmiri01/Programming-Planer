
from datetime import date


def validate_title(title):
    title = title.strip()

    if not title.strip():
        return False

    if title.isdigit():
        return False

    return True


def validate_description(description):
    description = description.strip()

    if not description.strip():
        return False

    if description.isdigit():
        return False

    return True


def validate_priority(priority):
    priority = priority.strip()

    if not priority:
        return False

    try:
        priority = int(priority)
        if priority < 0:
            return False
        return True

    except ValueError:
        return False

    return True


def validate_deadline(deadline):
    deadline = deadline.strip()

    if not deadline:
        return False

    try:
        deadline = date.fromisoformat(deadline)
        if deadline < date.today():
            return False

    except ValueError:
        return False

    return True
