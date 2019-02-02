import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre_cliente = formulario['nombre_cliente'] # alamcena el nombre escrito en el input
        apellidos_cliente = formulario['apellidos_cliente'] # almacena el contenido escrito en el input
        tipo_cliente = formulario['tipo_cliente'] # alamcena la marca escrito en el input
        calle_numero =formulario['calle_numero'] # alamcena el precio escrito en el input
        config.model_clientes.insert_clientes(nombre_cliente,apellidos_cliente,tipo_cliente,calle_numero) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/clientes') # redirecciona al index.html
