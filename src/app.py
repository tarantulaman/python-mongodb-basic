
#IMPORTANDO MODULOS

#LLamando al modulo MongoClient
#MongoClient = se esta llamando a todas las funcionalidades de MongoClient
from pymongo import MongoClient











# CONECTANDO A MONGODB


# Estableciendo la cadena de coneccion de MongoDB

#MONGO_URI = variable que almacena la direccion de mongodb
MONGO_URI = 'mongodb://localhost'




# Creando una variable que almacene mi cadena de conexion

#MongoClient = Para conectarme mediante su url

#cliet = objeto que almacenara mi conexin
client = MongoClient(MONGO_URI)




# Creando la base de datos

#En este caso no existe la base de datos pero mongo la crea automaticamente
db = client['teststore']

















# CREANDO LA COLECCION DE DATOS

#Creaando una coleccion de datos y almacanando en una varible

collection = db['products']












# AQUI EL CODIGO DE NUESTROS ARCHIVOS











