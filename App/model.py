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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.DataStructures import mapentry as me
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def TaxiInfo():
    chicago={"TotalTaxis":None,"companies":None,"services":None,'TotalCabs':None}

    chicago["TotalTaxis"]={'lista':lt.newList(datastructure='SINGLE_LINKED', cmpfunction=comparetaxiIds),'Total':0}
    chicago['TotalCabs']= m.newMap(20143,maptype='PROBING',loadfactor=0.5,comparefunction=comparecabsIds)
    chicago["companies"]=m.newMap(1019,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=comparecompanies)
    chicago["services"]=m.newMap(1019,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=comparetripsIds)
    return chicago

# Funciones para agregar informacion 

def addcompany(chicago,company):
    """
    añade una compañia al map
    """
    companies=chicago['companies']
    existcompany=m.contains(companies,company)
    #lstcomp=[]
    if existcompany:
        entry=m.get(companies,company)
        data=me.getValue(entry)
    else:
        data=newcompany(company)
        #lstcomp.append({"name":data['name'],'numtaxis':data['totaltaxis']})   
        #data["totaltaxis"] +=1 
        m.put(companies,company,data)
        #print(lstcomp)
    data['services'] +=1
    
    
    

def addtaxis(chicago,taxi):
    """
    añade el id del taxi a la lista
    """
    lst=chicago["TotalTaxis"]['lista']
    exist=lt.isPresent(lst,taxi)
    if exist == 0:
        lt.addLast(lst, taxi)
    chicago["TotalTaxis"]['Total'] =lt.size(lst)
    return lst , print(chicago["TotalTaxis"]['Total'])

def newcompany(companyname):
    company={'name':'','taxis':None,'totaltaxis':0,'services':0}
    company['name']=companyname
    company['taxis']= m.newMap(32,maptype='PROBING',loadfactor=0.5,comparefunction=comparecabsIds)
    company['totaltaxis']=m.size(company['taxis'])

    return company

def newTaxi(taxiId):
    taxi={'id':'','trips':0}
    taxi['id']=taxiId
    return taxi

def addtaxi_to_company(chicago,company,taxiId):
    companies=chicago['companies']
    info=m.get(companies,company)
    companytaxis= me.getValue(info)['taxis']
    existtaxi=m.contains(companytaxis,taxiId)
    if existtaxi:
            entry = m.get(companytaxis,taxiId)
            data = me.getValue(entry)       
    else:
            data=newTaxi(taxiId)
            m.put(companytaxis,taxiId,data)
            me.getValue(info)['totaltaxis'] +=1 
    data['trips'] +=1

def addtaxi(chicago,taxiId):
    """
    añade una compañia al map
    """
    Cabs=chicago['TotalCabs']
    existcab=m.contains(Cabs,taxiId)
    if existcab:
        entry=m.get(Cabs,taxiId)
        data=me.getValue(entry)
    else:
        data=newTaxi(taxiId)
        m.put(Cabs,taxiId,data)
    

        


    

# ==============================
# Funciones de consulta
# ==============================

def totaltax(chicago):
    num=m.size(chicago['TotalCabs'])
    return num

def totaltaxi(chicago):
    num=chicago['TotalTaxis']['Total']
    return num

def totalcomp(chicago):
    num=m.size(chicago['companies'])
    return num

def topcompaniesByTaxis(chicago):
    companies=m.keySet(chicago['companies'])
    lst=[]
    top={'name':[],'info':[]}
    iterator=it.newIterator(companies)
    while it.hasNext(iterator):
        info=it.next(iterator)
        data=m.get(chicago['companies'],info)
        top['name'].append(info)
        top['info'].append(data['value']['services'])
    return print(top) 

def topcompaniesByservices(chicago):
    companies=m.keySet(chicago['companies'])
    lst=[]
    top={'name':[],'info':[]}
    iterator=it.newIterator(companies)
    while it.hasNext(iterator):
        info=it.next(iterator)
        data=m.get(chicago['companies'],info)
        top['name'].append(info)
        top['info'].append(data['value']['services'])
    lst.append(top)
    return print(top )




# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================

def comparecompanies(keyname,company):
    companyentry=me.getKey(company)
    if (keyname == companyentry) :
        return 0
    elif (keyname > companyentry) :
        return 1
    else:
        return -1

def comparetaxiIds(id1,id2):
    """
    Compara dos Ids de taxis. 
    """
    if (id == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1

def comparecabsIds(keyid,id):
    identry= me.getKey(id)
    if (keyid == identry) :
        return 0
    elif (keyid > identry):
        return 1
    else:
        return -1
    
def comparetripsIds(id1,id2):
    """
    Compara dos Ids de taxis. 
    """
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1