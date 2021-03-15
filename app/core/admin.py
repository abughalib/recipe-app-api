from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
	ordering = ['id']
	list_display = ['email', 'name']
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(gettext('Personal Info'), {'fields': ('name',)}),
		(
			gettext('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}
		),
		(gettext('Important Dates'), {'fields': ('last_login',)})
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		}),
	)

# admin.site.register(User, UserAdmin)
