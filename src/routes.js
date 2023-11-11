import React from 'react';
import GeoMap from './GeoMap';

const Charts = React.lazy(() => import('./views/Charts'));
const Growth = React.lazy(() => import('./views/Growth'));
const GeoJson = React.lazy(() => import('./GeoJson'));
// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/map', exact: true, name: 'CoVid19', component: Charts },
  { path: '/growth', exact: true, name: 'Predictive Growth Model', component: Growth },
  { path: '/geojson', exact: true, name: 'Read GeoJSON', component: GeoJson },
  { path: '/geomap', exact: true, name: 'Read GeoJSON', component: GeoMap },
];

export default routes;
