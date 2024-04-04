package com.APEX.VoiceBridge;

import me.xdrop.fuzzywuzzy.FuzzySearch;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class BridgeController {
    private static final Logger logger = LoggerFactory.getLogger(BridgeController.class);
    private String voiceString;
    private String commandString;

    private final BridgeActions bridgeActions;

    private final Map<String, Runnable> bridgeMapping;

    public BridgeController() throws URISyntaxException {
        this.voiceString = "";
        this.commandString = "";
        this.bridgeActions = new BridgeActions();
        this.bridgeMapping = new HashMap<>();
        this.initializeBridgeMapping();
    }

    @GetMapping("/voice")
    public ResponseEntity<?> getVoice() {
        Map<String, String> response = new HashMap<>();
        response.put("voice", voiceString);
        return ResponseEntity.ok(response);
    }

    @PostMapping("/voice")
    public ResponseEntity<?> setVoice(@RequestBody String voiceString) {
        this.voiceString = voiceString;
        this.commandString = convertVoiceToCommand(this.voiceString);

        Map<String, String> response = new HashMap<>();
        response.put("voice", voiceString);
        response.put("command", commandString);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/command")
    public ResponseEntity<?> getCommand() {
        Map<String, String> response = new HashMap<>();
        response.put("command", commandString);
        return ResponseEntity.ok(response);
    }

    private void initializeBridgeMapping() {
        bridgeMapping.put("cursor move up", bridgeActions::cursorMoveUp);
        bridgeMapping.put("cursor move down", bridgeActions::cursorMoveDown);
        bridgeMapping.put("cursor move left", bridgeActions::cursorMoveLeft);
        bridgeMapping.put("cursor move right", bridgeActions::cursorMoveRight);
        bridgeMapping.put("cursor click left", bridgeActions::cursorClickLeft);
        bridgeMapping.put("cursor click right", bridgeActions::cursorClickRight);
        bridgeMapping.put("cursor click middle", bridgeActions::cursorClickMiddle);
        logger.info(bridgeMapping.keySet().toString());
    }

    // Acts like a passthrough for now - assumes that incoming voice strings are perfect
    // Add AI here (if we're still doing that)
    // For non-AI, maybe add some sort of fuzzy string matching
    public String convertVoiceToCommand(String voiceString) {
        String normalizedVoiceString = voiceString.toLowerCase();

        Map<String, String> bestCandidate = fuzzyFindStrategy(normalizedVoiceString);
        int bestScore = Integer.parseInt(bestCandidate.get("best"));
        int perfectCount = Integer.parseInt(bestCandidate.get("perfects"));
        String bestCommand = bestCandidate.get("command");

        if (bestScore <= 50 || perfectCount > 1) {
            logger.warn("Unknown command: {}:{}", bestScore, bestCommand);
            return "UNKNOWN_COMMAND";
        } else {
            Runnable action = this.bridgeMapping.get(bestCommand);
            if (action != null) {
                logger.info("Executing action for command: {}:{}", bestScore, bestCommand);
                action.run();
            }
            return bestCommand;
        }
    }

    public Map<String, String> fuzzyFindStrategy(String normalizedString) {
        int score;
        int bestScore = 0;
        int perfectCount = 0;
        for (String key : bridgeMapping.keySet()) {
            score = FuzzySearch.tokenSetRatio(voiceString, key);
            if (score == 100) {
                perfectCount++;
            }

            if (score > bestScore) {
                bestScore = score;
                normalizedString = key;
            }
            logger.info("{}:{}", score, key);
        }

        Map<String, String> results = new HashMap<>();
        results.put("best", String.valueOf(bestScore));
        results.put("perfects", String.valueOf(perfectCount));
        results.put("command", normalizedString);

        return results;
    }
}
