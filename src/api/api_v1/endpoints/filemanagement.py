import os
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src import schemas, controller

router = APIRouter()

#trabaja con varios xml
@router.post("/save_ndata")
async def save_nxml_to_excel(params: schemas.ListaFile):
  # print('parametros del postman')
  # print(params)

  resp = controller.save_n_xml_to_excel(params)
  # value =""
  if resp:
    print('test pass1 success')
    respons = schemas.Response(
      cod_respuesta='1',
      message='el excel se genero de manera correcta. C:/doc_generate/',
      data={})
    estado =status.HTTP_200_OK
    # value='success'
  else:
    print('test pass1 failed')
    # value='failed'
    respons = schemas.Response(
      cod_respuesta='0',
      message='lo sentimos no se pudo realizar el proceso',
      data={})
    estado =status.HTTP_400_BAD_REQUEST

  return JSONResponse(content=respons.__dict__, status_code=estado)

  # return JSONResponse(content=value, status_code=200)

#trabaja con varios xml desde una carpeta de windows
@router.get("/save_ndatafromfolder")
async def savefolder_nxml_to_excel():
  # params = {}
  lista_doc = []
  path = 'C:\\file_input\\'
  print(path)
  # r=root d=directories, f=files
  for r,d,f in os.walk(path):
    for file in f:
      if '.xml' in file:
        lista_doc.append(file) #llenar un listado con los nombres de los archivos

  if len(lista_doc)>0:

    resp = controller.save_folder_to_excel(lista_doc,path)
    # print(lista_doc)
    # value =""
    respons = schemas.Response(
      cod_respuesta='1',
      message='el excel se genero de manera correcta. C:/file_output/',
      data={})
    estado =status.HTTP_200_OK

    if resp:
      print('Success. archivo creado en la ruta C:/file_output')
      #eliminar los archivos tratados.
      for l in lista_doc:
        os.remove(path+l)

    return JSONResponse(content=respons.__dict__, status_code=estado)
  else:
    print('Error. la carpeta C:/file_input esta vacia')
    respons = schemas.Response(
      cod_respuesta='0',
      message='la carpeta C:/file_input esta vacia',
      data={})
    estado =status.HTTP_400_BAD_REQUEST
    return JSONResponse(content=respons.__dict__, status_code=estado)
  # return JSONResponse(content=value, status_code=200)