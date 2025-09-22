% rebase('base.tpl')

<h3>Add a new person to the Repertory</h3>

<form action="/new" method="post">
    <fieldset style="width: 50%; margin: auto; padding: 1em;">
        <legend><strong>Personal Information</strong></legend>
        <table>
            <tr>
                <td><label for="family_name">Nom de Famille :</label></td>
                <td><input type="text" id="family_name" name="family_name" maxlength="100" required></td>
            </tr>
            <tr>
                <td><label for="first_name">Prénom :</label></td>
                <td><input type="text" id="first_name" name="first_name" maxlength="100" required></td>
            </tr>
            <tr>
                <td><label>Date de naissance :</label></td>
                <td>
                    <input type="number" name="day" min="1" max="31" placeholder="Jour" required>
                    <input type="number" name="month" min="1" max="12" placeholder="Mois" required>
                    <input type="number" name="year" min="1900" max="2100" placeholder="Année" required>
                </td>
            </tr>
        </table>
    </fieldset>

    <fieldset style="width: 50%; margin: auto; padding: 1em; margin-top: 1em;">
        <legend><strong>Contact</strong></legend>
        <table>
            <tr>
                <td><label for="phone">Téléphone :</label></td>
                <td><input type="tel" id="phone" name="phone" maxlength="20" required></td>
            </tr>
            <tr>
                <td><label for="email">Email :</label></td>
                <td><input type="email" id="email" name="email" maxlength="100" required></td>
            </tr>
        </table>
    </fieldset>

    <fieldset style="width: 50%; margin: auto; padding: 1em; margin-top: 1em;">
        <legend><strong>Adresse</strong></legend>
        <table>
            <tr>
                <td><label for="address">Adresse :</label></td>
                <td><input type="text" id="address" name="address" maxlength="100" required></td>
            </tr>
            <tr>
                <td><label for="postal_code">Code Postal :</label></td>
                <td><input type="number" id="postal_code" name="postal_code" min="1000" max="99999" required></td>
            </tr>
            <tr>
                <td><label for="town">Ville :</label></td>
                <td><input type="text" id="town" name="town" maxlength="100" required></td>
            </tr>
        </table>
    </fieldset>

    <p style="text-align: center; margin-top: 1em;">
        <input type="submit" name="save" value="Enregistrer">
    </p>
</form>
