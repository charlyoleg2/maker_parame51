# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "myPartP"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_myPartP_face1_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(300.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(300.0000, 180.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 180.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartP_face1_Fa0():
	FC000 = ctr_face_myPartP_face1_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_myPartP_face1_Fa1_Ctr0():
	P000 = App.Vector(30.0000, 45.0000, 0)
	P001 = App.Vector(90.0000, 45.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(70.0000, 75.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(60.0000, 101.1803, 0)
	P004 = App.Vector(50.0000, 75.0000, 0)
	S002 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(30.0000, 45.0000, 0)
	S003 = Part.LineSegment(P004, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartP_face1_Fa1():
	FC000 = ctr_face_myPartP_face1_Fa1_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_myPartP_face1_Fa2_Ctr0():
	P000 = App.Vector(120.0000, 45.0000, 0)
	P001 = App.Vector(150.0000, 45.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(140.0000, 75.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(135.0000, 134.5804, 0)
	P004 = App.Vector(130.0000, 75.0000, 0)
	S002 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(120.0000, 45.0000, 0)
	S003 = Part.LineSegment(P004, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartP_face1_Fa2():
	FC000 = ctr_face_myPartP_face1_Fa2_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_myPartP_face1_Fa3_Ctr0():
	P000 = App.Vector(210.0000, 45.0000, 0)
	P001 = App.Vector(240.0000, 45.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(230.0000, 105.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(225.0000, 134.1421, 0)
	P004 = App.Vector(220.0000, 105.0000, 0)
	S002 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(210.0000, 45.0000, 0)
	S003 = Part.LineSegment(P004, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartP_face1_Fa3():
	FC000 = ctr_face_myPartP_face1_Fa3_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def myPartP_face1():
	FA000 = face_myPartP_face1_Fa0()
	FA001 = face_myPartP_face1_Fa1()
	FA002 = face_myPartP_face1_Fa2()
	FA003 = face_myPartP_face1_Fa3()
	rOneFig = FA000.fuse([FA001, FA002, FA003])
	rOneFig.check()
	return rOneFig

def fex_subpax_myPartP():
	FIG = myPartP_face1()
	VEX = FIG.extrude(App.Vector(0, 0, 1))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_myPartP = fex_subpax_myPartP()

pax_myPartP = subpax_myPartP

pax_myPartP.check()
#pax_myPartP.exportBrep(f"{outFileName}.brep")
#pax_myPartP.exportIges(f"{outFileName}.igs")
#pax_myPartP.exportStep(f"{outFileName}.stp")
pax_myPartP.exportStl(f"{outFileName}.stl")

