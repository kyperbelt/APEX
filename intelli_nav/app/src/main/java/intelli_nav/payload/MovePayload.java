package intelli_nav.payload;

import intelli_nav.math.EasingFunction;

public record MovePayload(EasingFunction function,float speed, int x, int y, int display) {
}

