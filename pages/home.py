from flet import *
# from pages.nav_menu import Nav_Menu
class Home(UserControl):
        def __init__(self,page):
                super().__init__()
                self.page = page
                self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
                self.spore = ElevatedButton(text="Add Spores", on_click=lambda _: page.go('/spore'))
                self.agar = ElevatedButton(text='Pour Agar', on_click=lambda _: page.go('/agar'))
                self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
                self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        def build(self):
          return Column(
            controls=[
              Container(
                  bgcolor=colors.INDIGO_300,
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.spore, self.agar, self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
                        Text('HOME PAGE'),
                  ]
          )
              )

            ]
          )