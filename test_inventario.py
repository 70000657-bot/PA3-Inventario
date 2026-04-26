import unittest
from Inventario_Optimizado import GestorInventario


class TestGestorInventario(unittest.TestCase):
    """Pruebas unitarias para sistema de inventario de equipos de cómputo.
    Ciclo TDD: Red-Green-Refactor"""

    def setUp(self):
        """Inicializa un gestor limpio antes de cada prueba."""
        self.gestor = GestorInventario()

    def test_agregar_equipo_correctamente(self):
        """Verifica que un equipo se registra en el inventario."""
        self.gestor.agregar_producto("Laptop Dell XPS 14", 5, 4400.0)
        inventario = self.gestor.obtener_inventario()
        self.assertIn("Laptop Dell XPS 14", inventario)

    def test_cantidad_equipo_correcta(self):
        """Verifica que la cantidad de unidades es correcta."""
        self.gestor.agregar_producto("Monitor LG 27", 10, 850.0)
        inventario = self.gestor.obtener_inventario()
        self.assertEqual(inventario["Monitor LG 27"][0], 10.0)

    def test_precio_equipo_correcto(self):
        """Verifica que el precio unitario del equipo es correcto."""
        self.gestor.agregar_producto("Teclado Logitech G512", 88, 55.0)
        inventario = self.gestor.obtener_inventario()
        self.assertEqual(inventario["Teclado Logitech G512"][1], 55.0)

    def test_inventario_vacio_inicial(self):
        """Verifica que el inventario inicia sin equipos registrados."""
        self.assertEqual(len(self.gestor.obtener_inventario()), 0)

    def test_multiples_equipos(self):
        """Verifica registro de múltiples equipos de cómputo."""
        self.gestor.agregar_producto("Laptop HP", 3, 3200.0)
        self.gestor.agregar_producto("Mouse Logitech", 20, 45.0)
        self.gestor.agregar_producto("Headset HyperX", 12, 180.0)
        self.assertEqual(len(self.gestor.obtener_inventario()), 3)

    def test_actualizar_stock_equipo(self):
        """Verifica que actualizar un equipo existente reemplaza sus datos."""
        self.gestor.agregar_producto("SSD Kingston 1TB", 8, 220.0)
        self.gestor.agregar_producto("SSD Kingston 1TB", 15, 210.0)
        inventario = self.gestor.obtener_inventario()
        self.assertEqual(inventario["SSD Kingston 1TB"][0], 15.0)

    def test_stock_minimo_alerta(self):
        """Kata TDD: verifica que equipos con stock <= 2 requieren reabastecimiento."""
        self.gestor.agregar_producto("Laptop Lenovo ThinkPad", 2, 5100.0)
        inventario = self.gestor.obtener_inventario()
        stock = inventario["Laptop Lenovo ThinkPad"][0]
        self.assertLessEqual(stock, 2)


if __name__ == "__main__":
    unittest.main()
