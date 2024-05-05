from flet import *
from datetime import date,datetime
from pages.database import *
import random
# from pages.nav_menu import Nav_Menu
class Liquid(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.crud = CRUD()

        #navigation
        self.inventory = ElevatedButton(text='Add/Update Inventory', on_click=lambda _: page.go('/inventory'))
        self.spore = ElevatedButton(text="Spore", on_click=lambda _: page.go('/spore'))
        self.agar = ElevatedButton(text='Agar', on_click=lambda _: page.go('/agar'))
        self.liquid = ElevatedButton(text='Liquid', on_click=lambda _: page.go('/liquid'))
        self.grain = ElevatedButton(text='Grain', on_click=lambda _: page.go('/grain'))
        self.bulk = ElevatedButton(text='Bulk', on_click=lambda _: page.go('/bulk'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        self.liquid_name= Dropdown(options=self.get_agar(),on_change=self.dropdown_changed)
        self.liquid_date= TextField(label=f'{date.today()}',read_only=True)
        self.date_string=date.today().strftime("%Y%m%d")
        self.liquid_batch = TextField(label="Batch Number", read_only=True)
        self.liquid_notes= TextField(label='Notes')
        self.liquid_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_liquid() )

    def generate_liquid_batch_number(self, liquid_name):
        """
        Generates a unique batch number for liquid entries.

        Args:
        liquid_name (str): The name of the liquid from which to derive part of the batch number.

        Returns:
        str: A unique batch number.
        """
        # Extract the first three letters of the liquid name, ensuring it's alphanumeric
        liquid_prefix = ''.join([c for c in liquid_name if c.isalnum()])[:3].upper()
        # Format the date as YYYYMMDD
        current_date = datetime.now().strftime("%Y%m%d")
        # Query the database for the total number of liquid entries to get an index
        total_count = self.crud.session.query(LiquidTable).count() + 1  # Make sure to use the correct table here
        # Generate a random number of specified length
        random_number = random.randint(100, 999)  # three-digit random number for uniqueness
        # Construct the batch number
        return f"LC-{liquid_prefix}-{current_date}-{total_count}-{random_number}"

    def dropdown_changed(self, event):
        # Directly use the value from the dropdown as the key
        self.selected_key = event.control.value

        # Find the corresponding option text using selected_key
        selected_option = next((opt for opt in self.liquid_name.options if opt.key == self.selected_key), None)
        if selected_option:
            self.selected_text = selected_option.text
        else:
            # Handle case where no corresponding option is found
            self.selected_text = None
            print("No corresponding option found for key:", self.selected_key)

        print(f"Selected key: {self.selected_key}, Selected text: {self.selected_text}")

    def get_agar(self):
        agar_options = self.crud.fetch_for_dropdown(AgarTable, 'aga_name', 'aga_batch')
        print("Fetched agar options:", agar_options)
        options = [dropdown.Option(key=str(option["value"]), text=option["text"]) for option in agar_options]
        return options

    # def get_spores(self):
    #     spore_query=self.crud.read(Spores)
    #     options = Options(self.crud.fetch_for_dropdown(Spores, 'spore_name', 'spore_id')
    #     return options
    def populate_options(self):
        self.liquid_name.options = self.get_agar()
        self.liquid_name.update()

    def confirm_add(self):
        # Show confirmation text or log it
        print("Liquid entry successfully added.")

        # Reset the dropdown selection to the default or blank option
        # Ensure you have a default or blank option in your dropdown initialization
        if self.liquid_name.options:
            self.liquid_name.value = self.liquid_name.options[0].key
        else:
            self.liquid_name.value = ''
        self.liquid_name.update()

        # Clear the notes TextField
        self.liquid_notes.value = ''
        self.liquid_notes.update()

    def add_liquid(self):
        if self.selected_key and self.selected_text:
            # Generate the batch number using the selected liquid name
            self.liquid_batch.value = self.generate_liquid_batch_number(self.selected_text)
            # Create the new liquid entry
            new_liquid_entry = LiquidTable(  # Replace AgarTable with LiquidTable if different
                liqui_batch=self.liquid_batch.value,
                liqui_name=self.selected_text,
                liqui_notes=self.liquid_notes.value,
                liqui_date=date.today()
            )
            self.crud.create(new_liquid_entry)
            print("Liquid entry added:", new_liquid_entry)
            self.confirm_add()
        else:
            print("No valid liquid selected or key not found.")

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
              Container(
                  padding=padding.all(130),
                  content=Column(controls=[self.liquid_name,self.liquid_notes,self.liquid_date,self.liquid_submit])
              )
                  ]
          )
              )

            ]
          )
