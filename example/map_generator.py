from Capsian import *


@IndependentComponent
class Generator(Script):
    def gen_window(self, pos: list, size: list) -> None:
        import scripts.data as data

        for x in range(size[0]):
            for y in range(size[1]):
                for z in range(size[2]):
                    Cube(
                        Transform(
                            x=pos[0] + x,
                            y=pos[1] + y,
                            z=pos[2] + z,
                            depth=0.25,
                        ),

                        data.current_scene,
                        data.glass_mat
                    )

        
    def gen_flash(self, pos: list) -> None:
        from scripts.flashing_light import FlashingLight
        import scripts.data as data
        entt = Entity(
            Transform(
                x=pos[0],
                y=pos[1],
                z=pos[2]
            ),

            data.current_scene,
            False
        )
        light = FlashingLight(Color(50, 50, 0, 255).rgba)
        entt.components.add(light)

        Cube(
            Transform(
                0.35,
                1.7,
                0.35,
                width=0.3,
                height=0.3,
                depth=0.3
            ),

            data.current_scene,
            data.log_mat
        )

        Cube(
            Transform(
                0.375,
                2,
                0.375,
                width=0.25,
                height=0.25,
                depth=0.25
            ),

            data.current_scene,
            data.glow_mat
        )

        @engine.default_clock.Schedule.loop(interval = 1/3)
        def flash(dt):
            light.flash()


    def gen_floor(self, pos: list, size: list) -> None:
        import scripts.data as data

        for x in range(size[0]):
            for z in range(size[2]):
                Cube(
                    Transform(
                        x=pos[0] + x,
                        y=pos[1],
                        z=pos[2] + z,
                        height=size[1]
                    ),

                    data.current_scene,
                    data.planks_mat
                )


    def gen_table(self, pos: list) -> None:
        import scripts.data as data

        Cube(
            Transform(
                x=pos[0] + 0.375,
                y=pos[1],
                z=pos[2] + 0.375,
                width=0.25,
                height=0.15,
                depth=0.25
            ),

            data.current_scene,
            data.table_mat
        )

        Cube(
            Transform(
                x=pos[0] + 0.4375,
                y=pos[1] + 0.15,
                z=pos[2] + 0.4375,
                width=0.125,
                height=0.75,
                depth=0.125
            ),

            data.current_scene,
            data.table_mat
        )

        Cube(
            Transform(
                0.375,
                1,
                0.375,
                width=0.25,
                height=0.25,
                depth=0.25
            ),

            data.current_scene,
            data.log_mat
        )

        Cube(
            Transform(
                x=pos[0],
                y=pos[1] + 0.75 + 0.15,
                z=pos[2],
                height=0.3
            ),

            data.current_scene,
            data.table_mat
        )


    def on_start(self, time) -> None:
        import scripts.data as data
        self.gen_flash([0.5, 1.5, 0.5])
        self.gen_floor([-1, 0, -1], [3, 0.5, 3])
        self.gen_table([0, 0.5, 0])
