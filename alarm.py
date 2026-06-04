import argparse
from cli.commands import (
    add_alarm,
    list_alarms,
    remove_alarm,
    run_scheduler
)


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="command"
)

ai_parser = subparsers.add_parser(
    "ai-add"
)

ai_parser.add_argument(
    "text"
)


add_parser = subparsers.add_parser("add")

add_parser.add_argument("time")

add_parser.add_argument(
    "--label",
    default="Alarm"
)

subparsers.add_parser("list")


remove_parser = subparsers.add_parser(
    "remove"
)

remove_parser.add_argument(
    "alarm_id",
    type=int
)

subparsers.add_parser("run")


args = parser.parse_args()

if args.command == "add":
    add_alarm(args.time, args.label)

elif args.command == "list":
    list_alarms()

elif args.command == "remove":
    remove_alarm(args.alarm_id)

elif args.command == "run":
    run_scheduler()

elif args.command == "ai-add":

    try:

        from services.ai_parser_service import (
            AIParserService
        )

        ai_service = AIParserService()

        alarm = ai_service.parse(
            args.text
        )

        add_alarm(
            alarm["time"],
            alarm["label"]
        )

    except Exception as e:
        print(e)
else:
    parser.print_help()