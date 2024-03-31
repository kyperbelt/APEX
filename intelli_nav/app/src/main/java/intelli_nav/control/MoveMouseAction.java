package intelli_nav.control;

import java.awt.MouseInfo;
import java.awt.Robot;

import org.slf4j.Logger;

import intelli_nav.Utils;
import intelli_nav.math.EasingFunction;
import intelli_nav.payload.MovePayload;

public class MoveMouseAction extends TimedControlAction {

    private static Logger log = Utils.createLogger();

    private int x;
    private int y;
    private float speed;
    private EasingFunction function;

    private int startX;
    private int startY;
    private float duration;
    private float elapsed;

    public MoveMouseAction(MovePayload payload) {
        this.x = payload.x();
        this.y = payload.y();
        this.speed = payload.speed();
        this.function = payload.function();
    }

    @Override
    public void init() {
        super.init();
        startX = (int) MouseInfo.getPointerInfo().getLocation().getX();
        startY = (int) MouseInfo.getPointerInfo().getLocation().getY();
        float distance = (float) Math.sqrt(Math.pow(x - startX, 2) + Math.pow(y - startY, 2));
        duration = Math.max(distance / speed, 0.00001f);
        if (function == EasingFunction.NONE) {
            elapsed = duration;
        } else {
            elapsed = 0;
        }

        log.info("Moving mouse to ({}, {}) in {} seconds", x, y, duration);
    }

    @Override
    public boolean onUpdate(final Robot robot, final float deltaTime) {
        elapsed += deltaTime;
        float alpha = Math.min(elapsed / duration, 1);
        int newX = (int) function.ease(alpha, startX, x);
        int newY = (int) function.ease(alpha, startY, y);
        robot.mouseMove(newX, newY);

        boolean finished = alpha == 1;
        if (finished) {
            log.info("Mouse movement finished");
        }
        return finished;
    }

}
