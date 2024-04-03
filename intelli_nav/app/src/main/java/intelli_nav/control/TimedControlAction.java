package intelli_nav.control;

import java.awt.Robot;

public abstract class TimedControlAction implements ControlAction{

    private long lastTime;

    public void init(){
        lastTime = System.nanoTime();
    }

    public boolean update(final Robot robot){
        long currentTime = System.nanoTime();
        float deltaTime = (currentTime - lastTime) / 1_000_000_000.0f;
        lastTime = currentTime;
        return onUpdate(robot, deltaTime);
    }

    public abstract boolean onUpdate(final Robot robot, final float deltaTime);

}
