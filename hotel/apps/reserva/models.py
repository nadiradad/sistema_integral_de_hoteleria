from django.db import models

# Create your models here.
class Reserva(models.Model):
    id_habitacion = models. ForeignKey('habitacion.Habitacion', on_delete=models.CASCADE)
    id_servicio_adicional = models.ForeignKey('servicio_adicional.Servicio_adicional', on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    monto_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Reserva {self.id} - {self.estado}' # type: ignore