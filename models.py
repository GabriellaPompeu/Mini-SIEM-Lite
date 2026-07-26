from dataclasses import dataclass

@dataclass
class LogEvent:
    ip : str
    timestamp : str
    method : str
    endpoint : str
    protocol : str
    status : int
    size : int
