# Python CLI Alarm Clock

## Overview

This project implements a lightweight Alarm Clock as a Python Command
Line Interface (CLI) application.

The original assignment intentionally provided minimal requirements:

> Build an alarm clock as a Python CLI application. CLI only, no web UI,
> no React, no database.

Rather than immediately writing code, the first step was to refine the
requirements, establish assumptions, document design decisions, and then
implement the solution.

As an optional enhancement, the project also includes an AI-powered
natural language interface that converts free-form text into structured
alarm commands.

------------------------------------------------------------------------

## Features

-   Add alarms
-   List alarms
-   Remove alarms
-   Persistent JSON storage
-   Alarm scheduler
-   Terminal notification
-   Sound notification (platform dependent)
-   Mobile notification integration (Pushover)
-   AI-powered natural language alarm creation

------------------------------------------------------------------------

## Project Structure

``` text
alarm_clock/

├── README.md
├── DESIGN.md
├── AI_USAGE.md
│
├── alarm.py
├── alarms.json
│
├── cli/
├── models/
├── services/
├── utils/
└── tests/
```

------------------------------------------------------------------------

## Installation

``` bash
pip install -r requirements.txt
```

Example dependencies:

-   openai
-   python-dotenv
-   requests

------------------------------------------------------------------------

## Usage

### Add Alarm

``` bash
python alarm.py add 07:30 --label Gym
```

### AI Add Alarm

``` bash
python alarm.py ai-add "Wake me up at 7:30 AM for gym"
```

### List Alarms

``` bash
python alarm.py list
```

### Remove Alarm

``` bash
python alarm.py remove 1
```

### Start Scheduler

``` bash
python alarm.py run
```

------------------------------------------------------------------------

## AI Enhancement

The AI integration is intentionally limited to natural language parsing.

Example:

``` text
User Input
      ↓
AI Parser
      ↓
Structured Alarm Object
      ↓
Existing add_alarm() Service
      ↓
alarms.json
```

This keeps the core business logic deterministic while improving
usability.

------------------------------------------------------------------------

## Additional Documentation

-   DESIGN.md
-   AI_USAGE.md
