import os
import time
import requests

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SchedulerService:

    def send_push_notification(self, alarm):

        resp = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": os.getenv("PUSHOVER_APP_TOKEN"),
                "user": os.getenv("PUSHOVER_USER_KEY"),
                "title": "Alarm Clock",
                "message": f"{alarm.label} ({alarm.time})"
            }
        )
        print(f"Push notification sent: {resp.status_code}")
        print(f"Response: {resp.text}")

    def run(self, alarms):

        print("Monitoring alarms...")

        while True:

            current_time = datetime.now().strftime("%H:%M")

            for alarm in alarms:

                if alarm.time == current_time:

                    os.system(
                        "afplay /System/Library/Sounds/Glass.aiff"
                    )

                    self.send_push_notification(alarm)

                    print(
                        f"\n⏰ Alarm Triggered: "
                        f"{alarm.label}"
                    )

            time.sleep(60)