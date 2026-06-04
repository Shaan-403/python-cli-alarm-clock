import json
from pathlib import Path

from models.alarm import Alarm


class StorageService:

    FILE_NAME = "alarms.json"

    def load_alarms(self):
        file = Path(self.FILE_NAME)

        if not file.exists():
            return []

        with open(file, "r") as f:
            data = json.load(f)

        return [Alarm(**item) for item in data]

    def save_alarms(self, alarms):
        with open(self.FILE_NAME, "w") as f:
            json.dump(
                [alarm.__dict__ for alarm in alarms],
                f,
                indent=4
            )