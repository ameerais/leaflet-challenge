// Ensure the script runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Create a map object, centering it over the U.S. and setting an initial zoom level.
    var myMap = L.map("map", {
        center: [37.09, -95.71], // Center of the U.S.
        zoom: 5 // Starting zoom level
    });

    // Add a tile layer (base map) from OpenStreetMap. This provides the basic map display.
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors" // This is required to give credit to OpenStreetMap.
    }).addTo(myMap);

    // URL to fetch the GeoJSON data for all earthquakes from the past 7 days.
    var earthquakeDataUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

    // Fetch earthquake data from the provided URL using D3.js
    d3.json(earthquakeDataUrl).then(function(data) {

        // Function to determine the marker color based on the depth of the earthquake.
        function getColor(depth) {
            return depth > 90 ? '#d73027' : // Deep red for the deepest earthquakes (> 90 km)
                   depth > 70 ? '#fc8d59' : // Orange for moderately deep earthquakes
                   depth > 50 ? '#fee08b' : // Yellow for shallower earthquakes
                   depth > 30 ? '#d9ef8b' : // Light green for even shallower earthquakes
                   depth > 10 ? '#91cf60' : // Darker green for shallow earthquakes
                                '#1a9850';  // Dark green for the shallowest earthquakes
        }

        // Function to determine the size of the marker based on the earthquake magnitude.
        function getRadius(magnitude) {
            // A multiplier to make markers more visible (e.g., a magnitude 0 earthquake will still have a radius of 1)
            return magnitude === 0 ? 1 : magnitude * 4; 
        }

        // Add GeoJSON layer to the map using the earthquake data.
        L.geoJson(data, {
            // PointToLayer is used to create circle markers at each earthquake's location.
            pointToLayer: function(feature, latlng) {
                return L.circleMarker(latlng);
            },
            // Style each marker with its radius, color, and other properties.
            style: function(feature) {
                return {
                    // The radius is proportional to the magnitude of the earthquake.
                    radius: getRadius(feature.properties.mag),
                    fillColor: getColor(feature.geometry.coordinates[2]), // Color based on earthquake depth.
                    color: "#000", // Border color for the circle (black)
                    weight: 0.5, // Border thickness
                    opacity: 1, // Border opacity
                    fillOpacity: 0.8 // Fill opacity
                };
            },
            // Bind popups to each marker to display more information when clicked.
            onEachFeature: function(feature, layer) {
                // Earthquake data to be displayed in the popup.
                var popupContent = `<h3>Magnitude: ${feature.properties.mag}</h3>
                                    <hr>
                                    <p>Location: ${feature.properties.place}</p>
                                    <p>Depth: ${feature.geometry.coordinates[2]} km</p>`;
                // Attach the popup to the layer.
                layer.bindPopup(popupContent);
            }
        }).addTo(myMap); // Add the GeoJSON layer to the map.

        // Add a legend to the map to explain the color coding for earthquake depths.
        var legend = L.control({ position: 'bottomright' }); // Position at the bottom right corner of the map.

        legend.onAdd = function() {
            // Create a new div element for the legend.
            var div = L.DomUtil.create('div', 'info legend');
            // Depth intervals to be displayed in the legend.
            var depthIntervals = [-10, 10, 30, 50, 70, 90];
            var colors = [];

            // Loop through the intervals and generate a color label for each range.
            for (var i = 0; i < depthIntervals.length; i++) {
                // Create a color box for each interval.
                div.innerHTML +=
                    '<i style="background:' + getColor(depthIntervals[i] + 1) + '"></i> ' +
                    depthIntervals[i] + (depthIntervals[i + 1] ? '&ndash;' + depthIntervals[i + 1] + '<br>' : '+');
            }

            return div; // Return the constructed legend div.
        };

        // Add the legend to the map.
        legend.addTo(myMap);

    }).catch(function(error) {
        console.error("Error loading earthquake data:", error); // Log any errors in data fetching.
    });
});
