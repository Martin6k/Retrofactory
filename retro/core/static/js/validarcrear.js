function v_mail(){
    var email = document.getElementById("email").value;
    if((email.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/))){
        document.getElementById("email").style.border = "1px solid lightgrey";
    }else{
        document.getElementById("email").style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-danger w-50 mx-auto text-center'>El correo debe ser valido</div>"
    }
}

function v_pass(){
    var pass = document.getElementById("contrasena").value;
    if(String(pass).length >= 8 && String(pass).length <= 15){
        document.getElementById("contrasena").style.border = "1px solid lightgrey";
    }else{
        document.getElementById("contrasena").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-danger w-50 mx-auto text-center'>" +
        "Contraseña debe tener minimo 8 caracteres</div>"
    }
    return pass;
}
function v_pass2(pass){
    var pass2 = document.getElementById("contrasena2").value;
    if (String(pass2)=String(pass)){
        document.getElementById("contrasena").style.border = "1px solid lightgrey";
    }else{
        document.getElementById("contrasena").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-danger w-50 mx-auto text-center'>" +
        "Las contraseñas deben ser iguales</div>"
    }
}

function validar_e() {
    var e = document.getElementById("correo-e").value;

    if (e.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        document.getElementById("correo-e").style.border= "5px solid green";
    } else {
        document.getElementById("correo-e").style.border= "5px solid red";
        document.getElementById("resultado").innerHTML= "<div class='alert alert-danger w-60 mx-auto text-center'>" +"El correo ingresado no es valido</div>";
    }
}

function validar_c(){
    var c = document.getElementById("clave").value;

    if (String(c).length >= 8 && String(c).length <= 15) {
        document.getElementById("clave").style.border= "5px solid green";
    }else{
        document.getElementById("clave").style.border= "5px solid red";
        document.getElementById("resultado").innerHTML="<div class='alert alert-danger w-60 mx-auto text-center'>" +"La contraseña debe tener al menos 8 caracteres</div>";
    }
}