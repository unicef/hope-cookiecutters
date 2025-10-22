from django.contrib import admin
from flags.admin import FlagStateAdmin as BaseFlagStateAdmin
from flags.models import FlagState

admin.site.unregister([FlagState])


@admin.register(FlagState)
class FlagStateAdmin(BaseFlagStateAdmin[FlagState]):  # type: ignore[misc]
    pass
