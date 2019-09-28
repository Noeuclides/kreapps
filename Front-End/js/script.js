document.querySelector('#map').addEventListener('click', function () {
  console.log('hello');
});

// using the backend for the names
const getNames = () => {
   fetch('http://localhost:5000/api/v1/hospitals')
   .then(response => response.json())
   .then(places => {
     places.forEach(place => {
       document.getElementById('lista_eps').append(`${place.name}`)
       console.log(place)
     })
   })
}

// get data ESE Antioquia
const placesInfo = [];
const getData = () => {
  fetch('http://localhost:5000/api/v1/hospitals')
    .then(response => response.json())
    .then(places => {
      // console.log(places);
      places.forEach(place => {
        const pointPosition = {
          lat: parseFloat(place.latitude),
          lng: parseFloat(place.longitude)
        };
        const placeIn = {
          position: pointPosition,
          name: place.nombre_sede
        };
        // console.log(placeIn);
        placesInfo.push(placeIn);
      });
      // get position of the user
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(userPlace => {
          const placeUser = {
            lat: parseFloat(userPlace.coords.latitude),
            lng: parseFloat(userPlace.coords.longitude)
          };
          // draw map
          drawMap(placeUser);
        });
      }
    });
};
// fucntion draw map
const drawMap = (object) => {
  // current position
  var iconBase = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/';
  const map = new google.maps.Map(document.getElementById('map'), {
    // center on place user
    center: object,
    zoom: 11
  });
  // create marker in current position of user
  const markerUser = new google.maps.Marker({
    position: object,
    title: 'Current Position', 
    icon: iconBase + 'library_maps.png'
  });
  // assign Marker to map
  markerUser.setMap(map);
  // markers of ESEs
  const markers = placesInfo.map(place => {
    return new google.maps.Marker({
      position: place.position,
      title: place.name,
      map: map,
      icon: iconBase + 'info-i_maps.png'
    });
  });
};
getData();
getNames();
