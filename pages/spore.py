from flet import *
from datetime import date
from pages.database import *
# from pages.nav_menu import Nav_Menu
class Spore(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        #self.spore_batch=TextField(label=f'$p3-{self.spore_name.value[:2]}-',read_only=True)
        self.spore_name= TextField(label='Name of Species')
        self.spore_date= TextField(label=f'{date.today()}',read_only=True)
        self.spore_vendor= TextField(label='Vendor Name')
        self.spore_website= TextField(label='Vendor Website')
        self.spore_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_spore() )
    def add_spore(self):
        self.crud=CRUD()
        self.crud.create(Spores(spore_name=self.spore_name.value,
                                spore_vendor=self.spore_vendor.value,
                                spore_website=self.spore_website.value,
                                spore_date=date.today()
                                ))
        self.confirm_add()
    def confirm_add(self):
        #show confirmation text and clear values
        self.spore_name.value = ''
        self.spore_name.update()

        self.spore_website.value = ''
        self.spore_website.update()

        self.spore_vendor.value = ''
        self.spore_vendor.update()
    def build(self):
          return Column(
            controls=[
              Container(
                  #padding=padding.all(50),
                  bgcolor='#33334d',
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.spore, self.agar, self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
              Container(
                  padding=padding.all(130),
                  content=Column(controls=[self.spore_name,self.spore_website,self.spore_date,self.spore_vendor,self.spore_submit])
              )
                  ]
          )
              )

            ]
          )