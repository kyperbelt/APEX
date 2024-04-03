package intelli_nav;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Utils {
    public static Logger createLogger() {
        try {
            Class<?> clazz = getCallerClass(2);
            return LoggerFactory.getLogger(clazz);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            return null;
        }
    };

    public static Class<?> getCallerClass(int level) throws ClassNotFoundException {
        StackTraceElement[] stElements = Thread.currentThread().getStackTrace();
        String rawFQN = stElements[level + 1].toString().split("\\(")[0];
        return Class.forName(rawFQN.substring(0, rawFQN.lastIndexOf('.')));
    }
}
