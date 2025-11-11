let emailField = document.getElementById("txtEmail");
let nameField = document.getElementById("txtName");
let phoneNumField = document.getElementById("txtPhoneNum");
let passwordField = document.getElementById("txtPassword");
let confirmField = document.getElementById("txtConfirm");
let buttonSubmit = document.getElementById("buttonSubmit");

buttonSubmit.addEventListener('click', function(){
    
    let rowClasses = document.getElementsByClassName('row');
    if(rowClasses.length > 0) {
        for(let i=0; i<rowClasses.length; i++) {
            if (rowClasses[i].getElementsByTagName('span').length > 0 ) {
                rowClasses[i].removeChild(rowClasses[i].
                    getElementsByTagName('span')[0]);
            }
        }
    }

    if( emailField.value == "") {
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Email field is required.";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = emailField.parentElement;
        parentElement.appendChild(spanElement);


    }
    if( nameField.value == ""){
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Name field is required.";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = nameField.parentElement;
        parentElement.appendChild(spanElement);
    }
    if( phoneNumField.value == ""){
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Phone number is required.";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = phoneNumField.parentElement;
        parentElement.appendChild(spanElement);
    }
    if( passwordField.value == ""){
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Password is required.";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = passwordField.parentElement;
        parentElement.appendChild(spanElement);
    }
    if( confirmField.value == ""){
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Please confirm your password.";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = confirmField.parentElement;
        parentElement.appendChild(spanElement);
    }
    if(confirmField.value != passwordField.value && confirmField.value != ""){
        let spanElement = document.createElement('span');
        spanElement.innerHTML = "Your password is incorrect";
        spanElement.style.color = "red";
        spanElement.style.fontSize = "13px";

        let parentElement = confirmField.parentElement;
        parentElement.appendChild(spanElement);
    }

});