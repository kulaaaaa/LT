from faker import Faker
fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
private_phone_number = fake.phone_number() 
business_phone_number = fake.phone_number()
job = fake.job()
company = fake.company()
number = fake.random_int(min = 1, max = 10)
class BaseContact:
    def __init__(self, first_name, last_name, email, private_phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.private_phone_number= private_phone_number

        self._label_lenght = 0
    @property
    def label_lenght(self):
        self._label_lenght = print(f"Długość imienia i nazwiska to: {(len(first_name)) +(len(last_name))}")
        return self._label_lenght

    
    def contact(self):
        print(f'Wybieram prywatny numer {private_phone_number} i dzwonię do {first_name} {last_name}')
        

class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.company =company
        self.job = job
        self.business_phone_number = business_phone_number
  
    def contact_business(self):
        print(f'Wybieram numer służbowy{business_phone_number} i dzwonię do {first_name} {last_name}')
    
def create_contacts(type, first_name, last_name, email, private_phone_number=None, company=None, job=None, business_phone_number=None):   
    if type == BaseContact:
        base_card = (f'Prywatna wizytówka {first_name} {last_name} {email}')
        cards.append(base_card)
    elif type == BusinessContact:
        business_card = (f'Służbowa wizytówka {first_name} {last_name} {email}')
        cards.append(business_card)                                             

cards = [] 

person_one = BusinessContact(first_name, last_name, email, private_phone_number, company, job, business_phone_number)

person_one.contact()
person_one.contact_business()
person_one.label_lenght

print()

create_contacts(BaseContact, first_name, last_name, email)
create_contacts(BusinessContact, first_name, last_name, email)
for i in range(number):
    print(cards)
print(f'Liczba wizytówek na każdy rodzaj to {number}')

