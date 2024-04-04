package com.APEX.VoiceBridge;

import org.json.JSONObject;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

public class BridgeActions {
    int[] position = {0, 0};

    URI uri = new URI("http://localhost:7070/v1/inav");
    private RestTemplate restTemplate;

    public BridgeActions() throws URISyntaxException {
        this.restTemplate = new RestTemplate();
    }

    public void cursorMoveUp() {

    }

    public void cursorMoveDown() {

    }

    public void cursorMoveLeft() {

    }

    public void cursorMoveRight() {

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
        payload.put("x", 200);
        payload.put("y", 300);
        payload.put("delay", 0);
        apiPostRequest(endpoint, payload);
    }

    public void cursorClickRight() {
        String endpoint = "/click";
        JSONObject payload = new JSONObject();
        payload.put("button", "RIGHT");
        payload.put("function", "CUBIC");
        payload.put("x", 200);
        payload.put("y", 300);
        payload.put("delay", 0);
        apiPostRequest(endpoint, payload);
    }

    public void cursorClickMiddle() {
        /*
        {
            "amount": 100,  // amount of notches to scroll by (positive values are down, and negative values are up)
            "function": "LINEAR", // easing function
            "speed": 30 // notches per second
        }
         */
        String endpoint = "/scroll";
        JSONObject payload = new JSONObject();
        payload.put("amount", 100);
        payload.put("function", "LINEAR");
        payload.put("speed", 30);
        apiPostRequest(endpoint, payload);
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
