package com.APEX.VoiceBridge;

import org.json.JSONObject;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.net.URI;
import java.net.URISyntaxException;

public class BridgeActions {
    int xPos, yPos;
    int MOVE_SIZE = 50;
    int MOVE_SPEED = 100;
    int SCROLL_SIZE = 10;
    int SCROLL_SPEED = 30;

    URI uri = new URI("http://localhost:7070/v1/inav");
    private final RestTemplate restTemplate;

    public BridgeActions() throws URISyntaxException {
        this.restTemplate = new RestTemplate();
    }

    public void cursorMoveUp() {
        /*{
            "function": "LINEAR", // easing function
            "speed": 100,       // speed of mouse in pixels if function is other than NONE
            "x": 300,           // x position to move to on the given display
            "y": 200,           // y position to move to on the given display
            "display" : 0       // display to move to <if multiple displays present>
        }*/
        this.getPosition();
        JSONObject payload = new JSONObject();
        payload.put("function", "CUBIC");
        payload.put("speed", MOVE_SPEED);
        payload.put("x", this.xPos);
        payload.put("y", this.yPos - MOVE_SIZE);
        this.yPos -= MOVE_SIZE;
        payload.put("display", 0);
        apiPostRequest("/move", payload);
    }

    public void cursorMoveDown() {
        this.getPosition();
        JSONObject payload = new JSONObject();
        payload.put("function", "CUBIC");
        payload.put("speed", MOVE_SPEED);
        payload.put("x", this.xPos);
        payload.put("y", this.yPos + MOVE_SIZE);
        this.yPos += MOVE_SIZE;
        payload.put("display", 0);
        apiPostRequest("/move", payload);
    }

    public void cursorMoveLeft() {
        this.getPosition();
        JSONObject payload = new JSONObject();
        payload.put("function", "CUBIC");
        payload.put("speed", MOVE_SPEED);
        payload.put("x", this.xPos - MOVE_SIZE);
        payload.put("y", this.yPos);
        this.xPos -= MOVE_SIZE;
        payload.put("display", 0);
        apiPostRequest("/move", payload);
    }

    public void cursorMoveRight() {
        this.getPosition();
        JSONObject payload = new JSONObject();
        payload.put("function", "CUBIC");
        payload.put("speed", MOVE_SPEED);
        payload.put("x", this.xPos + MOVE_SIZE);
        payload.put("y", this.yPos);
        this.xPos += MOVE_SIZE;
        payload.put("display", 0);
        apiPostRequest("/move", payload);
    }

    public void cursorClickLeft() {
        /*{
            "button": "LEFT",   // button on the mouse
            "function": "LINEAR", // easing function
            "speed": 1000,      // speed of mouse in pixels if function is other than NONE
            "x": 200,           // x position to move to on the given display
            "y": 300,           // y position to move to
            "delay": 20
        }*/
        String endpoint = "/click";
        JSONObject payload = new JSONObject();
        payload.put("button", "LEFT");
        payload.put("function", "CUBIC");
        payload.put("x", xPos);
        payload.put("y", yPos);
        payload.put("delay", 0);
        apiPostRequest(endpoint, payload);
    }

    public void cursorClickRight() {
        String endpoint = "/click";
        JSONObject payload = new JSONObject();
        payload.put("button", "RIGHT");
        payload.put("function", "CUBIC");
        payload.put("x", xPos);
        payload.put("y", yPos);
        payload.put("delay", 0);
        apiPostRequest(endpoint, payload);
    }

    public void cursorClickMiddle() {
        /* In case we want to middle click w/ cursor movements for scrolling */
    }

    public void cursorScrollUp() {
        String endpoint = "/scroll";
        JSONObject payload = new JSONObject();
        payload.put("amount", -SCROLL_SIZE);
        payload.put("speed", SCROLL_SPEED);
        payload.put("function", "LINEAR");
        apiPostRequest(endpoint, payload);
    }

    public void cursorScrollDown() {
        String endpoint = "/scroll";
        JSONObject payload = new JSONObject();
        payload.put("amount", SCROLL_SIZE);
        payload.put("speed", SCROLL_SPEED);
        payload.put("function", "LINEAR");
        apiPostRequest(endpoint, payload);
    }

    public void getPosition() {
        JSONObject result = apiGetRequest("/position");
        this.xPos = result.getInt("x");
        this.yPos = result.getInt("y");
    }

    // Generic API call
    public JSONObject apiGetRequest(String endpoint) {
        String url = this.uri + endpoint;
        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);
        String body = response.getBody();
        return new JSONObject(body);
    }

    public void apiPostRequest(String endpoint, JSONObject body) {
        String url = this.uri + endpoint;
        restTemplate.postForEntity(url, body.toString(), String.class);
//        String responseBody = response.getBody();
//        return new JSONObject(responseBody);
    }
}
