import vtk
import time


def create_sphere(center, theta_resolution=50, phi_resolution=50):
    sphere = vtk.vtkSphereSource()
    sphere.SetThetaResolution(theta_resolution)
    sphere.SetPhiResolution(phi_resolution)
    sphere.SetCenter(center[0], center[1], center[2])

    return sphere


def create_cone(center, height, direction, resolution=50):
    cone = vtk.vtkConeSource()
    cone.SetHeight(height)
    cone.SetResolution(resolution)
    cone.SetDirection(direction[0], direction[1], direction[2])
    cone.SetCenter(center[0], center[1], center[2])

    return cone


def create_actor(obj):
    obj_mapper = vtk.vtkPolyDataMapper()
    obj_mapper.SetInputConnection(obj.GetOutputPort())

    obj_actor = vtk.vtkActor()
    obj_actor.SetMapper(obj_mapper)

    return obj_actor


body = create_sphere((3, 0, 0))
head = create_sphere((1, 0, 0))
nose = create_cone((5, 0, 0), 0.3, (0, -1, 0))

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
# renderer.SetViewport(0,0,1,1)


# Create window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)
renWin.SetSize(600, 600)

#
# Now we loop over 360 degreeees and render the cone each time.
#
# for i in range(0,360):
#     time.sleep(0.03)
#
#     renWin.Render()
#     downBody.SetRadius(0.7)
#     upBody.SetRadius(0.5)
#     nose.SetRadius(0.08)
#     ren1.GetActiveCamera().Azimuth(1)
#     ren2.GetActiveCamera().Azimuth(1)

for i in range(0, 180):
    time.sleep(0.03)
    renWin.Render()

    body.SetRadius(0.7)
    head.SetRadius(0.5)
    nose.SetRadius(0.08)

    translator = vtk.vtkTransform()
    translator.Translate(0, 0, 0)
    translator.RotateZ(1)

    head_actor.SetUserTransform(translator)

    # ren2.GetActiveCamera().Pitch(-0.1)
    # ren2.GetActiveCamera().Yaw(0.1)

# #iren
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
#
# #Camera
# style = vtk.vtkInteractorStyleTrackballCamera()
# iren.SetInteractorStyle(style)
#
# #start
# iren.Initialize()
# iren.Start()
