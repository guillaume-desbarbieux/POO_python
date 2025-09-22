import datetime
from dataclasses import dataclass

@dataclass()
class Contact:
    phone_number : str
    email : str

    def __str__(self):
        return f"{self.phone_number} {self.email}"

@dataclass()
class PostalAddress:
    address : str
    postal_code : int
    town : str

    def __str__(self):
        return f"{self.address} {self.postal_code} {self.town}"

@dataclass()
class Person:
    family_name : str
    first_name : str
    birth_date : datetime.datetime
    contact : Contact
    postal_address : PostalAddress

    def __str__(self):
        return f"""{self.first_name} {self.family_name} ({self.birth_date.day}/{self.birth_date.month}/{self.birth_date.year})
{str(self.contact)}
{str(self.postal_address)}"""

@dataclass
class Repertory:
    people: list[Person]

    def add(self, person):
        if isinstance(person, Person):
            self.people.append(person)

    def __str__(self):
        answer = ""
        for person in self.people:
            answer += str(person) + "\n\n"
        return answer