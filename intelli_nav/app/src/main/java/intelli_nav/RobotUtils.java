package intelli_nav;

import java.awt.Robot;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class RobotUtils {
    private static final Logger log = LoggerFactory.getLogger(RobotUtils.class);
    private Robot robot;

    public RobotUtils() {
        try {
            robot = new Robot();
            robot.setAutoDelay(40);
        } catch (Exception e) {
            log.error("Error creating Robot", e);
        }

        log.info("Robot created");
    }
    public void moveMouse(int x, int y) {
        robot.mouseMove(x, y);
    }
}
