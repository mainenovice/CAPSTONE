from flet import *
from pages.home import Home
from pages.spore import Spore
from pages.inventory import Inventory
from pages.agar import Agar
from pages.liquid import Liquid
from pages.grain import Grain
from pages.bulkpage import BulkPage
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
        '/liquid': View(
            route='/liquid',
            controls=[
                Liquid(page)
            ]
        ),
        '/grain': View(
            route='/grain',
            controls=[
                Grain(page)
            ]
        ),
        '/bulk': View(
            route='/bulk',
            controls=[
                BulkPage(page)
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