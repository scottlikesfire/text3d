
# author: Scott Sorensen
# Date Aug 26 2017
def writeOBJ(filename, vertices, faces,vertexNormals = [],textureCoords=[]):
    with open(filename, 'w') as f:
        f.write("# OBJ file\n")
        f.write("mtllib tempMat.mtl\n")
        for v in vertices:
            f.write("v")
            for i in v:
                f.write(" %f" % i)
            f.write("\n")
        for vt in textureCoords:
            f.write("vt")
            for i in vt:
                f.write(" %f" % i)
            f.write("\n")
        for vt in textureCoords:
            f.write("vt %f" %(vt[0]+1.0))
            f.write(" %f \n" %(vt[1]))
        facesStr = genFaceString(textureCoords,faces)
        f.write(facesStr)
        #for p in faces:
            #f.write("f")
            #faceStr = genFaceString
            #for i in p:
            #    f.write(" %d" % (i + 1))
            #    f.write("/%d" % (i + 1))
            #f.write("\n")
        for vn in vertexNormals:
            f.write("vn")
            for i in vn:
                f.write(" %f" % i)
            f.write("\n")

def genFaceString(vt,faces):
    facesStr = ""
    #print("vt size is " +str(len(vt)))
    numVerts = len(vt)
    for f in faces:
        #print("f is " + str(f[0]) + " " + str(f[1]) + " " + str(f[2]))
        fstr = "f "
        vt0 = vt[f[0]]
        vt1 = vt[f[1]]
        vt2 = vt[f[2]]
        if detectCrossover(vt0,vt1,vt2):
            tf = correctCrossover(f,vt0,vt1,vt2, numVerts)
            fstr = fstr + tf 
        else:
            for f_ind in f:
                fstr = fstr + str(f_ind + 1) +"/" + str(f_ind +1 ) + " "
        facesStr = facesStr + fstr + "\n"
    return facesStr
        

def detectCrossover(vt0,vt1,vt2):
    u0 = vt0[0]
    u1 = vt1[0]
    u2 = vt2[0]
    if abs(u0-u1) > .5 or (abs(u1-u2)>.5 or abs(u0-u2) >.5):
        return True
    else:
        return False

def correctCrossover(f,vt0,vt1,vt2,numVerts):
    fstr = str(f[0] + 1)
    if vt0[0] < .5:
        fstr = fstr + "/" + str(f[0]+numVerts + 1)
    else:
        fstr = fstr + "/" + str(f[0]+1)

    fstr = fstr + " " + str(f[1]+1)
    if vt1[0] < .5:
         fstr = fstr + "/" + str(f[1]+numVerts+1)
    else:
        fstr = fstr + "/" + str(f[1]+1)

    fstr = fstr + " " + str(f[2]+1)
    if vt2[0] < .5:
         fstr = fstr + "/" + str(f[2]+numVerts+1)
    else:
        fstr = fstr + "/" + str(f[2]+1)
    return fstr

#def writeOBJWithMat(directory,filename, vertices, faces,,textureCoords,):