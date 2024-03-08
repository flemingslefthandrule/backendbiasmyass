from django.apps import apps
from django.contrib import admin


models = apps.get_models()

for model in models:
    if admin.sites.AlreadyRegistered:
        pass
    else:
        admin.site.register(model)