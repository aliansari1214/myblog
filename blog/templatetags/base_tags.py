from django import template
from ..models import Category

register = template.Library()




@register.inclusion_tag("blog/partials/category-navbar.html")
def category_navbar():
    data = {
        'category': Category.objects.filter(status=True),
    }
    return data

@register.simple_tag
def title():
    return 'Telecom Blog'

