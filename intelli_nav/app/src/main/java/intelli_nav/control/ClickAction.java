package intelli_nav.control;

import java.awt.MouseInfo;
import java.awt.Robot;

import org.slf4j.Logger;

import intelli_nav.Buttons;
import intelli_nav.Utils;
import intelli_nav.math.EasingFunction;
import intelli_nav.payload.ClickPayload;

public class ClickAction extends TimedControlAction {
	private static final Logger log = Utils.createLogger();

	private final Buttons button;
	private final int x;
	private final int y;
	private final int delay;
	private final float speed;
	private final EasingFunction function;

	private int startX;
	private int startY;

	private float duration = 0.0f;
	private float elapsed = 0.0f;

	public ClickAction(final ClickPayload payload) {
		this.button = payload.button();
		this.x = payload.x();
		this.y = payload.y();
		this.delay = payload.delay();
		this.speed = payload.speed();
		this.function = payload.function();
	}

	@Override
	public void init() {
		super.init();
		startX = MouseInfo.getPointerInfo().getLocation().x;
		startY = MouseInfo.getPointerInfo().getLocation().y;

		float distance = (float) Math.sqrt((x - startX) * (x - startX) + (y - startY) * (y - startY));
		duration = Math.max(distance / speed, 0.00001f);
		if (function == EasingFunction.NONE) {
			elapsed = duration;
		} else {
			elapsed = 0;
		}
		log.info("ClickAction Started |\n\tButton: {}, X: {}, Y: {}, Delay: {}, Speed: {}, Function: {}",
				button,
				x,
				y,
				delay,
				speed, function);
	}

	@Override
	public boolean onUpdate(Robot robot, float deltaTime) {
		elapsed += deltaTime;
		float alpha = Math.min(elapsed / duration, 1);
		int newX = (int) function.ease(alpha, startX, x);
		int newY = (int) function.ease(alpha, startY, y);
		robot.mouseMove(newX, newY);

		boolean finished = alpha == 1;
		if (finished) {
			robot.mousePress(button.getButton());
			robot.delay(delay);
			robot.mouseRelease(button.getButton());
			log.info("ClickAction finished");
		}
		return finished;
	}

}
