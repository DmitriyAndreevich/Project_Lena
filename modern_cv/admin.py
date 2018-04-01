from django.contrib import admin
from .models import Projects, Posts, Contact

class ProjectsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Projects._meta.fields]

    class Meta:
        model = Projects


admin.site.register(Projects, ProjectsAdmin)



class PostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Posts._meta.fields]

    class Meta:
        model = Posts


admin.site.register(Posts, PostsAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)