
# ACTUALIZANDO DATOS


#1. Actualizando un solo valor del atributo del documento

#    name: 'laptop' = nombre del atributo con su valor actual
#    '$set':{name: 'keyboard' = valor del atributo por el cual se va a reemplazar
#    'price': 300 = nuevo atributo que se le esta agregando a nuestro documento

'''
collection.update_one({'name': 'laptop'}, {'$set':{'name': 'keyboard', 'price': 300}})
'''







#2. Actualizando un solo valor, en este caso incrementamos en 30
#   al atributo 'price', del valor que este + 30

#inc = incrementa el valor del atributo especificado

'''
collection.update_one({'name': 'keyboard'}, {'$inc':{'price': 30}})
'''