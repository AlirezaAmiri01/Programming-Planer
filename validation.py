
from datetime import date
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

    if not title.strip():
        return False

    if title.isdigit():
        return False

    return title


def validate_description(description):
    description = description.strip()

    if not description.strip():
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

    return True


def validate_deadline(deadline):
    deadline = deadline.strip()

    if not deadline:
        return None

    try:
        deadline = parse_date(deadline)

        if deadline < date.today():
            return False

        return deadline

    except ValueError:
        return False
