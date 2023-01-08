

# LISTANDO DATOS


#1. Listando todos los documentos y recorriendolos mediante un for

'''
results = collection.find()

for r in results:
    print(r)
'''







#2. Mostrando un atributo especifico de nuestra lista de documentos

'''
results = collection.find()

for r in results:
    print(r['name'])
'''