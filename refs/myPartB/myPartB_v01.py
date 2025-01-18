# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "myPartB"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_myPartB_faceFront_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(25.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_myPartB_faceFront_Fa0_Ctr1():
	P000 = App.Vector(-10.0000, -10.0000, 0)
	P001 = App.Vector(10.0000, -10.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(10.0000, 10.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-10.0000, 10.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-10.0000, -10.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartB_faceFront_Fa0():
	FC000 = ctr_face_myPartB_faceFront_Fa0_Ctr0()
	FC001 = ctr_face_myPartB_faceFront_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def myPartB_faceFront():
	FA000 = face_myPartB_faceFront_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def myPartB_faceSide():
	rOneFig = undefined
	rOneFig.check()
	return rOneFig

def fex_subpax_myPartB():
	FIG = myPartB_faceFront()
	VEX = FIG.extrude(App.Vector(0, 0, 60))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_myPartB = fex_subpax_myPartB()

pax_myPartB = subpax_myPartB

pax_myPartB.check()
#pax_myPartB.exportBrep(f"{outFileName}.brep")
#pax_myPartB.exportIges(f"{outFileName}.igs")
#pax_myPartB.exportStep(f"{outFileName}.stp")
pax_myPartB.exportStl(f"{outFileName}.stl")

