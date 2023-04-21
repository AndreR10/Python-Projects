$(document).ready(function () {
  let datum1;
  let datum2;
  let datum1_name;
  let datum2_name;
  let transform;
  $(".inputCoord").hide();
  // Escolha do sistema de coordenadas
  $("#selectEntrada, #selectSaida, #selectTrans").change(function () {
    datum1 = $("#selectEntrada option:selected").val();
    datum2 = $("#selectSaida option:selected").val();

    datum1_name = $("#selectEntrada option:selected").text();
    datum2_name = $("#selectSaida option:selected").text();
    transform = $("#selectTrans option:selected").text();

    console.log(datum1);
    console.log(datum2);
    console.log(datum1_name);
    console.log(datum2_name);
    console.log(transform);

    $("#transform").toggle(datum1 !== datum2);
    if (datum1 === "4" && datum2 === "4") {
      // $("#fuso").prop('disabled', false);
      $("#fuso").removeAttr("disabled");
    } else {
      if ($("#fuso").is(":enabled")) {
        //input fuso is enabled
        $("#fuso").attr("disabled", "disabled");
      }
    }
  });

  // Escolha do tipo de coordenadas de entrada e saida
  $("#selectCoord").change(function () {
    $(".inputCoord").hide();

    if (
      $("#selectCoord option:selected").text() === "Cartesianas/Geográficas"
    ) {
      //----------------------------------------------------------
      // Cartesianas/Geográficas (Opção 1)
      //----------------------------------------------------------
      console.log("Cartesianas/Geográficas (Opção 1)");
      $("#inputCart").show();
    } else if (
      $("#selectCoord option:selected").text() === "Cartesianas/Retangulares"
    ) {
      //----------------------------------------------------------
      // Cartesianas/Retangulares (Opção 2)
      //----------------------------------------------------------
      console.log("Cartesianas/Retangulares (Opção 2)");
      $("#inputCart").show();
      $("#inputHFuso").show();
      if ($("#h").is(":enabled")) {
        //input h is enabled
        $("#h").attr("disabled", "disabled");
      }
    } else if (
      $("#selectCoord option:selected").text() === "Geográficas/Retangulares"
    ) {
      //----------------------------------------------------------
      // Geográficas/Retangulares (Opção 3)
      //----------------------------------------------------------
      console.log("Geográficas/Retangulares (Opção 3)");
      $("#inputGeo").show();
      $("#inputHFuso").show();
      if ($("#h").is(":enabled")) {
        //input h is enabled
        $("#h").attr("disabled", "disabled");
      }
    } else if (
      $("#selectCoord option:selected").text() === "Geográficas/Cartesianas"
    ) {
      console.log("Geográficas/Cartesianas (Opção 4)");
      $("#inputGeo").show();
      $("#inputHFuso").show();
      $("#h").removeAttr("disabled");
    } else if (
      $("#selectCoord option:selected").text() === "Retangulares/Geográficas"
    ) {
      console.log("Retangulares/Geográficas (Opção 5)");
      $("#inputRetan").show();
      $("#inputHFuso").show();
      if ($("#h").is(":enabled")) {
        //input h is enabled
        $("#h").attr("disabled", "disabled");
      }
    } else if (
      $("#selectCoord option:selected").text() === "Retangulares/Cartesianas"
    ) {
      console.log("Retangulares/Cartesianas (Opção 6)");
      $("#inputRetan").show();
      $("#inputHFuso").show();
      $("#h").removeAttr("disabled");
    } else if (
      $("#selectCoord option:selected").text() === "Retangulares/Retangulares"
    ) {
      console.log("Retangulares/Retangulares (Opção 9)");
      $("#inputRetan").show();
      $("#inputHFuso").show();
      $("#h").removeAttr("disabled");
    } else if (
      $("#selectCoord option:selected").text() === "Geográficas/Geográficas"
    ) {
      console.log("Geográficas/Geográficas (Opção 5)");
      $("#inputGeo").show();
      $("#inputHFuso").show();
      $("#h").removeAttr("disabled");
    } else if (
      $("#selectCoord option:selected").text() === "Cartesianas/Cartesianas"
    ) {
      //----------------------------------------------------------
      // Cartesianas/Cartesianas (Opção 1)
      //----------------------------------------------------------
      console.log("Cartesianas/Retangulares (Opção 2)");
      $("#inputCart").show();
      $("#inputHFuso").show();
      if ($("#h").is(":enabled")) {
        //input h is enabled
        $("#h").attr("disabled", "disabled");
      }
    }
  });

  $("#form").on("submit", function (e) {
    $("ul").empty();

    var coord = {};

    // Adiciona ao dicionário a key e value de cada input que se encontra visivel
    $(".inputCoord:visible :input").each(function () {
      coord[$(this).attr("name")] = $(this).val();
    });

    // Verificar se é opção 1 ou 2
    if (datum1 === datum2) {
      // Transformação no mesmo datum

      coord["datum"] = datum1;
      console.log(coord);

      if (
        $("#selectCoord option:selected").text() === "Cartesianas/Geográficas"
      ) {
        //----------------------------------------------------------
        // Cartesianas/Geográficas (Opção 1)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/cart_geo",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();
      } else if (
        $("#selectCoord option:selected").text() === "Cartesianas/Retangulares"
      ) {
        //----------------------------------------------------------
        // Cartesianas/Retangulares (Opção 2)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/cart_ret",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();
      } else if (
        $("#selectCoord option:selected").text() === "Geográficas/Retangulares"
      ) {
        //----------------------------------------------------------
        // Geográficas/Retangulares (Opção 3)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/geo_ret",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();
      } else if (
        $("#selectCoord option:selected").text() === "Geográficas/Cartesianas"
      ) {
        //----------------------------------------------------------
        // Geográficas/Cartesianas (Opção 4)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/geo_cart",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();

        //----------------------------------------------------------
        // Retangulares/Geográficas (Opção 5)
        //----------------------------------------------------------
      } else if (
        $("#selectCoord option:selected").text() === "Retangulares/Geográficas"
      ) {
        //----------------------------------------------------------
        // Retangulares/Geográficas (Opção 5)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/ret_geo",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();
      } else if (
        $("#selectCoord option:selected").text() === "Retangulares/Cartesianas"
      ) {
        //----------------------------------------------------------
        // Retangulares/Cartesianas (Opção 6)
        //----------------------------------------------------------
        $.ajax({
          data: JSON.stringify(coord),
          type: "POST",
          url: "/ret_cart",
          contentType: "application/json",
          dataType: "json",
          success: function (result) {
            console.log(result);
          },
          error: function (request, status, error) {
            console.log(request.responseText);
            console.log(request.error);
          },
        }).done(function (data) {
          var resultList = $("#output");
          $.each(data, function (key, value) {
            console.log(key);
            console.log(value);
            var li = $("<li/>")
              .addClass("list-group-item d-flex justify-content-between")
              .appendTo(resultList);
            var span = $("<span/>").addClass("fw-bold").text(key).appendTo(li);
            var p = $("<p/>").text(value).appendTo(li);
          });
        });
        e.preventDefault();
      }
    } else {
      // Transformação em datums diferentes
      coord["datum1"] = datum1;
      coord["datum2"] = datum2;

      coord["datum1_name"] = datum1_name;
      coord["datum2_name"] = datum2_name;

      coord["transform"] = transform;

      console.log(coord);

      if (transform === "Bursa-Wolf") {
        console.log("Bursa-Wolf");
        if (
          $("#selectCoord option:selected").text() ===
          "Retangulares/Retangulares"
        ) {
          //----------------------------------------------------------
          // Retangulares/Retangulares (Opção 9)
          //----------------------------------------------------------
          $.ajax({
            data: JSON.stringify(coord),
            type: "POST",
            url: "/bursa_wolf/ret_ret",
            contentType: "application/json",
            dataType: "json",
            success: function (result) {
              console.log(result);
            },
            error: function (request, status, error) {
              console.log(request.responseText);
              console.log(request.error);
            },
          }).done(function (data) {
            var resultList = $("#output");
            $.each(data, function (key, value) {
              console.log(key);
              console.log(value);
              var li = $("<li/>")
                .addClass("list-group-item d-flex justify-content-between")
                .appendTo(resultList);
              var span = $("<span/>")
                .addClass("fw-bold")
                .text(key)
                .appendTo(li);
              var p = $("<p/>").text(value).appendTo(li);
            });
          });
          e.preventDefault();
        } else if (
          $("#selectCoord option:selected").text() === "Cartesianas/Cartesianas"
        ) {
          //----------------------------------------------------------
          // Cartesianas/Cartesianas (Opção 1)
          //----------------------------------------------------------
          $.ajax({
            data: JSON.stringify(coord),
            type: "POST",
            url: "/bursa_wolf/cart_cart",
            contentType: "application/json",
            dataType: "json",
            success: function (result) {
              console.log(result);
            },
            error: function (request, status, error) {
              console.log(request.responseText);
              console.log(request.error);
            },
          }).done(function (data) {
            var resultList = $("#output");
            $.each(data, function (key, value) {
              console.log(key);
              console.log(value);
              var li = $("<li/>")
                .addClass("list-group-item d-flex justify-content-between")
                .appendTo(resultList);
              var span = $("<span/>")
                .addClass("fw-bold")
                .text(key)
                .appendTo(li);
              var p = $("<p/>").text(value).appendTo(li);
            });
          });
          e.preventDefault();
        }
      } else if (transform === "Molodenski") {
        console.log("Molodenski");
        if (
          $("#selectCoord option:selected").text() === "Geográficas/Geográficas"
        ) {
          //----------------------------------------------------------
          // Geográficas/Geográficas (Opção 5)
          //----------------------------------------------------------
          $.ajax({
            data: JSON.stringify(coord),
            type: "POST",
            url: "/molodenski/geo_geo",
            contentType: "application/json",
            dataType: "json",
            success: function (result) {
              console.log(result);
            },
            error: function (request, status, error) {
              console.log(request.responseText);
              console.log(request.error);
            },
          }).done(function (data) {
            var resultList = $("#output");
            $.each(data, function (key, value) {
              console.log(key);
              console.log(value);
              var li = $("<li/>")
                .addClass("list-group-item d-flex justify-content-between")
                .appendTo(resultList);
              var span = $("<span/>")
                .addClass("fw-bold")
                .text(key)
                .appendTo(li);
              var p = $("<p/>").text(value).appendTo(li);
            });
          });
          e.preventDefault();
        }
      } else if (transform === "Polinomial 2º grau") {
        console.log("Polinomial");
        if (
          $("#selectCoord option:selected").text() ===
          "Retangulares/Retangulares"
        ) {
          //----------------------------------------------------------
          // Retangulares/Retangulares (Opção 9)
          //----------------------------------------------------------
          $.ajax({
            data: JSON.stringify(coord),
            type: "POST",
            url: "/polinomial/ret_ret",
            contentType: "application/json",
            dataType: "json",
            success: function (result) {
              console.log(result);
            },
            error: function (request, status, error) {
              console.log(request.responseText);
              console.log(request.error);
            },
          }).done(function (data) {
            var resultList = $("#output");
            $.each(data, function (key, value) {
              console.log(key);
              console.log(value);
              var li = $("<li/>")
                .addClass("list-group-item d-flex justify-content-between")
                .appendTo(resultList);
              var span = $("<span/>")
                .addClass("fw-bold")
                .text(key)
                .appendTo(li);
              var p = $("<p/>").text(value).appendTo(li);
            });
          });
          e.preventDefault();
        }
      }
    }
  });
});
