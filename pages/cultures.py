from flet import *


class Cultures(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.add_btn = ElevatedButton(text='Back to Home', on_click=lambda _: page.go('/'))
        self.cultures_btn = ElevatedButton(text='Cultures Data', on_click=lambda _: page.go('/cultures'))
        self.notes_btn = ElevatedButton(text='Take New Notes', on_click=lambda _: page.go('/notes'))
        # define the variables to catch the user input I'm going to use c_<name> to avoid any mixups
        # self.c_name=TextField(label='Name:')
        # self.c_name=TextField(label='Message:')
        # self.c_name=TextField(label='Name:')
        # self.c_name=TextField(label='Name:')
        # self.c_name=TextField(label='Name:')

    def build(self):
        return Column(
            controls=[
                Container(
                    bgcolor=colors.INDIGO_500,
                    content=Column(
                        controls=[
                            Row(controls=[self.add_btn, self.cultures_btn, self.notes_btn],
                                alignment=MainAxisAlignment.CENTER),
                        ]
                    )
                ),
                Container(
                    bgcolor=colors.INDIGO_300,
                    content=Column(
                        controls=[
                            Row(controls=[TextField(label='Name'),TextField(label='Inventory')],
                                alignment=MainAxisAlignment.CENTER),
                        ]
                    )
                ),
                Container(
                    bgcolor=colors.INDIGO_300,
                    content=Column(
                        controls=[
                            Row(controls=[TextField(label='Name'),TextField(label='Inventory')],
                                alignment=MainAxisAlignment.CENTER),
                        ]
                    )
                ),
                Container(
                    bgcolor=colors.INDIGO_300,
                    content=Column(
                        controls=[
                            Row(controls=[TextField(label='Name'),TextField(label='Inventory')],
                                alignment=MainAxisAlignment.CENTER),
                        ]
                    )
                )
            ]
        )



