from datetime import datetime
from bottle import Bottle, template, redirect, request
from src.Repertory.Repertory import Repertory, Person, Contact, PostalAddress

app = Bottle()


@app.get('/')
def index():
    redirect('/repertory')


@app.get('/repertory')
def display_repertory():
    return template('show_repertory.tpl', repertory=repertory)


@app.route('/new', method=['GET', 'POST'])
def new_person():
    if request.POST:
        repertory.add(Person(request.forms.family_name, request.forms.first_name,
                             datetime(int(request.forms.year), int(request.forms.month), int(request.forms.day)),
                             Contact(request.forms.phone, request.forms.email),
                             PostalAddress(request.forms.address, request.forms.postal_code, request.forms.town)))
        return redirect('/repertory')
    else:
        return template('new_person.tpl')


@app.route('/edit/<id:int>', method=['GET', 'POST'])
def edit_person(id):
    person = next((p for p in repertory.people if p.id == id), None)
    if not person:
        return "Person not found"

    if request.POST:
        person.family_name = request.forms.family_name
        person.first_name = request.forms.first_name
        person.birth_date = datetime(
            int(request.forms.year),
            int(request.forms.month),
            int(request.forms.day))
        person.contact.phone_number = request.forms.phone
        person.contact.email = request.forms.email
        person.postal_address.address = request.forms.address
        person.postal_address.postal_code = int(request.forms.postal_code)
        person.postal_address.town = request.forms.town
        return redirect('/repertory')
    else:
        return template('edit_person.tpl', person=person)

@app.route('/remove/<id:int>', method=['GET', 'POST'])
def remove_person(id):
    person = next((p for p in repertory.people if p.id == id), None)
    if not person:
        return "Person not found"
    else:
        repertory.remove(id)
        return redirect('/repertory')


if __name__ == '__main__':
    geraud = Person("Yakou", "Geraud", datetime(2000, 1, 1), Contact("06.06.06.06.06", "geraud@yakou.com"),
                    PostalAddress("1 rue du Parc", 26000, "Valence"))

    sylvain = Person("Teissier", "Sylvain", datetime(1990, 2, 2), Contact("06.06.06.06.07", "sylvain@cemantix.com"),
                     PostalAddress("1 rue du Fleuve", 26100, "Montelimar"))

    killian = Person("Pujol", "Killian", datetime(2020, 3, 3), Contact("06.06.06.06.08", "killian@degeulasse.com"),
                     PostalAddress("1 rue du Pic", 26200, "Romans"))

    repertory = Repertory([geraud, sylvain, killian])
    app.run(host='localhost', port=8080, debug=True, reloader=True)