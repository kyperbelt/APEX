package intelli_nav.payload;

import intelli_nav.Buttons;
import intelli_nav.math.EasingFunction;

public record ClickPayload(Buttons button, int x, int y, int delay, float speed, EasingFunction function, int display){
}
