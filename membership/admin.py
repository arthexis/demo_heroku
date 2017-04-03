from django.contrib import admin
from membership.models import *


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'start_date', 'paid_amount')



