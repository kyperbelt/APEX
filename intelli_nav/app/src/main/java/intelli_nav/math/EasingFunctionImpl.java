package intelli_nav.math;

public interface EasingFunctionImpl {
    /**
     * @param alpha The alpha value to use for the easing function
     * @param start The start value of the easing function
     * @param end The end value of the easing function
     * @return The eased value
     */
    public float ease(float alpha, float start, float end);

    public static final EasingFunctionImpl LINEAR = new EasingFunctionImpl() {
        @Override
        public float ease(float alpha, float start, float end) {
            return start + (end - start) * alpha;
        }
    };
}
