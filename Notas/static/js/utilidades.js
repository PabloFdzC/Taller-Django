function peticionAjax(url, tipo, datos){
    return new Promise(function(resolve, reject) {
      $.ajax({
        url: url,
        type: tipo,
        data: datos,
        contentType: "application/json; charset=utf-8",
        success: function(r){
          resolve(r);
        },
        error: function(err){
          reject(err);
        }
      });
    });
  }

  function hola(){
    console.log("hola");
  }