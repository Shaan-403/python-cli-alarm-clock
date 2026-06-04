import os
import time
import requests
from services.notification_service import NotificationService
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SchedulerService:

    def run(self, alarms):
        notification_service = (NotificationService())
        print("Monitoring alarms...")

        while True:

            current_time = datetime.now().strftime("%H:%M")

            for alarm in alarms:

                if alarm.time == current_time:

                    os.system(
                        "afplay /System/Library/Sounds/Glass.aiff"
                    )

                    notification_service.send_push_notification(
                        alarm
                    )

                    print(
                        f"\n⏰ Alarm Triggered: "
                        f"{alarm.label}"
                    )

            time.sleep(60)