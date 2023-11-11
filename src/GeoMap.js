import React, { useState } from 'react';
import { LayersControl, Map, TileLayer, GeoJSON } from 'react-leaflet';
import L from 'leaflet';
import data from './testgeo.json';
const initState = {
    lat: 20,
    lng: 0,
    zoom: 2,
  }
  
const { BaseLayer } = LayersControl

const onEachFeature = (feature, layer) => {
    const popupContent = `<Popup><p><pre>${feature.properties.note}</pre></Popup>`
    layer.bindPopup(popupContent)
  }

  const pointToLayer = (feature, latlng) => {
    return L.circleMarker(latlng, {
      radius: feature.properties.radius,
      fillColor: feature.properties.color,
      color: "#000",
      weight: 1,
      opacity: 1,
      fillOpacity: 0.8
    });
  }

const GeoMap = (props) => {
    console.log(props);
    const [state, setState] = useState(initState);
    const position = [state.lat, state.lng];

    return (
        <Map center={position} zoom={state.zoom}
    style={{ width: '100%', height: '100vh' }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <LayersControl position="topright">
          <BaseLayer checked name="# Covid-19 Worldwide">
            <GeoJSON
              data={props.data}
              onEachFeature={ onEachFeature }
              pointToLayer= { pointToLayer }
            />
          </BaseLayer>
          
        </LayersControl>
    </Map>
    );
}

export default GeoMap;