from django.db import models

# Create your models here.


STATE_CHOICES = (
    (0, 'Pending'),
    (1, 'Paid'),
    (2, 'Cancelled'),
)

SERVICES_CHOICES = (
    (0, 'Agua'),
    (1, 'Luz'),
    (2, 'Telefono'),
    (3, 'Internet'),
    (4, 'Gas'),
)

class Payable(models.Model):
    """
    This class represents the payable document in the database.
    """
    service = models.PositiveSmallIntegerField(choices=SERVICES_CHOICES, verbose_name='Servicio')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    deadline = models.DateField(verbose_name='Fecha de vencimiento')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importe')
    state = models.PositiveSmallIntegerField(choices=STATE_CHOICES, verbose_name='Estado')

    class Meta:
        verbose_name = 'Boleta de pago'
        verbose_name_plural = 'Boletas de pago'

    def __str__(self):
        return f'{self.id} {self.service}-{self.amount}'

    @property
    def barcode(self):
        return self.id

    def save(self, *args, **kwargs):
        """
        This method is used to set the state of the bill to pending when
        the bill is created.
        """
        if self.pk is None:
            self.state = 0
        super(Payable, self).save(*args, **kwargs)


PAYMENT_METHOD_CHOICES = (
    (0, 'Efectivo'), # Cash
    (1, 'Tarjeta de crédito'), # Credit card
    (2, 'Tarjeta de débito'), # Debit card
)

class Transaction(models.Model):
    """
    This class represents the payment info in the database.
    """
    payable = models.OneToOneField(Payable, on_delete=models.CASCADE, verbose_name='Factura', related_name='payment')
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD_CHOICES, verbose_name='Método de pago', default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importe')
    card_number = models.CharField(max_length=16, verbose_name='Número de tarjeta', null=True, blank=True)
    date = models.DateField(verbose_name='Fecha de pago')

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'

    def __str__(self):
        return f'{self.get_payment_method_display()} {self.amount}'

    @property
    def barcode(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.payable.state = 1
        super(Transaction, self).save(*args, **kwargs)

