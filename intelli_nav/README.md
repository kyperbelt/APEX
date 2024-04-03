# IntelliNav API

## Getting Started
### Requirements
- Java 17 - thats it.

### Launching
Navigate to the **intelli_nav** directory inside the **APEX** repository folder and then launch the following command:

* Windows CMD/Powershell

```bash
    gradlew.bat run
```

* Linux or MAC 

```bash
    ./gradlew run
```
That will launch the server on `localhost:7070`. Checkout the [Api](#api) section for endpoints.



## FAQ

- Why is it not doing anything when I launch in wsl.
    - It does not work from wsl unless you launch it as a windows application. You have to run it from windows cmd or powershell and not wsl shell.
- How do I make something like mouse movement instant?
    - Set the easing function to `NONE` in the payload or the `speed` property to some insanely high value. Honestly the first option is better.

## API

### Mouse

#### Movement
* **description**: Moves the mouse to the specified location on the given display
* **method**: **`POST`** `v1/inav/move`
* **payload**: 
    ```json
        {
            "function": "LINEAR", // easing function
            "speed": 100,       // speed of mouse in pixels if function is other than NONE
            "x": 300,           // x position to move to on the given display
            "y": 200,           // y position to move to on the given display
            "display" : 0       // display to move to <if multiple displays present>
        }  
    ```

#### Click
* **description**: Moves the mouse to the specified location and clicks the given button.
* **method**: **`POST`** `v1/inav/click`
* **payload**:
```json
    {
        "button": "LEFT",   // button on the mouse
        "function": "LINEAR", // easing function
        "speed": 1000,      // speed of mouse in pixels if function is other than NONE
        "x": 200,           // x position to move to on the given display
        "y": 300,           // y position to move to 
        "delay": 20 
    }
```

#### Scroll
* **description**: Scrolls the mouse wheel by the given amount in ***notches*** not pixels. The ***speed*** is also in nothes per second not pixels.  
* **method**: **`POST`** `v1/inav/scroll`
* **payload**:
```json
    {
        "amount": 100,  // amount of notches to scroll by (positive values are down, and negative values are up)
        "function": "LINEAR", // easing function
        "speed": 30 // notches per second
    }
```


### Easing Functions
These are the `"function"` properties of most payloads. They are the functions used to interpolate mouse movement.

Checkout webite for easing examples: [https://easings.net/](https://easings.net/)

* **NONE**: no easing function, movements are instant
* **LINEAR**: no easing, movement is linear
* **QUADRATIC**: easing accellerates from 0 and decelerates to 0 in a quadratic fashion.
* **CUBIC**: easing accelerates from 0 and decelerates to 0 in a cubic fashion.



