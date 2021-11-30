from Capsian import *
import json


with open("autowin.json", "r") as autowin:
    global preferences
    preferences = json.loads(autowin.read())


win_prefs     = preferences["Window"]
window_width  = int(win_prefs["Width"])
window_height = int(win_prefs["Height"])
window_vsync  = bool(win_prefs["VSync"])

cam_prefs     = preferences["Camera"]
cam_pos       = cam_prefs["Position"]
camera_x      = float(cam_pos[0])
camera_y      = float(cam_pos[1])
camera_z      = float(cam_pos[2])
cam_rot       = cam_prefs["Rotation"]
cam_rotx      = float(cam_rot[0])
cam_roty      = float(cam_rot[1])
cam_rotz      = float(cam_rot[2])
cam_far       = float(cam_prefs["Draw Distance"])
cam_fov       = float(cam_prefs["Field of View"])


camera = PerspectiveCamera(
    transform=Transform(
        x=camera_x,
        y=camera_y,
        z=camera_z,
        width=1,
        height=1,
        depth=1,
        rotX=cam_rotx,
        rotY=cam_roty,
        rotZ=cam_rotz
    ),

    fov=cam_fov,
    far=cam_far
)

window = Window3D(
    camera,
    width=window_width,
    height=window_height,
    resizable=True,
    vsync=window_vsync
)
