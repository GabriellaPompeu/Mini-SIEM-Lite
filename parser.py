import re
from models import LogEvent

LOG_PATTERN = re.compile(r'(\S+) - - \[(.*?)\] "(GET|POST|PUT|DELETE) (\S+) (HTTP/\d.\d)" (\d{3}) (\d+)')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)

    if not match: return None

    return LogEvent (
        ip = match.group(1),
        timestamp  = match.group(2),
        method  = match.group(3),
        endpoint  = match.group(4),
        protocol  = match.group(5),
        status = int(match.group(6)),
        size = int(match.group(7)),
    )