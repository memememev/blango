from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()

@register.filter
#for parameter (name="author_details")
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return mark_safe(format_html("<strong>me</strong>"))

    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")
    if author.email:
        start_part = format_html('<a href="mailto:{}">',  author.email)
        name = start_part + name + '</a>'

    return mark_safe(name)