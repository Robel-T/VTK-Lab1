# Titre : Bonhomme de neige
# Description : Laboratoire 1 du cours de VTK
# Auteurs : Jael Dubey et Robel Teklehaimanot
# Date : 05 avril 1959 (lorsqu'il neigeait encore dans ce monde).


import vtk
import time

WAITING_TIME = 0.02


def create_sphere(radius, center, theta_resolution=50, phi_resolution=50):
    sphere = vtk.vtkSphereSource()
    sphere.SetThetaResolution(theta_resolution)
    sphere.SetPhiResolution(phi_resolution)
    sphere.SetCenter(center[0], center[1], center[2])
    sphere.SetRadius(radius)

    return sphere


def create_cone(radius, center, height, direction, resolution=50):
    cone = vtk.vtkConeSource()
    cone.SetHeight(height)
    cone.SetResolution(resolution)
    cone.SetDirection(direction[0], direction[1], direction[2])
    cone.SetCenter(center[0], center[1], center[2])
    cone.SetRadius(radius)

    return cone


def create_actor(obj):
    obj_mapper = vtk.vtkPolyDataMapper()
    obj_mapper.SetInputConnection(obj.GetOutputPort())

    obj_actor = vtk.vtkActor()
    obj_actor.SetMapper(obj_mapper)

    return obj_actor


def loop_camera(max_range, camera_function, val, ren_win):
    for i in range(0, max_range):
        time.sleep(WAITING_TIME)
        camera_function(val)
        ren_win.Render()


def loop_actor(max_range, function, val, ren_win):
    for i in range(0, max_range):
        time.sleep(WAITING_TIME)
        ren_win.Render()

        function(val)


body = create_sphere(0.7, (0, 0, 0))
head = create_sphere(0.5, (-1.5, 0, 0))
nose = create_cone(0.08, (1.05, 0, 0), 0.3, (0, -1, 0))

left_eye = create_sphere(0.1, (-0.15, 1.2, 0))
right_eye = create_sphere(0.1, (0.15, 1.2, 0))

body_actor = create_actor(body)
head_actor = create_actor(head)
nose_actor = create_actor(nose)

left_eye_actor = create_actor(left_eye)
right_eye_actor = create_actor(right_eye)

nose_actor.GetProperty().SetColor(1, 0.741, 0)
left_eye_actor.GetProperty().SetColor(0, 0, 0)
right_eye_actor.GetProperty().SetColor(0, 0, 0)

# Create renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(body_actor)
renderer.AddActor(head_actor)
renderer.AddActor(nose_actor)
renderer.SetBackground(0.1, 0.1, 0.1)

# Create camera
cam = vtk.vtkCamera()
cam.SetFocalPoint(0, 0, 0)
cam.SetPosition(0, 0, 10)

renderer.SetActiveCamera(cam)

# Create window
ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(renderer)
ren_win.SetSize(600, 600)

# Put the head above the body
loop_actor(90, head_actor.RotateZ, -1, ren_win)

# Attach head and body
for i in range(0, 40):
    time.sleep(WAITING_TIME)
    ren_win.Render()

    nose_position = head_actor.GetPosition()
    head_actor.SetPosition(nose_position[0], nose_position[1] - 0.01, nose_position[2])

# Rotate the nose above the body
loop_actor(90, nose_actor.RotateY, -1, ren_win)

# Put the nose in the head
loop_actor(90, nose_actor.RotateZ, 1, ren_win)

# Show the eyes
renderer.AddActor(left_eye_actor)
renderer.AddActor(right_eye_actor)

# Go up eyes and nose
for i in range(0, 50):
    time.sleep(WAITING_TIME)
    ren_win.Render()

    nose_position = nose_actor.GetPosition()
    le_position = left_eye_actor.GetPosition()
    re_position = right_eye_actor.GetPosition()

    nose_actor.SetPosition(nose_position[0], nose_position[1], nose_position[2] + 0.012)
    left_eye_actor.SetPosition(le_position[0], le_position[1], le_position[2] + 0.008)
    right_eye_actor.SetPosition(re_position[0], re_position[1], re_position[2] + 0.008)

# Camera 360 on Roll
loop_camera(360, renderer.GetActiveCamera().Roll, 1, ren_win)

# Camera 360 on Azimuth
loop_camera(360, renderer.GetActiveCamera().Azimuth, 1, ren_win)

# Camera 90 on Elevation
loop_camera(90, renderer.GetActiveCamera().Elevation, 1, ren_win)

# Camera -90 on Elevation
loop_camera(90, renderer.GetActiveCamera().Elevation, -1, ren_win)

time.sleep(5)
