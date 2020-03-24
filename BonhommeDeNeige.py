import vtk
import time




#Creation de la première grosse sphère
downBody = vtk.vtkSphereSource()
downBody.SetRadius(20)

#Creation du mapping
downBodyMapper = vtk.vtkPolyDataMapper()
downBodyMapper.SetInputConnection(downBody.GetOutputPort())

#Creation de l'acteur
downBodyActor = vtk.vtkActor()
downBodyActor.SetMapper(downBodyMapper)
downBodyActor.GetProperty().SetColor(1, 1, 1)
downBodyActor.GetProperty().SetDiffuse(0.7)
downBodyActor.GetProperty().SetSpecular(0.4)


#Creation du renderer
ren1 = vtk.vtkRenderer()
ren1.AddActor(downBodyActor)
ren1.SetBackground(0.1, 0.1, 0.1)

#Creation du rendererWindow
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(600, 600)


#
# Now we loop over 360 degreeees and render the cone each time.
#
for i in range(0,360):
    time.sleep(0.03)

    renWin.Render()
    ren1.GetActiveCamera().Azimuth( 1 )



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