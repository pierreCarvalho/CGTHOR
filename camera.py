import pyglet
from pyglet.window import key
from os import path
import ratcave as rc


#sets e configs
#tela
window = pyglet.window.Window()
#setas para a camera
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Insert filename into WavefrontReader.
obj_filename2 = path.join('thorFinal.obj')
#obj_filename = rc.resources.obj_primitives()
obj_reader = rc.WavefrontReader(obj_filename2)

# Create Mesh
thor = obj_reader.get_mesh("thor")
thor.position.xyz = 0,0,-2
scale = .1
thor.scale = scale

# Create Scene
scene = rc.Scene(meshes=[thor])
scene.bgColor = 0.4, 0.2, 0.4

def move_camera(dt):
  global scale
  camera_speed = 3
  if keys[key.W]:
    print(thor.scale)
    thor.scale.x += 0.1
    thor.scale.y += 0.1
    thor.scale.z += 0.1

    scene = rc.Scene(meshes=[thor])
    scene.bgColor = 0.4, 0.2, 0.4
  if keys[key.S]:
    thor.scale.x -= 0.1
    thor.scale.y -= 0.1
    thor.scale.z += 0.1
    scene = rc.Scene(meshes=[thor])
    scene.bgColor = 0.4, 0.2, 0.4
  if keys[key.RIGHT]:
      scene.camera.position.x += camera_speed * dt
  if keys[key.UP]:
      scene.camera.position.y += camera_speed * dt
  if keys[key.DOWN]:
      scene.camera.position.y -= camera_speed * dt
pyglet.clock.schedule(move_camera)


@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()


pyglet.app.run()