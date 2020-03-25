import vtk
import time




#Creation de la première grosse sphère
downBody = vtk.vtkSphereSource()
downBody.SetThetaResolution(50)
downBody.SetCenter(3,0,0)
downBody.SetPhiResolution(50)

#Creation de la deuxieme sphère
upBody = vtk.vtkSphereSource()
upBody.SetThetaResolution(50)
upBody.SetCenter(1,0,0)
upBody.SetPhiResolution(50)

#Creation du nez
nose = vtk.vtkConeSource()
nose.SetHeight(0.3)
nose.SetResolution(50)
nose.SetCenter(5,0,0)
nose.SetDirection(0,-1,0)



#Creation du mapping
downBodyMapper = vtk.vtkPolyDataMapper()
downBodyMapper.SetInputConnection(downBody.GetOutputPort())

upBodyMapper = vtk.vtkPolyDataMapper()
upBodyMapper.SetInputConnection(upBody.GetOutputPort())

noseMapper = vtk.vtkPolyDataMapper()
noseMapper.SetInputConnection(nose.GetOutputPort())

#Creation de l'acteur
downBodyActor = vtk.vtkActor()
downBodyActor.SetMapper(downBodyMapper)

upBodyActor = vtk.vtkActor()
upBodyActor.SetMapper(upBodyMapper)

noseActor = vtk.vtkActor()
noseActor.SetMapper(noseMapper)
noseActor.GetProperty().SetColor(1, 0.741, 0)

#Creation du renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(downBodyActor)
renderer.AddActor(upBodyActor)
renderer.AddActor(noseActor)
renderer.SetBackground(0.1,0.1,0.1)
#renderer.SetViewport(0,0,1,1)


#Creation du rendererWindow
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

for i in range(0,180):
    time.sleep(0.03)
    renWin.Render()

    downBody.SetRadius(0.7)
    upBody.SetRadius(0.5)
    nose.SetRadius(0.08)

    translator = vtk.vtkTransform()
    translator.Translate(0, 0, 0)
    translator.RotateZ(1)

    upBodyActor.SetUserTransform(translator)

    #ren2.GetActiveCamera().Pitch(-0.1)
    #ren2.GetActiveCamera().Yaw(0.1)


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