from flet import *
# from pages.nav_menu import Nav_Menu
class Culture(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.culture = ElevatedButton(text="Culture", on_click=lambda _: page.go('/culture'))
        self.inoculation = ElevatedButton(text='Inoculation', on_click=lambda _: page.go('/inoculation'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        self.culture_name= TextField(label='Culture Name')
        self.culture_date= TextField(label='Date')
    def build(self):
          return Column(
            controls=[
              Container(
                  bgcolor=colors.INDIGO_300,
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.culture, self.inoculation, self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
                        Text('Cultures'),
              Container(
                  padding=padding.all(20),
                  content=Column(controls=[self.culture_name,self.culture_date])
              )
                  ]
          )
              )

            ]
          )