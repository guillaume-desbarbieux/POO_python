%rebase('base.tpl')

<h3>My Repertory</h3>
<table border="1">
    <tr>
        <th> </th>
        <th> </th>
        <th>First name</th>
        <th>Family name</th>
        <th>Birth date</th>
        <th>Phone</th>
        <th>Email</th>
        <th>Address</th>
    </tr>
    %for person in repertory.people:
    <tr>
        <td><a href={{"/remove/"+str(person.id)}}>Supp</a></td>
        <td><a href={{"/edit/"+str(person.id)}}>Edit</a></td>
        <td>{{person.first_name}}</td>
        <td>{{person.family_name}}</td>
        <td>{{person.birth_date.day}} / {{person.birth_date.month}} / {{person.birth_date.year}}</td>
        <td>{{person.contact.phone_number}}</td>
        <td>{{person.contact.email}}</td>
        <td>{{person.postal_address.address}} {{person.postal_address.postal_code}} {{person.postal_address.town}}</td>
    </tr>
    %end
</table>

<a href="/new">Add a new person</a>