from mezzanine.conf import register_setting

from django.utils.translation import gettext as _

register_setting(
   name="TEMPLATE_ACCESSIBLE_SETTINGS",
   description = _("Sequence of setting names available within templates."),
   editable = False,
   default = ("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_VIMEO",
       "SOCIAL_LINK_TUMBRL", "SOCIAL_LINK_TWITTER", "SOCIAL_LINK_DELICIOUS"),
   append = True,
)

register_setting(
   name="SOCIAL_LINK_FACEBOOK",
   label=_("facebook link"),
   description=_("if present a facebook icon linking here will be in the "
                 "header."),
   #label="facebook link",
   #description="if present a facebook icon linking here will be in the header.",
   editable=True,
   default="https://facebook.com/mezzatheme",
)

register_setting(
   name="SOCIAL_LINK_VIMEO",
   #label=_("vimeo link"),
   #description=_("if present a vimeo icon linking here will be in the "
                 #"header."),
   #label="vimeo link",
   #description="if present a vimeo icon linking here will be in the header.",
   editable=True,
   default="https://vimeo.com/mezzatheme",
)

register_setting(
   name="SOCIAL_LINK_TUMBRL",
   #label=_("vimeo link"),
   #description=_("if present a vimeo icon linking here will be in the "
                 #"header."),
   label="vimeo link",
   description="if present a vimeo icon linking here will be in the header.",
   editable=True,
   default="https://vimeo.com/mezzatheme",
)

register_setting(
   name="SOCIAL_LINK_TWITTER",
   label=_("twitter link"),
   description=_("if present a twitter icon linking here will be in the "
                 "header."),
   #label="twitter link",
   #description="if present a twitter icon linking here will be in the header.",
   editable=True,
   default="https://twitter.com/mezzatheme",
)

register_setting(
   name="SOCIAL_LINK_DELICIOUS",
   label=_("delicious link"),
   description=_("if present a delicious icon linking here will be in the "
                 "header."),
   #label="delicious link",
   #description="if present a delicious icon linking here will be in the header.",
   editable=True,
   default="https://delicious.com/mezzatheme",
)

