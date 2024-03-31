package intelli_nav.control;

import java.awt.Robot;
import java.util.LinkedList;
import java.util.Queue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Manages the robot and the actions that it should perform while the
 * applicastion is running. The actions are queued
 * and executed one by one.
 */
public class RobotManager {
    private static final int MAX_ACTIONS = 10;

    private static final Logger log = LoggerFactory.getLogger(RobotManager.class);
    private Robot robot;
    private Queue<ControlAction> actions;

    public RobotManager() {
        try {
            robot = new Robot();
        } catch (Exception e) {
            log.error("Error creating Robot", e);
        }

        actions = new LinkedList<ControlAction>();

        log.info("Robot created");
    }

    /**
     * Adds an action to the queue.
     * 
     * @param action The action to add.
     */
    public synchronized void addAction(ControlAction action) {
        if (actions.size() >= MAX_ACTIONS) {
            log.warn("Max actions reached");
            return;
        }
        if (actions.isEmpty()) {
            action.init();
        }
        actions.add(action);
    }

    /**
     * Clears the action queue.
     */
    public synchronized void clearActions() {
        actions.clear();
    }

    /**
     * Updates the current action. If the action is finished, it is removed
     * from the queue and the next action is initialized.
     */
    public synchronized void update() {

        if (actions.isEmpty()) {
            return;
        }

        ControlAction action = actions.peek();
        boolean finished = action.update(robot);
        if (finished) {
            actions.poll();
            if (!actions.isEmpty()) {
                log.info("Next action");
                actions.peek().init();
            }
        }

    }
}
