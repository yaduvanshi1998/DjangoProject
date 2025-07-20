from django.contrib import admin

from .models import UserDetails

# Register your models here.

# admin.site.register(UserDetails)

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password') # These fields will be shown in the admin table
    search_fields = ('Username', 'Email') # This will help you to search data through username and email
    list_filter = ('Email',) # This will help to filter data by Email

