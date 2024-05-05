from flet import *
from datetime import date, datetime
from pages.database import *
import random
# from pages.nav_menu import Nav_Menu
class Grain(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.crud = CRUD()
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.liquid = ElevatedButton(text='Liquid', on_click=lambda _: page.go('/liquid'))
        self.grain = ElevatedButton(text='Grain', on_click=lambda _: page.go('/grain'))
        self.bulk = ElevatedButton(text='Bulk', on_click=lambda _: page.go('/bulk'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #page label
        self.page_label=ElevatedButton(text='Grain')

        #inputs
        self.grain_name = Dropdown(options=self.get_liquid(), on_change=self.dropdown_changed)
        self.grain_date= TextField(label=f'{date.today()}',read_only=True)
        self.date_string=date.today().strftime("%Y%m%d")
        #self.grain_batch= TextField(label=f'$${self.date_string}', read_only=True)
        self.grain_notes= TextField(label='Notes')
        self.grain_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_grain() )

    @staticmethod
    def generate_grain_batch_number(crud, grain_name):
        """
        Generates a unique batch number for grain entries.

        Args:
        crud (CRUD): The CRUD class instance for database interaction.
        grain_name (str): The name of the grain from which to derive part of the batch number.

        Returns:
        str: A unique batch number.
        """
        # Extract the first three letters of the grain name, ensuring it's alphanumeric
        grain_prefix = ''.join([c for c in grain_name if c.isalnum()])[:3].upper()
        # Format the date as YYYYMMDD
        current_date = datetime.now().strftime("%Y%m%d")
        # Query the database for the total number of grain entries to get an index
        total_count = crud.session.query(GrainTable).count() + 1
        # Generate a random number of specified length
        random_number = random.randint(100, 999)  # three-digit random number for uniqueness
        # Construct the batch number
        return f"GRA-{grain_prefix}-{current_date}-{total_count}-{random_number}"

    def dropdown_changed(self, event):
        self.selected_key = event.control.value
        selected_option = next((opt for opt in self.grain_name.options if opt.key == self.selected_key), None)
        if selected_option:
            self.selected_text = selected_option.text
        else:
            self.selected_key = None
            self.selected_text = None
            print("Selected key not found in options.")

    def get_liquid(self):
        # Fetching options using the fetch_for_dropdown method
        liqui_options = self.crud.fetch_for_dropdown(LiquidTable, 'liqui_name', 'liqui_batch')

        # Convert the dictionaries to Option objects
        #options = [dropdown.Option(text=option["text"], value=option["value"]) for option in spore_options]
        options = [dropdown.Option(key=str(option["value"]), text=option["text"]) for option in liqui_options]
        return options


    def populate_options(self):
        self.grain_name.options = self.get_agar()
        self.grain_name.update()

    def add_grain(self):
        if self.selected_key:  # Ensure there's a selection
            # Use the static method directly with the class, or just normally if within the class
            self.batch_number = Grain.generate_grain_batch_number(self.crud, self.selected_text)

            # Adjusted to match the actual schema for GrainTable
            self.crud.create(GrainTable(
                gra_batchid=self.batch_number,  # Adjusted the name here
                gra_name=self.selected_text,
                #gra_notes=self.grain_notes.value,
                gra_date=date.today()
            ))
            # Confirm addition and clear fields if necessary
            self.confirm_add()
        else:
            print("No selection made. Please select a grain.")

    def confirm_add(self):
        # Reset the dropdown and other fields to blank
        self.grain_name.value = ''
        self.grain_name.update()

        self.grain_notes.value = ''
        self.grain_notes.update()

        # Reset internal selection tracking
        self.selected_key = None
        self.selected_text = None

    def build(self):
          return Column(
            controls=[
              Container(
                  #padding=padding.all(50),
                  bgcolor='#33334d',
                  content=Column(
                    controls=[
                        Row(controls=[self.inventory, self.spore,self.agar,self.liquid,self.grain,self.bulk,
                                      self.harvest, self.dataview],
                            alignment=MainAxisAlignment.CENTER),
                        Container(content=Column(controls=[self.page_label])),
              Container(
                  padding=padding.all(130),
                  content=Column(controls=[self.grain_name,self.grain_notes,self.grain_date,self.grain_submit])
              )
                  ]
          )
              )

            ]
          )
