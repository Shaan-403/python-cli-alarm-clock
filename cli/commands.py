from models.alarm import Alarm
from services.storage_service import StorageService
from utils.validators import validate_time


storage = StorageService()

def add_alarm(time_str, label):

    if not validate_time(time_str):
        print("Invalid time format.")
        return

    alarms = storage.load_alarms()

    next_id = (
        max([a.id for a in alarms], default=0)
        + 1
    )

    alarm = Alarm(
        id=next_id,
        time=time_str,
        label=label
    )

    alarms.append(alarm)

    storage.save_alarms(alarms)

    print("Alarm added.")
    
def list_alarms():

    alarms = storage.load_alarms()

    if not alarms:
        print("No alarms found.")
        return

    for alarm in alarms:
        print(
            f"{alarm.id} | "
            f"{alarm.time} | "
            f"{alarm.label}"
        )
        
        
def remove_alarm(alarm_id):

    alarms = storage.load_alarms()

    alarms = [
        a
        for a in alarms
        if a.id != alarm_id
    ]

    storage.save_alarms(alarms)

    print("Alarm removed.")
    
    
from services.scheduler_service import SchedulerService


def run_scheduler():

    alarms = storage.load_alarms()

    scheduler = SchedulerService()

    scheduler.run(alarms)