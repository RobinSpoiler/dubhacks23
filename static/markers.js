function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 0, lng: 0 }, // Initial map center
        zoom: 8, // Initial zoom level
    });

    // JavaScript to add markers from your Flask route response
    fetch('/post', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        data.markers.forEach(markerData => {
            var marker = new google.maps.Marker({
                position: { lat: parseFloat(markerData.latitude), lng: parseFloat(markerData.longitude) },
                map: map,
                title: markerData.item,
            });
        });
    });
}