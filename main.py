import pandas as pd
#voy a organizar los datos
tabla1= pd.read_csv("./data/empleados.csv")

from data.comidas import comidas
tabla2= pd.DataFrame(comidas,columns=['nombrePlato','precio Unitario'])

from data.medicos import crearMedicos
medicos = crearMedicos()
tabla3 = pd.DataFrame(medicos)

print (tabla1)
print ("/n")
print (tabla2)
print ("/n")
print (tabla3)

#head es para mostrar los  primeros  datos
#tail es para mostrar los ultimos datos
#mostrar los datos  especificos
#tabla1Modificada = tabla1[['nombres','salario']].head(50)
#print (tabla1Modificada)

#tabla2Modificada =tabla2
#print(tabla2Modificada)
