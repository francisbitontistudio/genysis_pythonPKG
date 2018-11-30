import requests
import json
import ast

token = ""

def cylindricalProjection(target,resolution,height,output,center,range,startDir,rotateAxis):
    url ="https://studiobitonti.appspot.com/cylindricalProjection"
    payload = {"target":target,"center":center,"resolution":resolution,"range":range,"rotateAxis":rotateAxis,"start_dir":startDir,"height":height,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def sphericalProjection(target,center,resolution,range,rotateAxis,output):
    url ="https://studiobitonti.appspot.com/sphericalProjection"
    payload = {"target":target,"center":center,"resolution":resolution,"range":range,"rotateAxis":rotateAxis,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def planarProjection(target,center,direction,size,resolution,output):
    url ="https://studiobitonti.appspot.com/planeProjection"
    payload = {"target":target,"center":center,"direction": direction,"size":size,"resolution":resolution,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

#error
def boolean(input1,input2,output,operation): #operations are Union, Interset and Difference
    url ="https://studiobitonti.appspot.com/boolean"
    payload = {"input1":input1,"input2":input2,"output":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def convexHull(a):
    url ="https://studiobitonti.appspot.com/convexHull"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def voronoi(a):
    url ="https://studiobitonti.appspot.com/voronoi"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def delaunay(a):
    url ="https://studiobitonti.appspot.com/delaunay"
    payload = {"points":a,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def blend(compA,compB,value,output):
    url ="https://studiobitonti.appspot.com/blend"
    payload = {"compA":compA,"compB":compB,"value":value,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

#not working Li will check backend
def meshSplit(target,output):
    url ="https://studiobitonti.appspot.com/meshSplit"
    payload = {"target":target,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def meshReduce(target,output,portion):
    url ="https://studiobitonti.appspot.com/meshreduction"
    payload = {"target":target,"portion":portion,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

def genLatticeUnit(case,chamfer,centerChamfer,bendIn,cBendIn,connectPt,output):
# Case: Is an integer value between 0 - 7,  defining different type of lattice units.
# Chamfer: Is a float value between 0 to 0.5 defining the angle of chamfer of the corners.
# Center Chamfer: Is a float value between 0 to 0.5 defining the angle of chamfer from the center.
# Bendln: Is a float value between 0 and 1, defining angle bend of the lines.
# cBendln:  Is a float value between 0 and 1,defining the central bend of the lines.
# Connect Pt:  Is a float value between 0 and 1, defining the connection points.
    url = "https://studiobitonti.appspot.com/latticeUnit"
    payload = {"case":case,"chamfer":chamfer,"centerChamfer":centerChamfer,"bendIn":bendIn,"cBendIn":cBendIn,"connectPt":connectPt,"filename":output,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text


def parseComponents(a):
    bodyMain=""
    for i in range(len(a)):
        body="{\"component\":\"%s\",\"attractor\":{\"point\":%s,\"range\":%s}}" % (a[i][0],a[i][1],a[i][2])
        if(i>0):
            bodyMain+=","+body
        else:
            bodyMain+=body
    final="\"blendTargets\":["+bodyMain+"]}"
    return final

def marchingCube(lines,resolution,memberThickness,filename):

    url = "https://studiobitonti.appspot.com/marchingCube"
    payload = {"lines":lines,"resolution":resolution,"memberThickness":memberThickness,"filename":filename,"t":token}
    print(json.dumps(payload))
    r = requests.post(url,json=payload)
    return r.text

class volumeLattice:
    def __init__(self): #set global variables
        #URL is always this.
        #self.url = "https://studiobitonti.appspot.com/stochasticLattice"
        self.url = "https://studiobitonti.appspot.com/volumeLattice"
        self.urlStochastic = "https://studiobitonti.appspot.com/stochasticLattice"
        #variables that need to be set by the user.
        self.poreSize=.02
        self.volume=""
        self.output=""
        self.component="unit_1.obj"
        self.componentSize=1
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]

#functions for seting key variables

    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def setOutput(self,output):#file name that you want to save out
        self.output=output
    def setVolume(self,volume):#base surface
        self.volume=volume
    def setPoreSize(self,pore):#pore size for stochastic Lattice
        self.poreSize=pore
    def setComponentSize(self,cellHeight):#size of componet in a static or graded grid
        self.componentSize=cellHeight

#lattice generation functions

    def stochasticLatticeStatic(self):
        payload = {"volume":self.volume,"poreSize":self.poreSize,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.urlStochastic,json=payload)
        print(r.text)
        return r.text

    def volumeLatticeStatic(self):
        payload = {"component":self.component,"volume":self.volume,"componentSize":self.componentSize,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

    def volumeLatticeAttractor(self):
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"volume\":\"%s\",\"componentSize\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.volume,self.componentSize,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

class surfaceLattice:
    def __init__(self): #set global variables
        #URL is always this.
        self.url = "https://studiobitonti.appspot.com/surfaceLattice"
        #Always True
        self.autoScale="true"
        self.ESIPLON=1
        self.bin="true"
        #variables that need to be set by the user.
        self.output = "twoSurfaceLattice_attractor_output.obj"
        self.cellHeight=1
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]
        self.component="unit_1.obj"
        self.base="Base_Surface.obj"
        self.ceil="Ciel_CompB.obj"

#functions for seting key variables

    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def setBin(self,bin):
        self.bin=bin
    def setEspilon(self,espilon):
        self.ESIPLON=espilon
    def setOutput(self,output):#file name that you want to save out
        self.output=output
    def setSurface(self,base):#base surface
        self.base=base
    def setTopSurface(self,ceil):#Top surface
        self.ceil=ceil
    def setCellHeight(self,cellHeight):#if no top surface is defined set a cell height. Else it will be set to 1
        self.cellHeight=cellHeight

#lattice generation functions

    def twoSurfaceAttractors(self):#Lattice between two surfaces with attractors for blended lattice
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"base\":\"%s\",\"cellHeight\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.base,self.cellHeight,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

    def oneSurfaceLatticeAttractors(self):#Lattice on one surface with a constant offset with attractors for blended lattice
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"component\":\"%s\",\"base\":\"%s\",\"cellHeight\":%s,\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.component,self.base,self.cellHeight,self.output,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.url,json=dict)
        print(r.text)
        return r.text

    def surfaceLatticeStatic(self): #Lattice on one surface with a constant offset
        payload = {"component":self.component,"base":self.base,"cellHeight":self.cellHeight,"filename":self.output,"t":token}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

    def twoSurfaceLatticeStatic(self):#Lattice structure between two surfaces
        payload = {"component":self.component,"base":self.base,"cellHeight":self.cellHeight,"filename":self.output,"t":token,"ceil":self.ceil,"autoScale":self.autoScale,"ESIPLON":self.ESIPLON,"bin":self.bin}
        print(json.dumps(payload))
        #make post request
        r = requests.post(self.url,json=payload)
        print(r.text)
        return r.text

class conformalVolume:
    def __init__(self): #set global variables
        #URL is always this.
        self.urlGrid = "https://studiobitonti.appspot.com/conformalGrid"
        self.urlPopulate = "https://studiobitonti.appspot.com/boxMorph"
        #variables that need to be set by the user.
        self.u=65
        self.v=18
        self.w=3
        self.unitize="true"
        self.export="Board_Lattice.obj"
        self.component="box2.obj"
        self.surfaces="Skate.json"#This will be a JSON file with the surface points organized
        self.gridOutput="Skate_Grid.json"#grid output will be JSON format
        self.boxes=""
        #attactors will be formated as an 2D array "["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]"
        #default values are files included in sample repo.
        self.attractorSet=[["unit_0.obj", [0,0,0], 20], ["unit_1.obj", [4,36,22], 20]]

#functions for seting key variables
    def setAttractor(self,a): #attractors are optional (blended lattices only)
        self.attractorSet=a
    def seUVW(self,u,v,w): #attractors are optional (blended lattices only)
        self.u=u
        self.v=v
        self.w=w
    def setUnitize(self,unitize):
        self.unitize=unitize
    def setComponent(self,unitize):
        self.unitize=unitize
    def setSurfaces(self,surfaces):
        self.surfaces=surfaces
    def setGridOutput(self,gridOutput):#file name that you want to save out
        self.gridOutput=gridOutput

#Generate conformalGrid
    def genGrid(self):
        url ="https://studiobitonti.appspot.com/meshreduction"
        payload = {"u":self.u,"v":self.v,"w":self.w,"unitize":self.unitize,"surfaces":self.surfaces,"filename":self.gridOutput,"t":token}
        self.boxes=self.gridOutput
        print(json.dumps(payload))
        r = requests.post(self.urlGrid,json=payload)
        return r.text

#Populate conformal lattice
    def populateLattice(self):#Lattice on one surface with a constant offset with attractors for blended lattice
        #get attractor information
        att=parseComponents(self.attractorSet)
        payload = "{\"boxes\":\"%s\",\"component\":\"%s\",\"filename\": \"%s\",\"t\":\"%s\",%s" % (self.boxes,self.component,self.export,token,att)
        print(payload)
        #convert paylod to dictionary
        dict=ast.literal_eval(payload)
        #make post request
        r = requests.post(self.urlPopulate,json=dict)
        print(r.text)
        return r.text
