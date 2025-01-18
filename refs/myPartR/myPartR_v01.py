# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "myPartR"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_myPartR_faceDress_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(45.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(27.7230, 68.9604, 0)
	P003 = App.Vector(25.0000, 140.0000, 0)
	S001 = Part.Arc(P001, P002, P003)
	P004 = App.Vector(62.1572, 106.5435, 0)
	S002 = Part.LineSegment(P003, P004)
	P005 = App.Vector(69.2283, 113.6145, 0)
	S003 = Part.LineSegment(P004, P005)
	P006 = App.Vector(29.1411, 155.4548, 0)
	S004 = Part.LineSegment(P005, P006)
	P007 = App.Vector(15.0000, 161.0000, 0)
	S005 = Part.LineSegment(P006, P007)
	P008 = App.Vector(10.5000, 147.0000, 0)
	S006 = Part.LineSegment(P007, P008)
	P009 = App.Vector(0.0000, 141.0000, 0)
	S007 = Part.LineSegment(P008, P009)
	P010 = App.Vector(-10.5000, 147.0000, 0)
	S008 = Part.LineSegment(P009, P010)
	P011 = App.Vector(-15.0000, 161.0000, 0)
	S009 = Part.LineSegment(P010, P011)
	P012 = App.Vector(-29.1411, 155.4548, 0)
	S010 = Part.LineSegment(P011, P012)
	P013 = App.Vector(-65.5276, 109.9138, 0)
	S011 = Part.LineSegment(P012, P013)
	P014 = App.Vector(-58.4565, 102.8428, 0)
	S012 = Part.LineSegment(P013, P014)
	P015 = App.Vector(-25.0000, 140.0000, 0)
	S013 = Part.LineSegment(P014, P015)
	P016 = App.Vector(-27.7230, 68.9604, 0)
	P017 = App.Vector(-45.0000, 0.0000, 0)
	S014 = Part.Arc(P015, P016, P017)
	P018 = App.Vector(0.0000, 0.0000, 0)
	S015 = Part.LineSegment(P017, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartR_faceDress_Fa0():
	FC000 = ctr_face_myPartR_faceDress_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def myPartR_faceDress():
	FA000 = face_myPartR_faceDress_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_myPartR_faceShort_Fa0_Ctr0():
	P000 = App.Vector(25.0000, 0.0000, 0)
	P001 = App.Vector(31.9459, -39.3923, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(4.3713, -44.2545, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, -25.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-4.3713, -44.2545, 0)
	S003 = Part.LineSegment(P003, P004)
	P005 = App.Vector(-31.9459, -39.3923, 0)
	S004 = Part.LineSegment(P004, P005)
	P006 = App.Vector(-25.0000, 0.0000, 0)
	S005 = Part.LineSegment(P005, P006)
	P007 = App.Vector(25.0000, 0.0000, 0)
	S006 = Part.LineSegment(P006, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartR_faceShort_Fa0():
	FC000 = ctr_face_myPartR_faceShort_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def myPartR_faceShort():
	FA000 = face_myPartR_faceShort_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig


pax_myPartR.check()
#pax_myPartR.exportBrep(f"{outFileName}.brep")
#pax_myPartR.exportIges(f"{outFileName}.igs")
#pax_myPartR.exportStep(f"{outFileName}.stp")
pax_myPartR.exportStl(f"{outFileName}.stl")

