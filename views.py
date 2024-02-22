from flet import *
from pages.home import Home
def views_handler(page):
    return {
        '/':View(
                route='/',
                controls=[
                  Home(page)
                ]
        ),
        '/cultures': View(
            route='/login',
            controls=[
                Container(
                    bgcolor='blue'
                )
            ]
        ),
        '/add': View(
            route='/add',
            controls=[
                Container(
                    bgcolor='red'
                )
            ]
        ),
        '/cultures': View(
            route='/cultures',
            controls=[
                Container(
                    bgcolor='green'
                )
            ]
        ),
    }