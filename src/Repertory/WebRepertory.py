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


if __name__ == '__main__':
    geraud = Person("Yakou", "Geraud", datetime(2000, 1, 1), Contact("06.06.06.06.06", "geraud@yakou.com"),
                    PostalAddress("1 rue du Parc", 26000, "Valence"))

    sylvain = Person("Teissier", "Sylvain", datetime(1990, 2, 2), Contact("06.06.06.06.07", "sylvain@cemantix.com"),
                     PostalAddress("1 rue du Fleuve", 26100, "Montelimar"))

    killian = Person("Pujol", "Killian", datetime(2020, 3, 3), Contact("06.06.06.06.08", "killian@degeulasse.com"),
                     PostalAddress("1 rue du Pic", 26200, "Romans"))

    repertory = Repertory([geraud, sylvain])
    app.run(host='localhost', port=8080, debug=True, reloader=True)
