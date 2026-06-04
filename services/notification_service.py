import os
import requests

from dotenv import load_dotenv

load_dotenv()


class NotificationService:

    def send_push_notification(
        self,
        alarm
    ):

        app_token = os.getenv(
            "PUSHOVER_APP_TOKEN"
        )

        user_key = os.getenv(
            "PUSHOVER_USER_KEY"
        )

        if not app_token or not user_key:
            print(
                "Pushover not configured. "
                "Skipping mobile notification."
            )
            return

        try:

            response = requests.post(
                "https://api.pushover.net/1/messages.json",
                data={
                    "token": app_token,
                    "user": user_key,
                    "title": "Alarm Clock",
                    "message":
                        f"{alarm.label} "
                        f"({alarm.time})"
                }
            )
        except Exception as e:

            print(
                f"Notification failed: "
                f"{e}"
            )