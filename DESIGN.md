# Design Document

## 1. Requirement Analysis

### Objective

Build a Python-based alarm clock that runs entirely through the command
line.

The application should allow users to:

-   Create alarms
-   View alarms
-   Remove alarms
-   Start an alarm scheduler
-   Receive notifications when alarms trigger

------------------------------------------------------------------------

## Explicit Constraints

-   Python
-   CLI only
-   No web UI
-   No React
-   No database

------------------------------------------------------------------------

## Assumptions

### Persistence

Alarms should survive application restarts.

A JSON file is used for storage.

### Time Format

24-hour format:

-   07:30
-   18:00

### Multiple Alarms

The application supports multiple alarms.

### Scheduler Lifecycle

The scheduler runs only while:

``` bash
python alarm.py run
```

is active.

Closing the terminal stops monitoring.

### Notification

The initial implementation supports:

-   Console output
-   Sound notification
-   Optional mobile notification

------------------------------------------------------------------------

## Out of Scope

-   GUI
-   Authentication
-   Cloud synchronization
-   Multi-user support
-   Database integration

------------------------------------------------------------------------

# 2. Architecture

``` text
CLI
 │
 ▼
Command Handlers
 │
 ├──────────────┐
 ▼              ▼
Storage      Scheduler
 │
 ▼
JSON File
```

------------------------------------------------------------------------

## Project Structure

``` text
alarm_clock/

alarm.py
alarms.json

cli/
models/
services/
utils/
tests/
```

------------------------------------------------------------------------

## Data Model

``` json
{
  "id": 1,
  "time": "07:30",
  "label": "Gym",
  "daily": true
}
```

------------------------------------------------------------------------

## Design Decisions

### Why JSON?

-   Lightweight
-   Human readable
-   No external service required
-   Complies with "no database"

### Why Separate Services?

-   Single responsibility
-   Easier testing
-   Better maintainability

### Why Separate AI Layer?

The AI component only converts natural language into structured alarm
data.

It does not directly modify storage or scheduler behavior.

------------------------------------------------------------------------

# 3. Implementation Plan

## Phase 1

-   Alarm model
-   JSON serialization

## Phase 2

-   Storage service
-   Add/List/Remove operations

## Phase 3

-   CLI interface
-   argparse integration

## Phase 4

-   Scheduler
-   Alarm triggering

## Phase 5

-   Notification integration

## Phase 6

-   AI natural language parser

Example:

``` bash
python alarm.py ai-add "Wake me up at 7:30 AM for gym"
```

AI returns:

``` json
{
  "time": "07:30",
  "label": "Gym"
}
```

which is passed into the existing application services.

------------------------------------------------------------------------

# 4. Future Enhancements

-   Snooze
-   One-time alarms
-   Background daemon
-   Desktop notifications
-   Additional AI-powered commands
