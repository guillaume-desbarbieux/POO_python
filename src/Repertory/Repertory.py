from datetime import datetime
from dataclasses import dataclass, field

from pygments.lexer import default


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
    _counter:int = field(init = False, default = 0, repr = False)

    id : int = field(init=False)
    family_name : str
    first_name : str
    birth_date : datetime
    contact : Contact
    postal_address : PostalAddress

    def __post_init__(self):
        type(self)._counter += 1
        self.id = type(self)._counter

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
        return "\n\n".join(str(person) for person in self.people)

    def remove(self, id):
        self.people = [person for person in self.people if person.id != id]


if __name__ == "__main__":

    geraud = Person("Yakou", "Geraud", datetime(2000, 1, 1), Contact("06.06.06.06.06", "geraud@yakou.com"), PostalAddress("1 rue du Parc", 26000, "Valence"))

    sylvain = Person("Teissier", "Sylvain", datetime(1990, 2, 2), Contact("06.06.06.06.07", "sylvain@cemantix.com"),
                     PostalAddress("1 rue du Fleuve", 26100, "Montelimar"))

    killian = Person("Pujol", "Killian", datetime(2020, 3, 3), Contact("06.06.06.06.08", "killian@degeulasse.com"),
                     PostalAddress("1 rue du Pic", 26200, "Romans"))


    rep1 = Repertory([geraud, sylvain])
    rep1.add(killian)

    print(rep1)