from menu.models import MenuElement


class MenuHierarchyService:
    def __init__(self, menu_name, selected_menu_element_slug):
        self.menu_name = menu_name
        self.selected_menu_element_slug = selected_menu_element_slug
        self.menu_elements = self._get_menu_elements_by_name()
        self.selected_menu_element = self._get_selected_menu_element()

    def get_menu_hierarchy(self):
        if not self.selected_menu_element:
            return self._get_start_menu_element()

        menu_elements_clear = {}
        iter_element = self.selected_menu_element
        while iter_element:
            children = self._get_element_children(iter_element)
            mixed_children = self._mix_children(children, menu_elements_clear)
            new_children = self._sorted_children(mixed_children)

            menu_elements_clear = {
                'text': iter_element.text,
                'slug': iter_element.slug,
                'children': new_children
            }
            iter_element = self._get_parent_element(iter_element)
        return menu_elements_clear

    def _get_menu_elements_by_name(self):
        return list(MenuElement.objects.filter(parent_menu__name=self.menu_name))

    def _get_selected_menu_element(self):
        return next(filter(lambda x: x.slug == self.selected_menu_element_slug, self.menu_elements), None)

    def _get_start_menu_element(self):
        start_element = next(filter(lambda x: x.parent_id is None, self.menu_elements), None)
        if start_element:
            return {
                'text': start_element.text,
                'slug': start_element.slug
            }
        return {
                'text': 'Не найдено',
                'slug': 'not_found'
            }

    def _get_element_children(self, iter_element):
        return [
            {
                'text': elem.text,
                'slug': elem.slug,
            } for elem in filter(lambda x: x.parent_id == iter_element.id, self.menu_elements)
        ]

    def _mix_children(self, children, child_to_mix):
        if child_to_mix:
            return [
                *list(
                    filter(lambda x: x.get('text') != child_to_mix.get('text', ''), children)),
                child_to_mix
            ]
        return children

    def _sorted_children(self, children):
        return sorted(children, key=lambda x: x.get('text', ''))

    def _get_parent_element(self, element):
        return next(filter(lambda x: x.id == element.parent_id, self.menu_elements), None)
