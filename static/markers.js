// Initialize the map
function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 37.7749, lng: -122.4194 },
        zoom: 8
    });

    // Create an array of marker objects with locations and info windows
    const markers = [
        {
            position: { lat: 37.7749, lng: -122.4194 },
            title: 'San Francisco',
            content: 'This is San Francisco. Click for more info.'
        },
        {
            position: { lat: 34.0522, lng: -118.2437 },
            title: 'Los Angeles',
            content: 'This is Los Angeles. Click for more info.'
        }
        // Add more markers with positions and content here
    ];

    // Add markers to the map
    markers.forEach(markerData => {
        const marker = new google.maps.Marker({
            position: markerData.position,
            map: map,
            title: markerData.title
        });

        const infowindow = new google.maps.InfoWindow({
            content: markerData.content
        });
        
        marker.addListener('click', function() {
            infowindow.open(map, marker);
        });
    });
}