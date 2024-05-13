function valicuenta(){ 
    var email = document.getElementById("email").value;
    var pass = document.getElementById("contrasena").value;
    if(String(email).includes('@gmail.com') || String(email).includes('@yahoo.com') || String(email).includes('@outlook.com') || String(email).includes('@hotmail.com')){
        if(String(pass).length >= 8 && String(pass).length <= 15){
            /* a */
            document.getElementById("email").style.border = "1px solid lightgrey";
            document.getElementById("contrasena").style.border = "1px solid lightgrey";
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