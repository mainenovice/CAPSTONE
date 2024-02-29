from flet import *
from pages.home import Home
from pages.inventory import Inventory
from pages.preparation import Preparation
from pages.inoculation import Inoculation
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
        '/preparation': View(
            route='/preparation',
            controls=[
                Preparation(page)
            ]
        ),
        '/inoculation': View(
            route='/inoculation',
            controls=[
                Inoculation(page)
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