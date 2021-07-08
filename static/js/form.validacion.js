$(document).ready(function() {
    $("#contact-form").validate({
      rules: {
        name : {
          required: true,
          minlength: 3
        },
        rut : {
          required: true,
          number: true,
        },
        email: {
          required: true,
          email: true
        },
        transporte: {
            required: true,
        },
        alojamiento: {
            required: true,
        },
        cmbTours:{
            required: true,            
        },
        cmbTiempotours:{
          required: true,            
      },
        calendario:{
          required: true,
        }
      
      },
      messages : {
        name: {
          minlength: "El nombre debe de tener al menos 3 caracteres de largo"
        },
        rut: {
            required: "Ingrese un rut valido"
        },
        email: {
          required: "Por favor, escriba una dirección de correo válida",

        },
        transporte: {
            required: "Debe ingresar tipo de transporte",
        },
        cmbTours:{
            required: "Debe seleccionar el tour que desea",
            
        },
        cmbTiempotours:{
          required: "Debe seleccionar el tour que desea",

        }
      }
    });
  });


      $('input#rut')
      .keypress(function (event) {
        if (this.value.length === 9) {
          return false;
        }
      });

