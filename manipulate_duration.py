import re


def parse_duration(duration):
    match = re.match("PT(\d+H)?(\d+M)?(\d+S)?", duration)
    if match:
        hours = int(match.group(1)[:-1]) if match.group(1) else 0
        minutes = int(match.group(2)[:-1]) if match.group(2) else 0
        seconds = int(match.group(3)[:-1]) if match.group(3) else 0
        return hours * 3600 + minutes * 60 + seconds
    else:
        return 0


def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    formatted_duration = ""
    if hours > 0:
        formatted_duration += f"{hours} hours, "
    if minutes > 0:
        formatted_duration += f"{minutes} minutes, "
    if seconds > 0:
        formatted_duration += f" {seconds} seconds "

    return formatted_duration if formatted_duration != "" else "0 seconds"
