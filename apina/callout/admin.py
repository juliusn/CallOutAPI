from django.contrib import admin
from .models import User, Beacon, Workspace, Subscription
admin.site.register(User)
admin.site.register(Beacon)
admin.site.register(Workspace)
admin.site.register(Subscription)
