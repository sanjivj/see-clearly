from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

# Create your models here.
class HomePage(Page, RichText):
    '''
        A page representing the format of the HomePage.
    '''
    heading = models.CharField(max_length = 200, 
        help_text = "The heading under the icon blurbs")
    subheading = models.CharField(max_length = 200, 
        help_text = "The subheading under the heading")
    featured_works_heading = models.CharField(max_length = 200, 
        default = "Latest Posts")
        
    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")
        
class Slide(Orderable):
    '''
        A slide in a slider connected to a Home Page
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name =_("Image"),
        upload_to = upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True,)
    
class IconBlurb(Orderable):
    '''
        An icon box on a Home Page
    '''
    homepage = models.ForeignKey(HomePage, related_name='blurbs')
    icon = FileField(verbose_name=_("Image"),
        upload_to = upload_to("theme.IconBlurb.icon", "icons"),
        format ="Image", max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional; if provided, clicking the blurb will go here.")
        
    
class Portfolio(Page):
    '''
        A collection of individual portfolio items
    '''
    
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
    