from django.contrib import admin
from .models import Index,Service,Testimonial,Gallery,About,Language,Contact,Banner

# Register your models here.
admin.site.register(Language)
admin.site.register(Index)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Banner)