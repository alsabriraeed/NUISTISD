from django.contrib import admin
from .models import Department, Activity, News, Newsimages, Note, Schools, Programs, Programstype ,Aboutus, Websitelogo, Excellentscholar




class NewsimagesAdmin(admin.ModelAdmin):
    list_display = ('news', 'news_image')

    admin.site.site_header = 'NUIST Activities Management System'  # default: "Django Administration"
    admin.site.index_title = 'NUIST Activities'  # default: "Site administration"
    admin.site.site_title = 'NUIST Activities Management System'  # default: "Django site admin"


admin.site.register(Websitelogo)
admin.site.register(Excellentscholar)
admin.site.register(Department)
admin.site.register(Aboutus)
admin.site.register(Activity)
admin.site.register(News)
admin.site.register(Newsimages, NewsimagesAdmin)
admin.site.register(Note)
admin.site.register(Schools)
admin.site.register(Programs)
admin.site.register(Programstype)

