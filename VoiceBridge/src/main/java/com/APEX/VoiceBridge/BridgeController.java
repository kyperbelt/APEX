package com.APEX.VoiceBridge;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class BridgeController {
    private String voiceString;
    private String commandString;

    private final BridgeActions bridgeActions;

    private Map<String, Runnable> bridgeMapping;

    public BridgeController() {
        this.voiceString = "";
        this.commandString = "";
        this.bridgeActions = new BridgeActions();
        this.bridgeMapping = new HashMap<>();

    }

    @GetMapping("/voice")
    public ResponseEntity<?> getVoice() {
        return ResponseEntity.ok(voiceString);
    }

    @PostMapping("/voice")
    public ResponseEntity<?> setVoice(String voiceString) {
        this.voiceString = voiceString;
        return ResponseEntity.ok(voiceString);
    }

    @GetMapping("/command")
    public ResponseEntity<?> getCommand() {
        return ResponseEntity.ok(commandString);
    }

    private void initializeBridgeMapping() {
        bridgeMapping.put("Cursor move up", bridgeActions::cursorMoveUp);
        bridgeMapping.put("Cursor move down", bridgeActions::cursorMoveDown);
        bridgeMapping.put("Cursor move left", bridgeActions::cursorMoveLeft);
        bridgeMapping.put("Cursor move right", bridgeActions::cursorMoveRight);
        bridgeMapping.put("Cursor click left", bridgeActions::cursorClickLeft);
        bridgeMapping.put("Cursor click right", bridgeActions::cursorClickRight);
        bridgeMapping.put("Cursor click middle", bridgeActions::cursorClickMiddle);
    }
}
