import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre_cliente): 
        clientes = config.model_clientes.select_nombre(nombre_cliente) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self,nombre_cliente):
        formulario = web.input() # almacena los datos del formulario web
        nombre_cliente = formulario['nombre_cliente'] # alamcena el nombre escrito en el input
        apellidos_cliente = formulario['apellidos_cliente'] # almacena el contenido escrito en el input
        tipo_cliente = formulario['tipo_cliente'] # alamcena la marca escrito en el input
        calle_numero = formulario['calle_numero'] # alamcena el precio escrito en el input
        config.model_clientes.update_clientes(nombre_cliente,apellidos_cliente,tipo_cliente,calle_numero)
        raise web.seeother('/clientes') # redirecciona al index


