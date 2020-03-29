import vtk
import time


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


body = create_sphere(0.7, (0, 0, 0))
head = create_sphere(0.5, (-1.5, 0, 0))
nose = create_cone(0.08, (1.1, 0, 0), 0.3, (0, -1, 0))

body_actor = create_actor(body)
head_actor = create_actor(head)
nose_actor = create_actor(nose)

nose_actor.GetProperty().SetColor(1, 0.741, 0)

# Create renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(body_actor)
renderer.AddActor(head_actor)
renderer.AddActor(nose_actor)
renderer.SetBackground(0.1, 0.1, 0.1)


# Create window
ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(renderer)
ren_win.SetSize(600, 600)

# Put the head above the body
for i in range(0, 90):
    time.sleep(0.03)
    ren_win.Render()

    head_actor.RotateZ(-1)


# Attach head and body
for i in range(0, 40):
    time.sleep(0.03)
    ren_win.Render()

    position = head_actor.GetPosition()
    head_actor.SetPosition(position[0], position[1]-0.01, position[2])

# Rotate the nose above the body
for i in range(0, 90):
    time.sleep(0.03)
    ren_win.Render()

    nose_actor.RotateY(-1)

# Put the nose in the head
for i in range(0, 90):
    time.sleep(0.03)
    ren_win.Render()

    nose_actor.RotateZ(1)


time.sleep(5)
