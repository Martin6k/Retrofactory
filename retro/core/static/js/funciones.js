function val_nom(){
    var nom = document.getElementById("nombre").value;
    if (String(nom).length > 0){
        document.getElementById("nombre").style.border= "5px solid green";
    }else{
        var res = document.getElementById("nombre");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
            "El campo esta vacío</div>";
    }
}
function val_rut(){
    var rut = document.getElementById("rut").value;
    if (String(rut).length >= 9 && String(rut).length <= 10){
        document.getElementById("rut").style.border= "5px solid green";
    }else{
        var res = document.getElementById("rut");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger mx-auto text-center'>" +
        "El rut no es válido</div>"
    }
    
}
function val_fono(){
    var fono = document.getElementById("fono").value;
    if (String(fono).length >= 9 && String(fono).length <= 12){
        document.getElementById("fono").style.border= "5px solid green";
    }else{
        var res = document.getElementById("fono");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
        "El teléfono no es válido</div>"
    }
    
}
function val_correo(){
    var correo = document.getElementById("correo").value;
    if (String(correo).includes('@gmail.com')){
        document.getElementById("correo").style.border= "5px solid green";
    }else{
        var res = document.getElementById("correo");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
        "El correo no es válido</div>"
    }
    
}
function val_edad(){
    var edad = document.getElementById("edad").value;
    if (Number(edad) >= 18){
        document.getElementById("edad").style.border= "5px solid green";
    }else{
        var res = document.getElementById("edad");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
        "debes ser mayor de edad</div>"
    }
    
}
function val_razon(){
    var razon = document.getElementById("razon").value;
    if(Number(razon) >= 2 && Number(razon) <= 4){
        document.getElementById("razon").style.border= "5px solid green";
    }else{
        var res = document.getElementById("razon");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger  mx-auto text-center'>" +
        "Seleccione una opcion valida</div>"
    }
    
}