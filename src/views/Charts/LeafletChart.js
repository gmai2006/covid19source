// https://www.smashingmagazine.com/2020/02/javascript-maps-react-leaflet/
import React, { useState} from 'react';
import { Map, TileLayer, GeoJSON , LayersControl} from 'react-leaflet';

import dataworld from './covid-world.json';
import dataus from './covid-us.json';
import us1 from './predictive_2020-04-02.json';
import us2 from './predictive_2020-04-03.json';
import us3 from './predictive_2020-04-04.json';
import us4 from './predictive_2020-04-05.json';
import us5 from './predictive_2020-04-06.json';
import L from 'leaflet';

const initState = {
  lat: 20,
  lng: 0,
  zoom: 2,
}

const { BaseLayer } = LayersControl

const LeafletChart = () => {
  const [state, setState] = useState(initState);

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

  const position = [state.lat, state.lng]
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
              data={dataworld}
              onEachFeature={ onEachFeature }
              pointToLayer= { pointToLayer }
            />
          </BaseLayer>
          <BaseLayer name="# Covid 19 in US">
            <GeoJSON
                data={dataus}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
          <BaseLayer name="Predicted # next day">
            <GeoJSON
                data={us1}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
          <BaseLayer name="Predicted # following day">
            <GeoJSON
                data={us2}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
          <BaseLayer name="Predicted # 3rd day">
            <GeoJSON
                data={us3}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
          <BaseLayer name="Predicted # 4th day">
            <GeoJSON
                data={us4}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
          <BaseLayer name="Predicted # 5th day">
            <GeoJSON
                data={us5}
                onEachFeature={ onEachFeature }
                pointToLayer= { pointToLayer }
              />
          </BaseLayer>
        </LayersControl>
    </Map>
  )
}

export default LeafletChart;