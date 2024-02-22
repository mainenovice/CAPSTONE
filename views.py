from flet import *
from pages.home import Home
from pages.add import Add
from pages.cultures import Cultures
from pages.notes import Notes

def views_handler(page):
    return {
        '/':View(
                route='/',
                controls=[
                  Home(page)
                ]
        ),
        '/cultures': View(
            route='/cultures',
            controls=[
                Cultures(page)
            ]
        ),
        '/add': View(
            route='/add',
            controls=[
                Add(page)
            ]
        ),
        '/notes': View(
            route='/notes',
            controls=[
                Notes(page)
            ]
        ),
    }