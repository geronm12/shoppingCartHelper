from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Product(models.Model):
    code = models.CharField(max_length=255, verbose_name="Codigo", unique=True)
    numericCode = models.BigIntegerField(
        max_length=255, verbose_name="Codigo Numerico", unique=True)
    name = models.CharField(max_length=255, verbose_name="Descripción")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    public_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total")
    system_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total")
    expiration_date = models.DateTimeField(
        verbose_name="Fecha de Expiración")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"Carrito de {self.user.email} - {self.description}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_carts'
    )

    description = models.CharField(max_length=255, verbose_name="Descripción")
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total")
    expiration_date = models.DateTimeField(
        verbose_name="Fecha de Expiración")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    items = models.ManyToManyField(
        Product,
        through='CartItemRelation',  # Nombre de la tabla intermedia
        related_name='shopping_carts'
    )

    def __str__(self):
        return f"Carrito de {self.user.email} - {self.description}"


class CartItemRelation(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Datos extra sobre la relación
    quantity = models.PositiveIntegerField(default=1)
    unitary_price = models.DecimalField(
        max_digits=10, decimal_places=2)  # Precio al momento de agregar

    class Meta:
        unique_together = ('shopping_cart', 'item')

    def __str__(self):
        return f"{self.quantity} x {self.item.name} en carrito de {self.shopping_cart.user.email}"
