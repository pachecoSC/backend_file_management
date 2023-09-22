from fastapi import HTTPException, status
import base64, openpyxl,datetime,uuid
import xml.etree.ElementTree as ET

from pathlib import Path

from src import schemas

# armar datos para el formato
def save_folder_to_excel(list_doc,path):
  try:
    lista_modelos= []
    for l in list_doc:
      modelo_excel = {}
      tree = ET.parse(path+l)
      data = tree.getroot()
      #funcionalidad
      create_dictionary('nombre de archivo',l,modelo_excel)

      for element in data:
        for element1 in data.attrib:
          if(element1 == 'NoCertificado'):
            create_dictionary(element1,data.get(element1),modelo_excel) #guardar datos en un diccionario
          if(element1 == 'Total'):
            create_dictionary(element1,data.get(element1),modelo_excel) #guardar datos en un diccionario
        if element.tag == '{http://www.sat.gob.mx/cfd/4}Emisor':
          for item in element.attrib:
            if(item=='Rfc'):
              create_dictionary(item,element.get(item),modelo_excel) #guardar datos en un diccionario
            if(item=='Nombre'):
              create_dictionary(item,element.get(item),modelo_excel) #guardar datos en un diccionario
        #
        if element.tag == '{http://www.sat.gob.mx/cfd/4}Complemento':
          for item2 in element:
            # if item.get(item) == 'Rfc':
            for item3 in item2.attrib:
              if(item3=='UUID'):
                create_dictionary(item3,item2.get(item3),modelo_excel) #guardar datos en un diccionario
              if(item3=='FechaTimbrado'):
                create_dictionary(item3,item2.get(item3),modelo_excel) #guardar datos en un diccionario
      lista_modelos.append(modelo_excel)
      #fin funcionalidad
    save_to_excel(lista_modelos)

    return True
  except(Exception) as err:
    content = schemas.Response(
      cod_respuesta='0',
      message= 'error: '+ str(err),
      data={}
    )
    raise HTTPException(
      status_code= status.HTTP_400_BAD_REQUEST,
      detail= content.__dict__
    )
  finally:
    print('finalizado')

# metodo para guardar la lista de modelos
def save_n_xml_to_excel(listaf: schemas.ListaFile) -> bool:
  try:
    lista_modelos= []
    # print('parametros de endpoint lista')
    for file in listaf.lista :
      modelo_excel = {}
      create_dictionary('nombre de archivo',file['name_file'],modelo_excel)
      string_64_decode = base64.b64decode(file['content']).decode("utf-8")
      #print(string_64_decode)
      tree = ET.fromstring(string_64_decode,parser=None)
      #inicio obtener datos de manera especifica
      for element in tree:
        print(element.tag)
        for element1 in tree.attrib:
          if(element1 == 'NoCertificado'):
            create_dictionary(element1,tree.get(element1),modelo_excel) #guardar datos en un diccionario
          if(element1 == 'Total'):
            create_dictionary(element1,tree.get(element1),modelo_excel) #guardar datos en un diccionario
        if element.tag == '{http://www.sat.gob.mx/cfd/4}Emisor':
          for item in element.attrib:
            if(item=='Rfc'):
              # print(element.get(item))
              create_dictionary(item,element.get(item),modelo_excel) #guardar datos en un diccionario
            if(item=='Nombre'):
              create_dictionary(item,element.get(item),modelo_excel) #guardar datos en un diccionario
        if element.tag == '{http://www.sat.gob.mx/cfd/4}Complemento':
          for item2 in element:
            print(item2.attrib)
            # if item.get(item) == 'Rfc':
            for item3 in item2.attrib:
              if(item3=='UUID'):
                print(item2.get(item3))
                create_dictionary(item3,item2.get(item3),modelo_excel) #guardar datos en un diccionario
              if(item3=='FechaTimbrado'):
                print(item2.get(item3))
                create_dictionary(item3,item2.get(item3),modelo_excel) #guardar datos en un diccionario
      #fin obtener datos de manera especifica
      # print('modelo de un diccionario')
      # print(modelo_excel)
      lista_modelos.append(modelo_excel)
    #armar un excel con el diccionario.
    save_nxml_to_excel(lista_modelos)
    return True # indica que todo funciona de manera correcta.

  except(Exception) as err:
    content = schemas.Response(
      cod_respuesta='0',
      message= 'error: '+ str(err),
      data={}
    )
    raise HTTPException(
      status_code= status.HTTP_400_BAD_REQUEST,
      detail= content.__dict__
    )
  finally:
    print('fin de save_xml_to_excel')

# metodos locales
def create_dictionary (key:str, value:str, modelo_new:dict):
  modelo_new[key] =value
  return modelo_new

def save_to_excel(data):
  #print(data)
  wb = openpyxl.Workbook() # apertura de un libro
  sheet = wb.active # activamos una hoja
  sheet.title = 'datos_empresas' # renombrar la hoja
  count = 0
  for row in data:
    if count == 0:
      sheet.append(list(row.keys())) #llenar los titulos 1 fila
      count = count + 1
    sheet.append(list(row.values())) # llenar los valores 1 fila
  fecha_actual = datetime.datetime.now().date()
  nombre_ramdom= uuid.uuid1()

  #preguntar si existe carpeta
  Path('C:/file_output').mkdir(exist_ok=True)

  wb.save('C:/file_output/'+str(fecha_actual)+'_'+str(nombre_ramdom)+'.xlsx')
  # wb.save('C:/doc_generate/'+str(fecha_actual)+'_'+str(nombre_ramdom)+'.xlsx')
