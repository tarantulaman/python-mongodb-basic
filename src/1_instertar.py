
# INSERTANDO DATOS



#1. Insertando 1 solo documento a nuestra coleccion

'''
collection.insert_one({"name": "keyboard", "price": 300})
'''











#2. Insertando varios documentos a nuestra coleccion

#   Creando varios documentos para insertarlos

'''
product_one = {"name": "mouse"}
product_two = {"name": "monitor"}
'''

#   Insertando los documentos creados

'''
collection.insert_many([product_one, product_two])
'''