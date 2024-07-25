from django import template

from menu.models import Menu, MenuElement

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(menu_name, selected_menu_element):
    menu_elements = list(MenuElement.objects.filter(parent_menu__name=menu_name))

    parent_elem = next(filter(lambda x: x.parent_id is None, menu_elements), None)
    menu_elements_clear = {
        'text': parent_elem.text,
        'slug': parent_elem.slug
    }

    selected = next(filter(lambda x: x.slug == selected_menu_element, menu_elements), None)
    if selected:
        parent_elem = selected
        menu_elements_clear = {}

        while parent_elem:
            menu_elements_clear = {
                'text': parent_elem.text,
                'slug': parent_elem.slug,
                'children': [
                    *[{
                        'text': elem.text,
                        'slug': elem.slug,
                    } for elem in
                        filter(lambda x: x.parent_id == parent_elem.id and x.text != menu_elements_clear.get('text'),
                               menu_elements)],
                    menu_elements_clear
                ]
            }
            parent_elem = parent_elem.parent

    return {
        "menu_elements": [menu_elements_clear],
        'selected_menu_element': selected_menu_element
    }
