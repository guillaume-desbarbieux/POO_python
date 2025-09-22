% rebase('base.tpl')

<h3>Edit person: {{person.first_name}} {{person.family_name}}</h3>

<form action="/edit/{{person.id}}" method="post">
    <fieldset style="width: 50%; margin: auto; padding: 1em;">
        <legend><strong>Personal Information</strong></legend>
        <table>
            <tr>
                <td><label for="family_name">Nom de Famille :</label></td>
                <td><input type="text" id="family_name" name="family_name" maxlength="100" required value="{{person.family_name}}"></td>
            </tr>
            <tr>
                <td><label for="first_name">Prénom :</label></td>
                <td><input type="text" id="first_name" name="first_name" maxlength="100" required value="{{person.first_name}}"></td>
            </tr>
            <tr>
                <td><label>Date de naissance :</label></td>
                <td>
                    <input type="number" name="day" min="1" max="31" placeholder="Jour" required value="{{person.birth_date.day}}">
                    <input type="number" name="month" min="1" max="12" placeholder="Mois" required value="{{person.birth_date.month}}">
                    <input type="number" name="year" min="1900" max="2100" placeholder="Année" required value="{{person.birth_date.year}}">
                </td>
            </tr>
        </table>
    </fieldset>

    <fieldset style="width: 50%; margin: auto; padding: 1em; margin-top: 1em;">
        <legend><strong>Contact</strong></legend>
        <table>
            <tr>
                <td><label for="phone">Téléphone :</label></td>
                <td><input type="tel" id="phone" name="phone" maxlength="20" required value="{{person.contact.phone_number}}"></td>
            </tr>
            <tr>
                <td><label for="email">Email :</label></td>
                <td><input type="email" id="email" name="email" maxlength="100" required value="{{person.contact.email}}"></td>
            </tr>
        </table>
    </fieldset>

    <fieldset style="width: 50%; margin: auto; padding: 1em; margin-top: 1em;">
        <legend><strong>Adresse</strong></legend>
        <table>
            <tr>
                <td><label for="address">Adresse :</label></td>
                <td><input type="text" id="address" name="address" maxlength="100" required value="{{person.postal_address.address}}"></td>
            </tr>
            <tr>
                <td><label for="postal_code">Code Postal :</label></td>
                <td><input type="number" id="postal_code" name="postal_code" min="1000" max="99999" required value="{{person.postal_address.postal_code}}"></td>
            </tr>
            <tr>
                <td><label for="town">Ville :</label></td>
                <td><input type="text" id="town" name="town" maxlength="100" required value="{{person.postal_address.town}}"></td>
            </tr>
        </table>
    </fieldset>

    <p style="text-align: center; margin-top: 1em;">
        <input type="submit" name="save" value="Mettre à jour">
    </p>
</form>
