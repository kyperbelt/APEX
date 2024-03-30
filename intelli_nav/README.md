# IntelliNav API

## Mouse

### Movement
* method: **`POST`** `v1/inav/move`
* payload: 
    ```json
        {
            "function": "NONE", // easing function
            "speed": 100,       // speed of mouse in pixels if function is other than NONE
            "x": 300,           // x position to move to on the given display
            "y": 200,           // y position to move to on the given display
            "display" : 0       // display to move to <if multiple displays present>
        }  
    ```

### Click
* method: **`POST`** `v1/inav/click`
* payload:
```json
    {
        "button": "LEFT", // button to click
    }
```

### Scroll
* method: **`POST`** `v1/inav/scroll`
* payload:
```json
    {
        "axis": "X" // the axis of scroll
        "amount": 100 // amount to scroll by
        "function": "NONE" // easing function
        "speed": 300 // pixels per second
    }
```




