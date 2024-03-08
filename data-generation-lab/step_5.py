import omni.replicator.core as rep

with rep.new_layer():
    CRATE = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Samples/Marbles/assets/standalone/SM_room_crate_3/SM_room_crate_3.usd'
    SURFACE = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/Scenes/Templates/Basic/display_riser.usd'
    ENVS = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/Scenes/Templates/Interior/ZetCG_ExhibitionHall.usd'
    FRUIT_PROPS = {
        'apple': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Apple.usd',
        'avocado': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Avocado01.usd',
        'kiwi': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Kiwi01.usd',
        'lime': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Lime01.usd',
        'lychee': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Lychee01.usd',
        'pomegranate': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Pomegranate01.usd',
        'onion': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Vegetables/RedOnion.usd',
        'strawberry': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Food/Berries/strawberry.usd',
        'lemon': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Decor/Tchotchkes/Lemon_01.usd',
        'orange': 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_01.usd'    }
    
    def random_props(file_name, class_name, max_number=1, one_in_n_chance=3):
        instances = rep.randomizer.instantiate(file_name, size=max_number, mode='scene_instance')
        with instances:
            # First implementation of collisions for Replicator, further work coming to keep objects from overlapping
            rep.physics.collider()
            rep.modify.semantics([('class', class_name)])
            rep.modify.pose(
                position=rep.distribution.uniform((-4, 4, -25), (4, 15, 25)),
                rotation=rep.distribution.uniform((-180,-180, -180), (180, 180, 180)),
                scale = rep.distribution.uniform((0.8), (1.2)),
            )
            rep.modify.visibility(rep.distribution.choice([True],[False]*(one_in_n_chance)))
        return instances.node
    
    def sphere_lights(num):
        lights = rep.create.light(
            light_type="Sphere",
            temperature=rep.distribution.normal(3000, 500),
            intensity=rep.distribution.normal(30000, 1000),
            position=rep.distribution.uniform((-300, -300, -300), (300, 300, 300)),
            scale=rep.distribution.uniform(50, 100),
            count=num        )
        return lights.node

    # Setup the static elements
    env = rep.create.from_usd(ENVS)
    surface = rep.create.from_usd(SURFACE)
    with surface:
        rep.physics.collider()
    crate = rep.create.from_usd(CRATE)
    with crate:
        rep.physics.collider()
        rep.physics.mass(mass=100)
        rep.modify.pose(
                position=(0,20,0),
                rotation=(0, 0, 90)
            )
        
    # setup the camera and attach it to render the product
    camera =  rep.create.camera()
    render_product = rep.create.render_product(camera, resolution=(1024, 1024))

    rep.randomizer.register(random_props)
    rep.randomizer.register(sphere_lights)

    # trigger on frame for an interval
    with rep.trigger.on_frame(num_frames=100):
        for n, f in FRUIT_PROPS.items():
            random_props(f, n)
        rep.randomizer.sphere_lights(5)
        with camera:
            rep.modify.pose(position=rep.distribution.uniform((-20, 90, -17), (10, 140, -15)), look_at=(0,20,0))

    writer = rep.WriterRegistry.get("BasicWriter")
    now=now.strftime("%Y-%m-%d_%H:%M:%S")
    output_dir = "/dli/task/data/fruit_data_"+now
    writer.initialize( output_dir=output_dir, rgb=True, bounding_box_2d_tight=True)
    writer.attach([render_product])

# modifications to run headless missing
# rep.orchestrator.run()