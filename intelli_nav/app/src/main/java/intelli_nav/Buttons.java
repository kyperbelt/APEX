package intelli_nav;

import java.awt.event.InputEvent;

/**
 * Enum for the mouse buttons
 */
public enum Buttons {
    LEFT(InputEvent.BUTTON1_DOWN_MASK),
    MIDDLE(InputEvent.BUTTON2_DOWN_MASK),
    RIGHT(InputEvent.BUTTON3_DOWN_MASK);

    private final int button;

    Buttons(int button) {
        this.button = button;
    }

    public int getButton() {
        return button;
    }
}
