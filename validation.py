from datetime import date


def parse_date(date_text):

    parts = date_text.strip().split("-")

    if len(parts) != 3:
        raise ValueError

    year, month, day = parts

    return date(
        int(year),
        int(month),
        int(day)
    )


def validate_title(title):
    title = title.strip()

    if not title:
        return False

    if title.isdigit():
        return False

    return title


def validate_description(description):
    description = description.strip()

    if not description:
        return False

    if description.isdigit():
        return False

    return description


def validate_priority(priority):
    priority = priority.strip()

    if not priority:
        return False

    try:
        priority = int(priority)
        if priority < 0:
            return False
        return priority

    except ValueError:
        return False


def validate_deadline(deadline):
    deadline = deadline.strip()

    if not deadline:
        return None

    try:
        deadline = parse_date(deadline)
    except ValueError:
        raise ValueError("Invalid date format")

    if deadline < date.today():
        raise ValueError("Deadline cannot be in the past")

    return deadline
