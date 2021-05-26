from pretix.base.email import TemplateBasedMailRenderer
from django.template.loader import get_template
template = get_template('pretix_nes_mail/NES.html')

class NESMailRenderer(TemplateBasedMailRenderer):
    verbose_name = "NES Mail"
    identifier = "NES"
    thumbnail_filename = "pretix_nes_mail/NET_Thumb.png"
    template_name = "pretix_nes_mail/NES.html"
