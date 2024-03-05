from dataclasses import dataclass
from datetime import datetime


@dataclass
class TwitchNode:
    numeric_id: int
    views: int
    created_at: datetime
    updated_at: datetime
    mature: int
    language: str

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%d')
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%d')
