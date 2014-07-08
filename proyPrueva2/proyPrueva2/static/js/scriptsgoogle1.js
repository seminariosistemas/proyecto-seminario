$(function(){
	// alert('OK');
    var popup;
	var datos=[]
	$("#data1 input").each(function(){
		var latitud=$(this).attr("latitud")
		var longitud=$(this).attr("longitud")
		var nombre=$(this).attr("nombre")
		datos.push({"lat":latitud,"lon":longitud,"nombre":nombre})

	});

	if (navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	}else{

		initialize(-19.571228999999963, -65.76189451481935);
	}
	function getCoords(position)
	{
		var lat=position.coords.latitude;
		var lng=position.coords.longitude;

		initialize(lat, lng);
	}
	function getError(err)
	{
		initialize(-19.571228999999963, -65.76189451481935);
	}
	function initialize(lat, lng)
	{

		var LatLng= new google.maps.LatLng(lat, lng);
		var mapSettings ={
			center: LatLng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}

		map= new google.maps.Map($('#mapa1').get(0), mapSettings);

		/*var marker= new google.maps.Marker({
			position:LatLng,
			map:map,
			draggable: true,
			title: 'Arrastrame'
		});*/
		for(i=0;i<datos.length;i++){
                console.log(datos[i].lat)
            var LatLng= new google.maps.LatLng(datos[i].lat, datos[i].lon);
            var marker= new google.maps.Marker({
                position:LatLng,
                map:map,
                draggable: false,
                title:datos[i].nombre,
                icon: 'http://i57.tinypic.com/s63cpz.jpg'
            });
            console.log(marker)




            google.maps.event.addListener(marker,'click', function(){
 	 			if(!popup){
 	 				popup = new google.maps.InfoWindow();
 	 			}
 	 			var note = 'Proyecto: ' + this.title +' ';

 	 			popup.setContent(note);
 				popup.open(map, this);
 	 			getMarkerCoords(marker);
 	 		});


		}

		google.maps.event.addListener(marker,'position_changed', function(){
			getMarkerCoords(marker);
		});
	}
	function getMarkerCoords(marker)
	{
		var markerCoords= marker.getPosition();
		$('#id_lat').val(markerCoords.lat());
		$('#id_lng').val(markerCoords.lng());
	}
	$('#form_coords1').submit(function(e){
		e.preventDefault();
		$.post('/coords/save',$(this).serialize(),function(data){
			if(data.ok)
			{
				$('#data1').html(data.msg);
				$('#form_coords1').each(function(){ this.reset(); });
			}else{
				alert(data.msg);
			}
		},'json');
	});
});

