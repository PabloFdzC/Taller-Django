$('body').ready(function(){
    const cargarNotas = async function(){
      try{
        var res = await peticionAjax(ver_mis_notas_url, 'GET', {});
        if(res){
          $('#lista-notas').append(res);
        }
      }catch(err){
        console.log(err);
        $('#lista-notas').append("Fallo");
      }
    };
    
    cargarNotas();
  });