from flet import *
from datetime import date
from pages.database import *
# from pages.nav_menu import Nav_Menu
class Inventory(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        #self.inventory_batch=TextField(label=f'$p3-{self.inventory_name.value[:2]}-',read_only=True)
        self.inventory_name= TextField(label='Item name')
        self.inventory_date= TextField(label=f'{date.today()}',read_only=True)
        self.inventory_vendor= TextField(label='Vendor Name')
        self.inventory_quantity= TextField(label='Quantity in units')
        self.inventory_units= TextField(label='Unit of Measurement')
        self.inventory_website= TextField(label='Reorder Link')
        self.inventory_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_inventory() )

    def generate_batch_number(self):
        # Generate a batch number from the date and first 3 characters of the vendor name
        date_str = f'{date.month}{date.day}'  # Remove dashes from date
        vendor_prefix = self.inventory_vendor.value[:3].upper()  # First 3 characters of vendor, made uppercase
        return f"{date_str}-{vendor_prefix}"
    def confirm_add(self):
        #show confirmation text and clear values
        self.inventory_name.value = ''
        self.inventory_name.update()

        self.inventory_vendor.value = ''
        self.inventory_vendor.update()

        self.inventory_quantity.value = ''
        self.inventory_quantity.update()

        self.inventory_units.value = ''
        self.inventory_units.update()

        self.inventory_website.value = ''
        self.inventory_website.update()

    def add_inventory(self):
        batch_number = self.generate_batch_number()  # Generate the unique batch number
        self.crud=CRUD()
        self.crud.create(InvTable(inv_batch=batch_number,
                                  inv_name=self.inventory_name.value,
                                  inv_vendor=self.inventory_vendor.value,
                                  inv_website=self.inventory_website.value,
                                  inv_quantity=self.inventory_quantity.value,
                                  inv_units=self.inventory_units.value,
                                  inv_date=date.today()
                                ))
        self.confirm_add()
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
                  content=Column(controls=[self.inventory_name,self.inventory_vendor,self.inventory_website,self.inventory_date,self.inventory_quantity,self.inventory_units,self.inventory_submit])
              )
                  ]
          )
              )

            ]
          )