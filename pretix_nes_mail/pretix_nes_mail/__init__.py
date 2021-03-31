from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = "1.0.0"


class PluginApp(PluginConfig):
    name = "pretix_nes_mail"
    verbose_name = "NES Mail"

    class PretixPluginMeta:
        name = gettext_lazy("NES Mail")
        author = "mk"
        description = gettext_lazy("Short description")
        visible = True
        version = __version__
        category = "CUSTOMIZATION"
        compatibility = "pretix>=3"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_nes_mail.PluginApp"
