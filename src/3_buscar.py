
# BUSCANDO DATOS


#1. Buscando por un valor especifico que contiene el atributo de nuestra
#   lista de documentos

#    Aqui estamos buscando todos los documentos que tengan como valor en sus
#    atributos "price = 300"

'''
results = collection.find({"price": 300})
for r in results:
    print(r)
'''








#2. Aqui estamos buscando todos los docuemntos que tengan como valor en sus
#   atributos "name = keybord"

'''
results = collection.find({"name": "keyboard"})
for r in results:
    print(r)
'''










#3. Buscando un objeto en especifico sin necesidad de recorrer un for,
#   aqui me devuelve 1 solo objeto y no una lista

'''
result = collection.find_one({"name": "mouse"})
print(result)
'''


