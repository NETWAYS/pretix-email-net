from pretix.base.email import TemplateBasedMailRenderer


class NESMailRenderer(TemplateBasedMailRenderer):
    verbose_name = "NES Mail"
    identifier = "NES"
    thumbnail_filename = "pretixbase/email/thumb.png"
    template_name = "pretixbase/email/NES.html"
