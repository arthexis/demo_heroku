from moneyed import Money, MXN
from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager
from django.db.models import *
from django.contrib.auth.models import User
from localflavor.mx.models import MXStateField


class MembershipManager(Manager):
    pass


class Membership(User):
    objects = money_manager(MembershipManager())

    start_date = DateField("Inicio Membresía", auto_now_add=True)
    balance = MoneyField("Balance", max_digits=10, decimal_places=2, default=Money(100, MXN), default_currency=MXN)
    mx_state = MXStateField("Ubicación", default='NLE')

    class Meta:
        ordering = ('start_date', )
        verbose_name = 'Membresía'
        db_table = 'demo_membership'


__all__ = ('Membership', )
