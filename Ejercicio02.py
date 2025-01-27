from Ejercicio01 import Producto

class Pedido:

    def __init__(self):
        self.productos = []
        self.cantidades = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)

    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidades):
            total += producto.calcular_total(cantidad)
        return total

    def mostrar_productos(self):
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f"{producto} - Cantidad: {cantidad}")


# Ejemplo de uso
p1 = Producto(1, "Producto 1", 100)
p2 = Producto(2, "Producto 2", 200)
p3 = Producto(3, "Producto 3", 300)

pedido = Pedido()
pedido.agregar_producto(p1, 5)
pedido.agregar_producto(p2, 3)
pedido.agregar_producto(p3, 2)

pedido.mostrar_productos()
print("Total del pedido:", pedido.total_pedido())