from flet import *
from datetime import date
from pages.database import *
# from pages.nav_menu import Nav_Menu
class Agar(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        #self.agar_batch=TextField(label=f'$p3-{self.agar_name.value[:2]}-',read_only=True)
        self.agar_name= Dropdown()
        self.agar_date= TextField(label=f'{date.today()}',read_only=True)
        self.agar_vendor= TextField(label='Vendor Name')
        self.agar_website= TextField(label='Vendor Website')
        self.agar_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_agar() )
        self.agar_name.options=self.get_spores()
    def get_spores(self):
        self.crud=CRUD()
        spore_query=self.crud.read(Spores)
        options = [{"text": spore.spore_name, "value": str(spore.spore_id)} for spore in spore_query]
        return options

    def add_agar(self):
        self.crud=CRUD()
        self.crud.create(Agar(agar_name=self.agar_name.value,
                                agar_vendor=self.agar_vendor.value,
                                agar_website=self.agar_website.value,
                                agar_date=date.today()
                                ))
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
                  padding=padding.all(300),
                  content=Column(controls=[self.agar_name,self.agar_website,self.agar_date,self.agar_vendor,self.agar_submit])
              )
                  ]
          )
              )

            ]
          )