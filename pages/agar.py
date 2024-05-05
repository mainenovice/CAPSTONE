from flet import *
from datetime import date, datetime
import random
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
        self.liquid = ElevatedButton(text='Liquid', on_click=lambda _: page.go('/liquid'))
        self.grain = ElevatedButton(text='Grain', on_click=lambda _: page.go('/grain'))
        self.bulk = ElevatedButton(text='Bulk', on_click=lambda _: page.go('/bulk'))
        self.harvest = ElevatedButton(text='Harvest', on_click=lambda _: page.go('/harvest'))
        self.dataview = ElevatedButton(text='View Data', on_click=lambda _: page.go('/dataview'))
        #inputs
        self.agar_name= Dropdown(options=self.get_spores(),on_change=self.dropdown_changed)
        self.agar_date= TextField(label=f'{date.today()}',read_only=True)
        self.agar_notes= TextField(label='Notes')
        self.agar_submit= ElevatedButton(text='Add to Database', on_click=lambda _: self.add_agar() )

    def generate_agar_batch_number(self, agar_name):
        """
        Generates a unique batch number for agar entries.

        Args:
        crud (CRUD): The CRUD class instance for database interaction.
        agar_name (str): The name of the agar from which to derive part of the batch number.

        Returns:
        str: A unique batch number.
        """
        # Extract the first three letters of the agar name, ensuring it's alphanumeric
        agar_prefix = ''.join([c for c in agar_name if c.isalnum()])[:3].upper()
        # Format the date as YYYYMMDD
        current_date = datetime.now().strftime("%Y%m%d")
        # Query the database for the total number of agar entries to get an index
        total_count = self.crud.session.query(AgarTable).count() + 1
        # Generate a random number of specified length
        random_number = random.randint(100, 999)  # three-digit random number for uniqueness
        # Construct the batch number
        return f"AGA-{agar_prefix}-{current_date}-{total_count}-{random_number}"

    def dropdown_changed(self, event):
        # Convert index to integer (assuming it's provided as a string)
        selected_index = int(event.control.value) - 1  # Adjust if your index is 0-based or 1-based

        # Ensure the index is within the valid range
        if 0 <= selected_index < len(self.agar_name.options):
            selected_option = self.agar_name.options[selected_index]
            self.selected_key = selected_option.key
            self.selected_text = selected_option.text
        else:
            self.selected_key = None
            self.selected_text = None
            print("Selected index is out of range.")

        print(f"Selected key: {self.selected_key}, Selected text: {self.selected_text}")

    #def define_batch(self):
    def get_spores(self):
        spore_options = self.crud.fetch_for_dropdown(Spores, 'spore_name', 'spore_batch')
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
        if self.selected_text:
            # Generate the batch number using the selected agar name
            self.batch_number = self.generate_agar_batch_number(self.selected_text)
            # Create the new agar entry with the generated batch number
            new_agar_entry = AgarTable(
                aga_batch=self.batch_number,
                aga_name=self.selected_text,  # Use the actual name, not just the key
                aga_notes=self.agar_notes.value,
                aga_date=date.today()
            )
            self.crud.create(new_agar_entry)
            self.confirm_add()
        else:
            print("No agar selected.")

    def confirm_add(self):
        # show confirmation text and clear values
        self.agar_name.value = ''
        self.agar_name.update()

        #self.agar_batch.value = ''
        #self.agar_batch.update()

        self.agar_notes.value = ''
        self.agar_notes.update()
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
                  content=Column(controls=[self.agar_name,self.agar_notes,self.agar_date,self.agar_submit])
              )
                  ]
          )
              )

            ]
          )
