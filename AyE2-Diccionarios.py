infoDict = {"nombre":"Eduardo","apellido":"Sanchez","edad":20}
print "Nombre:\t\t",infoDict["nombre"]
print "Apellido:\t", infoDict["apellido"]
print "Edad:\t\t", infoDict["edad"]

infoDict.update({"ciudadNacimiento":"Valencia"})

print "\nAnadido Ciudad De Nacimiento\n"
print "Nombre:\t\t",infoDict["nombre"]
print "Apellido:\t", infoDict["apellido"]
print "Edad:\t\t", infoDict["edad"]
print "Nacimiento:\t", infoDict["ciudadNacimiento"]