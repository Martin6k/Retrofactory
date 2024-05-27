function valicuenta(){ 
    var email = document.getElementById("email").value;
    var pass = document.getElementById("contrasena").value;
    if((email.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/))){
        if(String(pass).length >= 8 && String(pass).length <= 15){
            /* a */
            document.getElementById("email").style.border = "1px solid lightgrey";
            document.getElementById("contrasena").style.border = "1px solid lightgrey";
            document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-success w-50 mx-auto text-center'>" +
            "Validado exitosamente</div>"
            /* b */
            document.getElementById("resultado").innetHTML = "<div style='margin-top: 2%' class='alert alert-success w-50 mx-auto text-center'>" +
            "Cuenta creada con exito</div>"
        } else {
            document.getElementById("contrasena").style.border = "1px solid red";
            document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-danger w-50 mx-auto text-center'>" +
                    "Contraseña debe tener minimo 8 caracteres</div>"
        }
    } else {
        document.getElementById("email").style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div style='margin-top: 2%' class='alert alert-danger w-50 mx-auto text-center'>El correo debe ser valido</div>"

    }
} 