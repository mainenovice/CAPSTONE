import flet as ft

class Nav_Menu():
    menu_add = ft.ElevatedButton(text='Add/Update Cultures', on_click=lambda _:page.go('/add'))
    menu_about = ft.ElevatedButton(text='Cultures Data', on_click=lambda _:page.go('/cultures'))
    menu_notes = ft.ElevatedButton(text='Take New Notes', on_click=lambda _:page.go('/notes'))
    menu_row = ft.Row(controls=[menu_add, menu_about, menu_notes], alignment=ft.MainAxisAlignment.CENTER)
