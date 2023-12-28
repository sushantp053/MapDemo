var map = L.map('map').setView([17.31275168944332, 73.88766000779006], 13);

var o = document.getElementById("map");

//73.88766000779006, 17.31275168944332
//17.061195, 74.258851

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)

var marker = L.marker([17.061195, 74.258851]).addTo(map);

var circle = L.circle([17.061195, 74.258851], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

var polygon = L.polygon([[17.067469, 74.259670],
    [17.062464, 74.257954], 
    [17.062186, 74.250218], 
    [17.063345, 74.248545]], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

const natoshi = JSON.parse(document.getElementById('natoshi').textContent);

var n = JSON.parse(natoshi.data);
// console.log(n);

// var natoshi1 = L.geoJSON(n).addTo(map);

var agriLayer = L.geoJSON(n, {
    style: function(feature) {
        switch (feature.properties.crop) {
            case 'Sugar Cane': return {color: "red"};
            case 'Barren': return {color: "yellow"};
            default: return {color: "blue"};
        }
    }
});


agriLayer.addTo(map);

