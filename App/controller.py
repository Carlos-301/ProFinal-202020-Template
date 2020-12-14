"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
from App import model as mod
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    catalog = mod.TaxiInfo()
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(catalog, taxisfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    taxisfile = cf.data_dir + taxisfile
    input_file = csv.DictReader(open(taxisfile, encoding="utf-8"),delimiter=",")
    for trip in input_file:
        company=trip['company']
        taxiId=trip['taxi_id']
        if company == '':
            company = "Independent Owner"

        #mod.addtaxis(catalog,trip['taxi_id'])
        mod.addcompany(catalog,company)
        mod.addtaxi_to_company(catalog,company,taxiId)
        mod.addtaxi(catalog,taxiId)
    return catalog

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def totaltax(catalog):
    return mod.totaltax(catalog)

def totalcomp(catalog):
    return mod.totalcomp(catalog)

def totaltaxi(catalog):
    return mod.totaltaxi(catalog)

def topcompaniesByTaxis(catalog):
    return mod.topcompaniesByTaxis(catalog)

def topcompaniesByservices(catalog):
    return mod.topcompaniesByservices(catalog)