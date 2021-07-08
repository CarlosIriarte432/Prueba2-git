
// notacion abreviada
$(function () {
    $("#submit-form").click(function (event) {
        event.preventDefault();

        var nombre = $("#nombre").val();
        var rut = $("#rut").val();
        var correo = $("#correo").val();
        var transporte = $("#transporte").val();
        var hotel = $("#hotel").val();
        var tour = $("#tour").val();
        var fecha = $("#fecha").val();

        var fila = '<tr><th>' + nombre + '</th><th>' + rut + '</th><th>' + correo + '</th><th>' + transporte + '</th><th>' + hotel + '</th></tr>' + tour + '</th></tr>' + fecha + '</th></tr>';

        $('#tablaprueba>tbody').append(fila);

        var documento = $("#tablaprueba");
        documento.css("background-color", "#7584");

    });
    //   cierre del click de submint
});
//   cierre del ready

