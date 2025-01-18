# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "myPartM"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_myPartM_face1_Fa0_Ctr0():
	P000 = App.Vector(15.0000, 0.0000, 0)
	P001 = App.Vector(22.9111, 5.7279, 0)
	P002 = App.Vector(25.9808, 15.0000, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(16.1228, 6.5961, 0)
	P004 = App.Vector(3.5355, 3.5355, 0)
	S001 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(6.5961, 16.1228, 0)
	P006 = App.Vector(15.0000, 25.9808, 0)
	S002 = Part.Arc(P004, P005, P006)
	P007 = App.Vector(5.7279, 22.9111, 0)
	P008 = App.Vector(0.0000, 15.0000, 0)
	S003 = Part.Arc(P006, P007, P008)
	P009 = App.Vector(-7.2443, 20.8397, 0)
	P010 = App.Vector(-15.0000, 25.9808, 0)
	S004 = Part.Arc(P008, P009, P010)
	P011 = App.Vector(-8.5578, 15.1208, 0)
	P012 = App.Vector(-3.5355, 3.5355, 0)
	S005 = Part.Arc(P010, P011, P012)
	P013 = App.Vector(-15.1208, 8.5578, 0)
	P014 = App.Vector(-25.9808, 15.0000, 0)
	S006 = Part.Arc(P012, P013, P014)
	P015 = App.Vector(-20.8397, 7.2443, 0)
	P016 = App.Vector(-15.0000, 0.0000, 0)
	S007 = Part.Arc(P014, P015, P016)
	P017 = App.Vector(-24.0512, -4.8933, 0)
	P018 = App.Vector(-25.9808, -15.0000, 0)
	S008 = Part.Arc(P016, P017, P018)
	P019 = App.Vector(-15.9795, -6.8765, 0)
	P020 = App.Vector(-3.5355, -3.5355, 0)
	S009 = Part.Arc(P018, P019, P020)
	P021 = App.Vector(-6.8765, -15.9795, 0)
	P022 = App.Vector(-15.0000, -25.9808, 0)
	S010 = Part.Arc(P020, P021, P022)
	P023 = App.Vector(-4.8933, -24.0512, 0)
	P024 = App.Vector(0.0000, -15.0000, 0)
	S011 = Part.Arc(P022, P023, P024)
	P025 = App.Vector(7.2443, -20.8397, 0)
	P026 = App.Vector(15.0000, -25.9808, 0)
	S012 = Part.Arc(P024, P025, P026)
	P027 = App.Vector(8.5578, -15.1208, 0)
	P028 = App.Vector(3.5355, -3.5355, 0)
	S013 = Part.Arc(P026, P027, P028)
	P029 = App.Vector(15.1208, -8.5578, 0)
	P030 = App.Vector(25.9808, -15.0000, 0)
	S014 = Part.Arc(P028, P029, P030)
	P031 = App.Vector(20.8397, -7.2443, 0)
	P032 = App.Vector(15.0000, 0.0000, 0)
	S015 = Part.Arc(P030, P031, P000)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_myPartM_face1_Fa0():
	FC000 = ctr_face_myPartM_face1_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def myPartM_face1():
	FA000 = face_myPartM_face1_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def fex_subpax_myPartM():
	FIG = myPartM_face1()
	VEX = FIG.extrude(App.Vector(0, 0, 1))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_myPartM = fex_subpax_myPartM()

pax_myPartM = subpax_myPartM

pax_myPartM.check()
#pax_myPartM.exportBrep(f"{outFileName}.brep")
#pax_myPartM.exportIges(f"{outFileName}.igs")
#pax_myPartM.exportStep(f"{outFileName}.stp")
pax_myPartM.exportStl(f"{outFileName}.stl")

