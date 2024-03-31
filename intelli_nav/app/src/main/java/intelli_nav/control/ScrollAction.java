
package intelli_nav.control;

import java.awt.Robot;

import org.slf4j.Logger;

import intelli_nav.Utils;
import intelli_nav.math.EasingFunction;
import intelli_nav.payload.ScrollPayload;

public class ScrollAction extends TimedControlAction {
	public static final Logger log = Utils.createLogger();

	private final int amount;
	private final EasingFunction function;
	private final float speed;

	private float duration = 0.0f;
	private float elapsed = 0.0f;
	private int amountScrolled = 0;

	public ScrollAction(ScrollPayload payload) {
		this.amount = payload.amount();
		this.function = payload.function();
		this.speed = payload.speed();
	}

	@Override
	public void init() {
		super.init();

		duration = Math.max(Math.abs(amount) / speed, 0.00001f);
		if (function == EasingFunction.NONE) {
			elapsed = duration;
		} else {
			elapsed = 0;
		}
		log.info("ScrollAction Started | Amount: {}, Speed: {}, Function: {}", amount, speed, function);
		log.info("Duration: {}", duration);

	}

	@Override
	public boolean onUpdate(Robot robot, float deltaTime) {
		elapsed += deltaTime;
		float alpha = elapsed / duration;
		float value = function.ease(alpha, 0, amount);
		int scrollAmount = (int) (value - amountScrolled);
		amountScrolled += scrollAmount;
		while(scrollAmount != 0){
			robot.mouseWheel(scrollAmount > 0 ? 1 : -1);
			scrollAmount += scrollAmount > 0 ? -1 : 1;
		}

		if (elapsed >= duration) {
			log.info("ScrollAction Finished");
			return true;
		}
		return false;
	}

}
