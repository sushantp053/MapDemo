let map = L.map('map').setView([1914491.959396094, 381797.91886491224], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/">OpenStreetMap</a> contributors'
}).addTo(map);

let natoshiData = fetch('http://127.0.0.1:8000/api/natoshi1/').then(response => response.json())
    .then(data => {
        console.log(data)
        let natoshi = L.geoJSON(data, {
            style: function (feature) {
                switch (feature.properties.crop) {
                    case 'Sugar Cane': return { color: "red" };
                    case 'Barren': return { color: "yellow" };
                    default: return { color: "blue" };
                }
            }
        })
        natoshi.addTo(map)
    })
    .catch(err => console.log(err))
