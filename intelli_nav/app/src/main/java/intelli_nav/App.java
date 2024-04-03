package intelli_nav;

import io.javalin.Javalin;
import static io.javalin.apibuilder.ApiBuilder.*;

import intelli_nav.control.ClickAction;
import intelli_nav.control.MoveMouseAction;
import intelli_nav.control.RobotManager;
import intelli_nav.control.ScrollAction;
import intelli_nav.payload.ClickPayload;
import intelli_nav.payload.MovePayload;
import intelli_nav.payload.ScrollPayload;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {

        final RobotManager robotManager = new RobotManager();

        var app = Javalin.create(config -> {
            config.router.apiBuilder(() -> {
                path("v1", () -> {
                    path("inav", () -> {
                        path("move", () -> {
                            post(ctx -> {
                                var payload = ctx.bodyAsClass(MovePayload.class);
                                robotManager.addAction(new MoveMouseAction(payload));
                                ctx.status(200);
                            });
                        });
                        path("click", () -> {
                            post(ctx -> {
                                var payload = ctx.bodyAsClass(ClickPayload.class);
                                robotManager.addAction(new ClickAction(payload));
                                ctx.status(200);
                            });
                        });
                        path("scroll", () -> {
                            post(ctx -> {
                                var payload = ctx.bodyAsClass(ScrollPayload.class);
                                robotManager.addAction(new ScrollAction(payload));
                                ctx.status(200);
                            });
                        });
                    });
                });
            });
        })
                .start(7070);

        while (true) {
            robotManager.update();
            try {
                Thread.sleep(33);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
