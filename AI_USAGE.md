# AI Usage

## Objective

The assignment explicitly encouraged the use of AI during planning and
implementation.

The goal was to use AI as an engineering productivity tool rather than
replacing implementation ownership.

------------------------------------------------------------------------

## AI-Assisted Activities

### Requirement Refinement

AI was used to:

-   Identify ambiguous requirements
-   Define a reasonable MVP
-   Generate assumptions
-   Identify out-of-scope items

------------------------------------------------------------------------

### Architecture Exploration

AI helped evaluate:

-   JSON vs SQLite
-   CLI command structure
-   Scheduler design
-   Service separation

Final decisions were manually reviewed and adapted.

------------------------------------------------------------------------

### Implementation Assistance

AI was used for:

-   Boilerplate generation
-   argparse usage patterns
-   Dataclass modeling
-   Error handling ideas
-   OpenAI API integration examples

Generated code was reviewed, modified, and integrated manually.

------------------------------------------------------------------------

## AI Feature Added

An optional natural language interface was implemented.

Example:

``` bash
python alarm.py ai-add "Wake me up at 7:30 AM for gym"
```

Processing Flow:

``` text
Natural Language
        ↓
   AI Parser
        ↓
Structured JSON
        ↓
Existing add_alarm() Service
        ↓
alarms.json
```

The AI component does not directly manipulate persistence or scheduler
logic.

------------------------------------------------------------------------

## Engineering Principle

The AI layer is intentionally isolated from the business layer.

Responsibilities:

AI: - Natural language understanding - JSON generation

Core Application: - Validation - Persistence - Scheduling -
Notifications

This separation keeps the system deterministic while allowing future AI
enhancements.

------------------------------------------------------------------------

## Future Possibilities

Potential future extensions include:

-   AI-based alarm updates
-   AI-assisted alarm deletion
-   Conversational CLI interface
-   Multi-step reminder workflows

These were intentionally excluded from the MVP to keep the
implementation focused and maintainable.
