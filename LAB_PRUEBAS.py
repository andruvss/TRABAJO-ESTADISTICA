import pandas as pd
import matplotlib.pyplot as plt

#Análisis descriptivo <ITEM I>

"""
La población de estudio son alumnos que esten cursando 
alguna carrera en institutos en todas las provincias de chile.
"""

#Variables

"""

Género:

Edad:

Rango Edad:

Año Ingreso:

Semestre Ingreso:

Tipo de Institución: Se trata de una variable CUALITATIVA ORDINAL ya que existe una jerarquía
            academica entre los institutos o centros de formacion con respecto a las universidades.

Nombre Institución:

Acreditadción Institucional:

Periodo de Acreditación:

Años de Acreditación:

Nombre Carrera:

Requisito Ingreso:

Via de Ingreso:

Modalidad:

Jornada:

Tipo Plan Carrera:

Nivel de Estudio Carrera:

Area Conocimiento: Se trata de una variable CUALITATIVA NOMINAL, esto se debe a que en un instituto
                no hay una carrera que sea mas importante o se encuentre sobre otra, no vemos una jerarquía.

Duración Plan de Estudio(Semestre):

Duración Proceso Titulación(Semestre):

Duración Total Carrera(Semestre):

Valor Matrícula(Pesos): Se trata de una variable CUANTITATIVA CONTINUA, ya que vemos claramente un rango de
                    valores, se repiten pero no son todos identicos.

Valor Arancel(Pesos): Se trata nuevamente de una variable CUANTITATIVA CONTINUA, ya que vemos claramente un rango de
                    valores, se repiten pero no son todos identicos.

Región Sede:

Provincia Sede:

Comuna Sede:


"""

#Desarrollo de las preguntas <ITEM II>

#°1
"Aquí leemos el archivo excel"
df_1 =  pd.read_excel('BLOQUE 4.xlsx')

"Con el definimos la muestra de la tabla"
muestra_1 = df_1.shape[0]

"Calculamos la frecuencia de cada carrera"

tabla_1 = df_1[['AREA CONOCIMIENTO', 'VALOR ARANCEL (PESOS)']].s
print(tabla_1)

"Calculamos la frecuencia de "