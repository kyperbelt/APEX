# VoiceBridge
Converts incoming strings into commands.

## Getting Started

### Requirements
* Java 17+

### Running
* `gradle dependencies`
  * Only needed if dependencies aren't running
* `gradle bootRun`

> Also requires that IntelliNav be running on localhost:7070

## API
* `GET /voice`
  * Returns the stored voice string
* `POST /voice`
  * Sets the stored voice string and runs the converter that turns the voice string into a command string
    * Requires IntelliNav to be running
  * Send only the string in an empty body

```
POST /voice

Move cursor up
```

* `GET /command`
  * Returns the stored command string
  * Will be empty until `POST /voice` is hit first