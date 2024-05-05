from flet import *
from datetime import date,datetime
import random
from pages.database import *
# from pages.nav_menu import Nav_Menu
class BulkPage(UserControl):
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
        self.bulk_name= Dropdown(options=self.get_grains(),on_change=self.dropdown_changed)
        self.bulk_date= TextField(label=f'{date.today()}',read_only=True)
        self.date_string=date.today().strftime("%Y%m%d")
        self.bulk_batch= TextField(label=f'$${self.date_string}', read_only=True)
        self.bulk_notes= TextField(label='Notes')
        self.bulk_submit = ElevatedButton(text='Add to Database', on_click=lambda _: self.add_bulk())

    @staticmethod
    def generate_bulk_batch_number(crud, bulk_name):
        """
        Generates a unique batch number for bulk entries.

        Args:
        crud (CRUD): The CRUD class instance for database interaction.
        bulk_name (str): The name of the bulk item from which to derive part of the batch number.

        Returns:
        str: A unique batch number.
        """
        # Extract the first three letters of the bulk name, ensuring it's alphanumeric
        bulk_prefix = ''.join([c for c in bulk_name if c.isalnum()])[:3].upper()
        # Format the date as YYYYMMDD
        current_date = datetime.now().strftime("%Y%m%d")
        # Query the database for the total number of bulk entries to get an index
        total_count = crud.session.query(Bulk).count() + 1
        # Generate a random number of specified length
        random_number = random.randint(100, 999)  # three-digit random number for uniqueness
        # Construct the batch number
        return f"BULK-{bulk_prefix}-{current_date}-{total_count}-{random_number}"
    def dropdown_changed(self, event):
        selected_option = next((opt for opt in self.bulk_name.options if opt.key == event.control.value), None)
        if selected_option:
            self.selected_key = selected_option.key
            self.selected_text = selected_option.text
        else:
            self.selected_key = None
            self.selected_text = None
            print("Selected item not found.")

    def get_grains(self):
        # Fetching options using the fetch_for_dropdown method
        grain_options = self.crud.fetch_for_dropdown(GrainTable, 'gra_name', 'gra_batchid')

        # Convert the dictionaries to Option objects
        #options = [dropdown.Option(text=option["text"], value=option["value"]) for option in spore_options]
        options = [dropdown.Option(key=str(option["value"]), text=option["text"]) for option in grain_options]
        return options

    # def get_spores(self):
    #     spore_query=self.crud.read(Spores)
    #     options = Options(self.crud.fetch_for_dropdown(Spores, 'spore_name', 'spore_id')
    #     return options
    def populate_options(self):
        self.bulk_name.options = self.get_grains()
        self.bulk_name.update()

    def add_bulk(self):
        if self.selected_key:
            # Generate a unique batch number for the new bulk entry
            bulk_batch_id = self.generate_bulk_batch_number(self.crud, self.selected_text)

            try:
                new_bulk = Bulk(
                    bulk_batch=bulk_batch_id,
                    bulk_name=self.selected_text,
                    bulk_quantity=10,  # Assuming a default quantity or capturing from UI.
                    bulk_date=date.today()
                )
                self.crud.create(new_bulk)
                self.confirm_add()
            except Exception as e:
                print(f"An error occurred while adding bulk: {e}")
        else:
            print("Please select a grain before submitting.")

    def confirm_add(self):
        # Reset the inputs to default states
        self.bulk_name.value = ''
        self.bulk_name.update()

        self.bulk_notes.value = ''
        self.bulk_notes.update()

        # Optionally reset other fields if necessary

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
                  content=Column(controls=[self.bulk_name,self.bulk_notes,self.bulk_date,self.bulk_submit])
              )
                  ]
          )
              )

            ]
          )
