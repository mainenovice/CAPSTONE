from flet import *
# from pages.nav_menu import Nav_Menu
class Home(UserControl):
        def __init__(self,page):
                super().__init__()
                self.page = page
                self.add_btn = ElevatedButton(text='Add/Update Cultures', on_click=lambda _: page.go('/add'))
                self.cultures_btn = ElevatedButton(text='Cultures Data', on_click=lambda _: page.go('/cultures'))
                self.notes_btn = ElevatedButton(text='Take New Notes', on_click=lambda _: page.go('/notes'))
        def build(self):
          return Column(
            controls=[
              Container(
                  bgcolor=colors.INDIGO_300,
                  content=Column(
                    controls=[
                        Row(controls=[self.add_btn, self.cultures_btn, self.notes_btn],alignment=MainAxisAlignment.CENTER),
                        Text('HOME PAGE'),
                  ]
          )
              )

            ]
          )