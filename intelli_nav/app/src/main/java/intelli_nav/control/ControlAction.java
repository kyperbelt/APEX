package intelli_nav.control;

import java.awt.Robot;

public interface ControlAction {
    public void init();
    public boolean update(final Robot robot);
}
