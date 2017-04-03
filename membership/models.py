from django.db.models import *
from django.contrib.auth.models import User


class Membership(User):
    start_date = DateField("Inicio Membresía", auto_now_add=True)
    paid_amount = FloatField("Monto Pagado", default=100)

    class Meta:
        ordering = ('start_date', )
        verbose_name = 'Membresía'
        db_table = 'demo_membership'


__all__ = ('Membership', )
