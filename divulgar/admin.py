from django.contrib import admin

from divulgar.models import Raca, Tag, Pet

admin.site.register([Raca, Tag, Pet])
