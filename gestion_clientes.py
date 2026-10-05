#clase que representa la informacion de un cliente 
class GestionClientes:

#Constructor : Inicializa los datos del cliente 
    def __init__(
            self,
            identificacion,
            nombreCompleto, 
            genero, 
            tipoMenu, 
            numeroSesiones, 
            fechaRegistro, 
            costoPorSesion
    ):

        self.identificacion = identificacion
        self.nombreCompleto = nombreCompleto
        self.genero = genero
        self.tipoMenu = tipoMenu
        self.numeroSesiones = numeroSesiones
        self.fechaRegistro = fechaRegistro
        self.costoPorSesion = costoPorSesion

# Metodo para calcular el costo total
    def calcularCostoTotal(self):
        return self.numeroSesiones * self.costoPorSesion