from flet import *
from pages.home import Home
from pages.spore import Spore
from pages.inventory import Inventory
from pages.agar import Agar
from pages.harvest import Harvest
from pages.dataview import Dataview

def views_handler(page):
    return {
        '/':View(
                route='/',
                controls=[
                  Home(page)
                ]
        ),
        '/inventory': View(
            route='/inventory',
            controls=[
                Inventory(page)
            ]
        ),
        '/spore': View(
            route='/spore',
            controls=[
                Spore(page)
            ]
        ),
        '/agar': View(
            route='/agar',
            controls=[
                Agar(page)
            ]
        ),
        '/harvest': View(
            route='/harvest',
            controls=[
                Harvest(page)
            ]
        ),
        '/dataview': View(
            route='/dataview',
            controls=[
                Dataview(page)
            ]
        ),
    }