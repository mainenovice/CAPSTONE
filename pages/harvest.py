from flet import *
# from pages.nav_menu import Nav_Menu
class Harvest(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.preparation = ElevatedButton(text="Preparation", on_click=lambda _: page.go('/preparation'))
        self.inoculation = ElevatedButton(text='Inoculation', on_click=lambda _: page.go('/inoculation'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
    def build(self):
          return Column(
            controls=[
              Container(
                  bgcolor=colors.INDIGO_300,
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.preparation, self.inoculation,self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
                        Text('Harvest'),
                  ]
          )
              )

            ]
          )