from flet import *
from datetime import date
from pages.database import *
# from pages.nav_menu import Nav_Menu
class Agar(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.crud = CRUD()
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        self.agar_name= Dropdown(options=self.get_spores(),on_change=self.dropdown_changed)
        self.agar_date= TextField(label=f'{date.today()}',read_only=True)
        self.date_string=date.today().strftime("%Y%m%d")
        self.agar_batch= TextField(label=f'$${self.date_string}', read_only=True)
        self.agar_notes= TextField(label='Notes')
        self.agar_submit= ElevatedButton(text='Add to Database')#, on_click=lambda _: self.add_agar() )


    def dropdown_changed(self,event):
        self.selected_value=self.agar_name.value

    def get_spores(self):
        # Fetching options using the fetch_for_dropdown method
        spore_options = self.crud.fetch_for_dropdown(Spores, 'spore_name', 'spore_id')

        # Convert the dictionaries to Option objects
        #options = [dropdown.Option(text=option["text"], value=option["value"]) for option in spore_options]
        options = [dropdown.Option(key=str(option["value"]), text=option["text"]) for option in spore_options]
        return options

    # def get_spores(self):
    #     spore_query=self.crud.read(Spores)
    #     options = Options(self.crud.fetch_for_dropdown(Spores, 'spore_name', 'spore_id')
    #     return options
    def populate_options(self):
        self.agar_name.options = self.get_spores()
        self.agar_name.update()
    def add_agar(self):
        self.crud.create(AgarTable(aga_name=self.agar_name.value,
                                   aga_batch=self.agar_batch.value,
                                   aga_notes=self.agar_notes.value,
                                   aga_date=date.today()
                                ))
    def build(self):
          return Column(
            controls=[
              Container(
                  #padding=padding.all(50),
                  bgcolor='#33334d',
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.spore,self.agar,
                                      self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
              Container(
                  padding=padding.all(130),
                  content=Column(controls=[self.agar_name,self.agar_notes,self.agar_date,self.agar_submit])
              )
                  ]
          )
              )

            ]
          )
