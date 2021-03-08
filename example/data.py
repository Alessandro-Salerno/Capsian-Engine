from Capsian import *


# Scenes
current_scene: Scene3D

# Textures
log_tex      = Texture3D("assets/textures/oak_log.png")
glass_tex    = Texture3D("assets/textures/glass.png")
planks_tex   = Texture3D("assets/textures/oak_planks.png")
trapdoor_tex = Texture3D("assets/textures/trapdoor.png")
table_tex    = Texture3D("assets/textures/table.png")
glow_tex     = Texture3D("assets/textures/glowstone.png")

# Materials
log_mat      = Material(log_tex)
glass_mat    = Material(glass_tex)
planks_mat   = Material(planks_tex)
trapdoor_mat = Material(trapdoor_tex)
table_mat    = Material(table_tex)
glow_mat     = Material(glow_tex)
