package intelli_nav.model;

import intelli_nav.EasingFunction;

public record MovePayload(EasingFunction function,float speed, int x, int y) {
}

