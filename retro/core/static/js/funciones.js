function validacion_form(){
    var nom = document.getElementById("nombre").value;
    var rut = document.getElementById("rut").value;
    var fono = document.getElementById("fono").value
    var correo = document.getElementById("correo").value;
    var edad = document.getElementById("edad").value;
    var razon = document.getElementById("razon").value;
    //validacion nombre
    if (String(nom).length > 0){
        //validacion rut
        if (String(rut).length >= 9 && String(rut).length <= 10) {
            //validacion fono
            if (String(fono).length >= 9 && String(fono).length <= 12) {
                //validacion correo
                if (String(correo).includes('@gmail.com')) {
                    //validacion edad
                    if (Number(edad) >= 18){
                        //validar el fono
                        if(Number(razon) >= 2 && Number(razon) <= 4){
                            var res = document.getElementById("razon");
                            res.style.border = "1px solid green"
                            document.getElementById("resultado").innerHTML = "<div class='alert alert-success  mx-auto text-center'>" +
                            "formulario completo</div>"
                        }else{
                            var res = document.getElementById("razon");
                            res.style.border = "1px solid red"
                            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
                                "Seleccione una opcion valida</div>"
                        }
                    }else{
                        var res = document.getElementById("edad");
                        res.style.border = "1px solid red"
                        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
                            "debes ser mayor de edad</div>"
                    }
                }else {
                    var res = document.getElementById("correo");
                    res.style.border = "1px solid red"
                    document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
                        "El correo no es válido</div>"
                }
            }else {
                var res = document.getElementById("fono");
                res.style.border = "1px solid red"
                document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
                    "El teléfono no es válido</div>"
            }
        }else {
            var res = document.getElementById("rut");
            res.style.border = "1px solid red"
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger mx-auto text-center'>" +
                "El rut no es válido</div>"
        }
    }else {
        var res = document.getElementById("nombre");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
            "El campo esta vacío</div>";
    }
}

function validacion_ini(){
    var mail = document.getElementById("email").value;
    var con = document.getElementById("pass").value;
    if(String(mail).includes('@gmail.com')){
        if(String(con).length >= 8 && String(con).length <= 15){
            var res = document.getElementById("pass");
            res.style.border = "1px solid green"
            document.getElementById("resultado").innerHTML = "<div class='alert alert-success  mx-auto text-center'>" +
            "Sesión iniciada</div>"
        }else{
            var res = document.getElementById("pass");
            res.style.border = "1px solid red"
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
                "La contraseña debe tener entre 8 y 15 caracteres</div>";
        }
    }else{
        var res = document.getElementById("email");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
            "El correo no es válido</div>"
    }
}