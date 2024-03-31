package intelli_nav.payload;

import intelli_nav.math.EasingFunction;

public record ScrollPayload(int amount, EasingFunction function, float speed) {
}
