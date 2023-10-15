// import "https://maps.googleapis.com/maps/api/js?key=AIzaSyB8WvkZaF6qGXS6vlJ8x765_h_V8t_rttc";
// // const apiKey = process.env.API_KEY;
// function initMap() {
//     // Set the coordinates for the initial map center
//     var myLatLng = {lat: 37.7749, lng: -122.4194};

//     // Create a map object and set the center and zoom level
//     var map = new google.maps.Map(document.getElementById('map'), {
//         center: myLatLng,
//         zoom: 12
//     });

//     // Add a marker to the map
//     var marker = new google.maps.Marker({
//         position: myLatLng,
//         map: map,
//         title: 'San Francisco, CA'
//     });
// }
// // Load the Google Maps JavaScript API using your API key
//     const script = document.createElement('script');
//     script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyB8WvkZaF6qGXS6vlJ8x765_h_V8t_rttc&callback=initMap`;
//     script.defer = true;
//     script.async = true;
//     document.head.appendChild(script);

const apiKey = 'YOUR_API_KEYAIzaSyB8WvkZaF6qGXS6vlJ8x765_h_V8t_rttc';

function initMap() {
    // Set the coordinates for the initial map center
    var myLatLng = {lat: 37.7749, lng: -122.4194};

    // Create a map object and set the center and zoom level
    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 12
    });

    // Add a marker to the map
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'San Francisco, CA'
    });
}