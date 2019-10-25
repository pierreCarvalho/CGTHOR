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


# Inserir o caminho do arquivo do obj
obj_filename2 = path.join('thorFinal.obj')
# Ler o arquivo obj e retorna os pontos
obj_reader = rc.WavefrontReader(obj_filename2)

# Create Mesh
thor = obj_reader.get_mesh("thor")
# Seta a posição inicial, escala, ?
thor.position.xyz = 0,0,-2
scale = .1
thor.scale = scale
thor.uniforms['diffuse'] = [.5, .0, .8]

# Cria a cena
scene = rc.Scene(meshes=[thor])
scene.bgColor = 0.4, 0.2, 0.4
scene.light.position = 0, 3, -1
# Cria a camera
camera = rc.Camera(projection=rc.PerspectiveProjection(fov_y=90, aspect=1.))
scene.camera = camera
#Faz a projeção da cena
projected_scene = rc.Scene(meshes=[thor], bgColor=(1., 1., 1.))
projected_scene.light.position = scene.light.position
projected_scene.camera = rc.Camera(position=(0, 0, 5), rotation=(0, 0, 0))
projected_scene.camera.projection.z_far = 50

# Atualiza a movimentação da camera e do objeto
def move_camera(dt):
    global scale
    global projected_scene
    camera_speed = 1
    if keys[key.W]:
        thor.scale.x += 0.1
        thor.scale.y += 0.1
        thor.scale.z += 0.1
    elif keys[key.S]:
        thor.scale.z -= 0.1
        thor.scale.y -= 0.1
        thor.scale.x -= 0.1
    elif keys[key.J]:
        thor.rotation.y += 0.5
    elif keys[key.U]:
        thor.rotation.x -= 0.5
    elif keys[key.K]:
        thor.rotation.z += 0.5
    elif keys[key.RIGHT]:
        projected_scene.camera.position.x += camera_speed * dt
    elif keys[key.LEFT]:
        projected_scene.camera.position.x -= camera_speed * dt
    elif keys[key.UP]:
        projected_scene.camera.position.y += camera_speed * dt
    elif keys[key.DOWN]:
        projected_scene.camera.position.y -= camera_speed * dt
  
pyglet.clock.schedule(move_camera)

@window.event
def on_draw():
    with rc.default_shader:
      projected_scene.draw()

pyglet.app.run()
