package intelli_nav.math;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Easing functions for interpolating between values.
 * 
 * check this website for a list of easing functions and how they look:
 * https://easings.net/
 */
public enum EasingFunction {
    NONE(null),
    LINEAR(EasingFunctionImpl.LINEAR),
    QUADRATIC(new EasingFunctionImpl() {
        @Override
        public float ease(float alpha, float start, float end) {
            // quad_in_out
            float t = alpha;
            if (t < 0.5f) {
                t = 2 * alpha * alpha;
            } else {
                t = 1- (float) Math.pow(-2 * alpha + 2, 2) / 2;
            }
            return start + (end - start) * t;
        }
    }),
    CUBIC(new EasingFunctionImpl() {
        // cubic_in_out
        @Override
        public float ease(float alpha, float start, float end) {
            float t = alpha;
            if (t < 0.5f) {
                t = 4 * alpha * alpha * alpha;
            } else {
                t = 1 - (float) Math.pow(-2 * alpha + 2, 3) / 2;
            }
            return start + (end - start) * t;
        }
    });

    public static Logger log = LoggerFactory.getLogger(EasingFunction.class);

    private EasingFunctionImpl impl;

    public float ease(float alpha, float start, float end) {
        if (impl == null) {
            log.warn("No easing function specified, returning end value");
            return end; // No easing
        }
        return impl.ease(alpha, start, end);
    }

    EasingFunction(EasingFunctionImpl impl) {
        this.impl = impl;
    }
}
