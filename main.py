from faker import Faker
fake = Faker()



class BaseContact:
    def __init__(self, first_name, last_name, email, private_phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.private_phone_number= private_phone_number

        self._label_lenght = 0
    @property
    def label_lenght(self):
        self._label_lenght = print(f"Długość imienia i nazwiska to: {(len(self.first_name)) +(len(self.last_name))}")
        return self._label_lenght

    
    def contact(self):
        print(f'Wybieram prywatny numer {self.private_phone_number} i dzwonię do {self.first_name} {self.last_name}')
        

class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.company =company
        self.job = job
        self.business_phone_number = business_phone_number
  
    def contact_business(self):
        print(f'Wybieram numer służbowy {business_phone_number} i dzwonię do {first_name} {last_name}')
    
def create_contacts(type):  
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    private_phone_number = fake.phone_number() 
    business_phone_number = fake.phone_number()
    job = fake.job()
    company = fake.company()
    number = fake.random_int(min = 1, max = 10)
  # do cards powininienes dodawac aktualna klase BaseContact, BusinessContact
    if type == "BaseContact":
        card = BaseContact(...)
    elif type == "BusinessContact":
        card = BusinessContact(...)
    cards.append(card)                                             

cards = [] 

person_one = BusinessContact(first_name, last_name, email, private_phone_number, company, job, business_phone_number)

person_one.contact()
person_one.contact_business()
person_one.label_lenght

print()

create_contacts("BaseContact")
create_contacts("BusinessContact")

