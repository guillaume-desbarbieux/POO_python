from datetime import datetime

from src.Repertory.Repertory import Repertory, Person, Contact, PostalAddress

if __name__ == "__main__":

    geraud = Person("Yakou", "Geraud", datetime(2000, 1, 1), Contact("06.06.06.06.06", "geraud@yakou.com"), PostalAddress("1 rue du Parc", 26000, "Valence"))

    sylvain = Person("Teissier", "Sylvain", datetime(1990, 2, 2), Contact("06.06.06.06.07", "sylvain@cemantix.com"),
                     PostalAddress("1 rue du Fleuve", 26100, "Montelimar"))

    killian = Person("Pujol", "Killian", datetime(2020, 3, 3), Contact("06.06.06.06.08", "killian@degeulasse.com"),
                     PostalAddress("1 rue du Pic", 26200, "Romans"))


    rep1 = Repertory([geraud, sylvain])
    rep1.add(killian)

    print(rep1)