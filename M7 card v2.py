
from faker import Faker
 
fake = Faker()
 
 
class BaseContact:
    def __init__(self, first_name, last_name, email, private_phone_number, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.private_phone_number = private_phone_number
 
        self._label_lenght = 0
 
    def __repr__(self):
        return f"{self.first_name, self.last_name}"
 
    @property
    def label_lenght(self):
        self._label_lenght = print(f"Długość imienia i nazwiska to: {(len(self.first_name)) + (len(self.last_name))}")
        return self._label_lenght
 
    def contact(self):
        print(f'Wybieram prywatny numer {self.private_phone_number} i dzwonię do {self.first_name} {self.last_name}')
 
 
class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.business_phone_number = business_phone_number
 
    def contact(self):
        print(f'Wybieram numer służbowy {self.business_phone_number} i dzwonię do {self.first_name} {self.last_name}')
 
 
cards = []
 
 
def create_contacts(contact_class):
    kwargs = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'private_phone_number': fake.phone_number(),
        'business_phone_number': fake.phone_number(),
        'job': fake.job(),
        'company': fake.company(),
        'number': fake.random_int(min=1, max=10)
    }
 

    card = contact_class(**kwargs)
    cards.append(card)
  
create_contacts(BaseContact)
create_contacts(BusinessContact)
 
for contact in cards:
    contact.contact()
