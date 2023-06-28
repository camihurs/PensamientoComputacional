import unittest
#Las pruebas de cristal asumen que ya hay código escrito.
#Por eso estas pruebas no se escriben antes que el código.

#La diferencia entre las pruebas de Caja Negra y Caja de Cristal
# es que en las pruebas de caja negra se escriben primero los test
# para ayudarnos a implementar nuevo código. En las pruebas de caja
# de cristal se asume que se tiene código escrito y las pruebas se
# escriben para verificar todas las ramificaciones del programa y
# probar todos los diferentes caminos posibles.

#Tenemos que generar dos tests que nos permitan verificar que nuestra
#función se comporta de la manera correcta

def es_mayor_de_edad(edad):

    """Verifica si la persona es mayor de edad

    Returns:
        _Boolean_: True si es mayor de edad, de lo contrario False
    """

    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):

    #Este es el primer test. Las funciones deben iniciar con la palabra "test"
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado,True)#Comparamos resultado contra True, y debe salir OK en la terminal


    #Este es el segundo test
    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado,False)#Aparece en terminal que corrieron los dos test, y OK ambos.

if __name__ == "__main__":
    unittest.main(verbosity=2)#El argumento "verbosity" arroja resultados más completos en la consola.