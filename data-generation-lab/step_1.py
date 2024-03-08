import omni.replicator.core as rep

with rep.new_layer():
    # Define paths for the character, the props, the environment and the surface where the assets will be scattered in.
    CRATE = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Samples/Marbles/assets/standalone/SM_room_crate_3/SM_room_crate_3.usd'
    SURFACE = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/Scenes/Templates/Basic/display_riser.usd'
    ENVS = 'omniverse://ove-nucleus.courses.nvidia.com/NVIDIA/Assets/Scenes/Templates/Interior/ZetCG_ExhibitionHall.usd'

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