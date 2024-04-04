# VoiceBridge
A translation layer for converting voice to command. This package uses various strategies for
mapping a given string to a predefined map of functions. Currently supported strategies are:
* Fuzzy string comparison
* Local LLM inference (todo)
* OpenAI model inference (todo)

## Getting Started

### Requirements
* Java 17+

### Running
* `gradle dependencies`
  * Only needed if dependencies aren't installed
* `gradle bootRun`

> Also requires that IntelliNav be running on http://localhost:7070

## API
* `GET /voice`
  * Returns the stored voice string

```
GET /voice

<<<
{
	"voice": "Cursor up"
}
```

* `POST /voice`
  * Sets the stored voice string
  * Runs the converter that translates the voice string into a command string
    * Requires IntelliNav to be running
  * Send only the string in an empty body
  * Returns the input voice string and the 

```
POST /voice

>>>
Cursor up

<<<
{
	"voice": "Cursor up",
	"command": "cursor move up"
}
```

* `GET /command`
  * Returns the stored command string
  * Will be empty until `POST /voice` is hit first

```
GET /voice

<<<
{
	"command": "cursor move up"
}
```