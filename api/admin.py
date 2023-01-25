from django.contrib import admin

from api.models import Profil, InstagramAccounts, Services, ServicePrices, EarnList, Orders, BalanceRequest
# Register your models here.
admin.site.register(Profil)
admin.site.register(InstagramAccounts)
admin.site.register(EarnList)
admin.site.register(ServicePrices)
admin.site.register(Services)
admin.site.register(Orders)
admin.site.register(BalanceRequest)
