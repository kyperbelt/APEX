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

    private final Map<String, Runnable> bridgeMapping;

    public BridgeController() {
        this.voiceString = "";
        this.commandString = "";
        this.bridgeActions = new BridgeActions();
        this.bridgeMapping = new HashMap<>();
        this.initializeBridgeMapping();
    }

    @GetMapping("/voice")
    public ResponseEntity<?> getVoice() {
        return ResponseEntity.ok(voiceString);
    }

    @PostMapping("/voice")
    public ResponseEntity<?> setVoice(String voiceString) {
        this.voiceString = voiceString;
        this.commandString = convertVoiceToCommand(this.voiceString);
        return ResponseEntity.ok(voiceString);
    }

    @GetMapping("/command")
    public ResponseEntity<?> getCommand() {
        return ResponseEntity.ok(commandString);
    }

    private void initializeBridgeMapping() {
        bridgeMapping.put("cursor move up", bridgeActions::cursorMoveUp);
        bridgeMapping.put("cursor move down", bridgeActions::cursorMoveDown);
        bridgeMapping.put("cursor move left", bridgeActions::cursorMoveLeft);
        bridgeMapping.put("cursor move right", bridgeActions::cursorMoveRight);
        bridgeMapping.put("cursor click left", bridgeActions::cursorClickLeft);
        bridgeMapping.put("cursor click right", bridgeActions::cursorClickRight);
        bridgeMapping.put("cursor click middle", bridgeActions::cursorClickMiddle);
    }

    // Acts like a passthrough for now - assumes that incoming voice strings are perfect
    // Add AI here (if we're still doing that)
    // For non-AI, maybe add some sort of fuzzy string matching
    public String convertVoiceToCommand(String voiceString) {
        String normalizedVoiceString = voiceString.toLowerCase();
        Runnable action = this.bridgeMapping.get(normalizedVoiceString);
        if (action != null) {
            action.run();
            return normalizedVoiceString;
        }
        return "UNKNOWN_COMMAND";
    }
}
