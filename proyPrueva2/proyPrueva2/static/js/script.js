//Aqui esta un script que es ejecutado al cargar la pagina con el metodo onload
$(document).ready(inicio);
function inicio(){
    var texto=$("#tbuscar").keypress(Enviar);
}
function Enviar(){
    var texto=this.value;
    $.ajax({
        type:"POST",
        url:"/buscar/",
        data:$("#fbuscar").serialize(),
        success:resultado,
        error:errores
    });
}
function resultado(data){
    //$("#dresultado").text(data);
    $("#dresultado").html(data);
}
function errores(){
    $("#dresultado").text("Error en el servidor");
}