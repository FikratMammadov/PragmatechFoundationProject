// CRUD
// C -Create
// R- Read
// U- Update
// D- Delete

let name=document.querySelector('#name');
let surname = document.querySelector("#surname");
let email  =document.querySelector('#email');
let t = document.querySelector('tbody');
users=[]
count=1;
function getFormData(event){
    event.preventDefault();
    // tr = `
    // <tr>
    //     <td scope="row">1</td>
    //     <td>${name.value}</td>
    //     <td>${surname.value}</td>
    //     <td>${email.value}</td>
    // </tr>
    // `;
    users.push({
        id:count,
        ad:name.value,
        soyad:surname.value,
        email = email.value
    });
     count++;
}

function showData(event){
    event.preventDefault();
    t_content="";
    for(i=0;i<users.length;i++){
        tr = `
    <tr>
        <td scope="row">1</td>
        <td>${users[i].ad}</td>
        <td>${users[i].surname}</td>
        <td>${users[i].email}</td>
    </tr>
    `;

        t_content+=tr;
    }
    t.innerHTML=t_content;
}