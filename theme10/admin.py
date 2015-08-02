from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from theme10.models import HomePage, IconBlurb, Portfolio, Slide

class IconBlurbAdmin(TabularDynamicInlineAdmin):
    """docstring for IconBlurbAdmin"""
    #def __init__(self, arg):
        #super(IconBlurbAdmin, self).__init__()
        #self.arg = arg
    model = IconBlurb

class SlideAdmin(TabularDynamicInlineAdmin):
    """docstring for SlideAdmin"""
    #def __init__(self, arg):
        #super(SlideAdmin, self).__init__()
        #self.arg = arg
    model = Slide

class HomePageAdmin(PageAdmin):
    """docstring for HomePageAdmin"""
    #def __init__(self, arg):
        #super(HomePageAdmin, self).__init__()
        #self.arg = arg
    model = HomePage
    inlines = (IconBlurbAdmin, SlideAdmin)

admin.site.register(HomePage, HomePageAdmin)

admin.site.register(Portfolio, PageAdmin)
