# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "myPartF"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_myPartF_faceCorners_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(190.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(197.0711, 2.9289, 0)
	P003 = App.Vector(200.0000, 10.0000, 0)
	S001 = Part.Arc(P001, P002, P003)
	P004 = App.Vector(200.0000, 100.0000, 0)
	S002 = Part.LineSegment(P003, P004)
	P005 = App.Vector(10.0000, 100.0000, 0)
	S003 = Part.LineSegment(P004, P005)
	P006 = App.Vector(2.9289, 97.0711, 0)
	P007 = App.Vector(0.0000, 90.0000, 0)
	S004 = Part.Arc(P005, P006, P007)
	P008 = App.Vector(0.0000, 0.0000, 0)
	S005 = Part.LineSegment(P007, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_myPartF_faceCorners_Fa0_Ctr1():
	P000 = App.Vector(47.4755, 20.0000, 0)
	P001 = App.Vector(83.3333, 20.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(90.4044, 22.9289, 0)
	P003 = App.Vector(93.3333, 30.0000, 0)
	S001 = Part.Arc(P001, P002, P003)
	P004 = App.Vector(93.3333, 65.8579, 0)
	S002 = Part.LineSegment(P003, P004)
	P005 = App.Vector(93.3333, 80.0000, 0)
	P006 = App.Vector(79.1912, 80.0000, 0)
	S003 = Part.Arc(P004, P005, P006)
	P007 = App.Vector(43.3333, 80.0000, 0)
	S004 = Part.LineSegment(P006, P007)
	P008 = App.Vector(36.2623, 77.0711, 0)
	P009 = App.Vector(33.3333, 70.0000, 0)
	S005 = Part.Arc(P007, P008, P009)
	P010 = App.Vector(33.3333, 34.1421, 0)
	S006 = Part.LineSegment(P009, P010)
	P011 = App.Vector(33.3333, 20.0000, 0)
	P012 = App.Vector(47.4755, 20.0000, 0)
	S007 = Part.Arc(P010, P011, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_myPartF_faceCorners_Fa0_Ctr2():
	P000 = App.Vector(126.6667, 20.0000, 0)
	P001 = App.Vector(166.6667, 20.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(146.6667, 80.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(126.6667, 20.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartF_faceCorners_Fa0():
	FC000 = ctr_face_myPartF_faceCorners_Fa0_Ctr0()
	FC001 = ctr_face_myPartF_faceCorners_Fa0_Ctr1()
	FC002 = ctr_face_myPartF_faceCorners_Fa0_Ctr2()
	rOneFace = FC000.cut([FC001, FC002])
	rOneFace.check()
	return rOneFace

def myPartF_faceCorners():
	FA000 = face_myPartF_faceCorners_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def fex_subpax_myPartF_corners():
	FIG = myPartF_faceCorners()
	VEX = FIG.extrude(App.Vector(0, 0, 50))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_myPartF_corners = fex_subpax_myPartF_corners()

pax_myPartF = subpax_myPartF_corners

pax_myPartF.check()
#pax_myPartF.exportBrep(f"{outFileName}.brep")
#pax_myPartF.exportIges(f"{outFileName}.igs")
#pax_myPartF.exportStep(f"{outFileName}.stp")
pax_myPartF.exportStl(f"{outFileName}.stl")

