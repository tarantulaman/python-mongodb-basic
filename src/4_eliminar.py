
# ELIMINANDO DATOS


#1. Eliminando a multiples documentos

'''
collection.delete_many({"price": 300})
'''




#2. Eliminando un documento en especifico

'''
collection.delete_one({"name": "monitor"})
'''





#3. Eliminando todos los  documentos de mi coleccion

'''
collection.delete_many({}) 
'''