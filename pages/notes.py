from flet import *
# from pages.nav_menu import Nav_Menu
class Notes(UserControl):
        def __init__(self,page):
                super().__init__()
                self.page = page
                self.add_btn = ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
                self.cultures_btn = ElevatedButton(text='Cultures Data', on_click=lambda _: page.go('/cultures'))
                self.notes_btn = ElevatedButton(text='Add A Culture', on_click=lambda _: page.go('/add'))
        def build(self):
          return Column(
            controls=[
              Container(
                  bgcolor='blue',
                  content=Column(
                    controls=[
                        Row(controls=[self.add_btn, self.cultures_btn, self.notes_btn],alignment=MainAxisAlignment.CENTER),
                        Text('NOTES PAGE')
                  ]
          )
              )

            ]
          )

