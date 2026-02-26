
from conexionBD import ConexionBD


class XeradorAlbaran:
    """Clase para xerar albaráns en formato PDF desde a base de datos"""

    def __init__(self, ruta_bd):
        """Inicializa o xerador de albaráns.

        :param ruta_bd: str da ruta da base de datos
        """

        self.ruta_bd = ruta_bd




    def obter_cabeceira_albara(self, numero_albara):
        """Obtén os datos da cabeceira do albará da base de datos.

        Dado un número de albará, retorna unha lista con numeroAlbaran, numeroClente, nomeCliente, apelidosCliente,
        dataAlbaran, dataEntrega.

        :param numero_albara:
        :return datosCabeceira: list | None
        """

        # Conectar á base de datos
        conexion = ConexionBD(self.ruta_bd)
        conexion.conectaBD()
        conexion.creaCursor()

        # Consulta SQL para os datos principais do albarán
        consulta_albaran = """
            SELECT v.numeroAlbaran, v.numeroCliente, c.nomeCliente, c.apelidosCliente, 
                   v.dataAlbaran, v.dataEntrega 
            FROM ventas v 
            INNER JOIN clientes c ON v.numeroCliente = c.numeroCliente 
            WHERE v.numeroAlbaran = ?
        """

        # Executar consulta
        resultado_albaran = conexion.consultaConParametros(consulta_albaran, numero_albara)

        if not resultado_albaran or len(resultado_albaran) == 0:
            print(f"Non se atopou o albarán número {numero_albara}")
            conexion.pechaBD()
            return None

        # Pechar base de datos
        conexion.pechaBD()
        # Obter primeira (e única) fila
        datosCabeceira = resultado_albaran[0]
        return datosCabeceira

    def obter_detalle_albara(self, numero_albara):
        """Obtén os datos do corpo do albará da base de datos.

           Dado un número de albará, retorna unha lista coas liñas que forman o corpo do albará. En cada liña ven
           representada por unha lista onde aparecen os datos codigoProducto, nomeProducto, cantidade,
           prezoUnitario.

           :param numero_albara:
           :return linhas: list | None
           """

        # Conectar á base de datos
        conexion = ConexionBD(self.ruta_bd)
        conexion.conectaBD()
        conexion.creaCursor()
        # Consulta SQL para as liñas do albarán
        consulta_linhas = """
        SELECT 
            dv.codigoProducto,
            p.nomeProducto,
            dv.cantidade,
            dv.prezoUnitario
        FROM detalleVentas dv
        INNER JOIN productos p ON TRIM(dv.codigoProducto) = TRIM(p.codigoProducto)
        WHERE dv.numeroAlbaran = ?
        ORDER BY dv.numeroLinhaAlbaran
        """

        # Executar consulta de liñas
        linhas = conexion.consultaConParametros(consulta_linhas, numero_albara)

        if not linhas or len(linhas) == 0:
            print(f"Non se atopou o datos para o corpo do albará número {numero_albara}")
            conexion.pechaBD()
            return None

        # Pechar base de datos
        conexion.pechaBD()
        return linhas





if __name__ == "__main__":
   x = XeradorAlbaran("modelosClasicos.dat")
   print (x.obter_cabeceira_albara(1))
   print (x.obter_detalle_albara(10))
