import React from 'react';

const Charts = React.lazy(() => import('./views/Charts'));
const Growth = React.lazy(() => import('./views/Growth'));
const GeoJson = React.lazy(() => import('./GeoJson'));
// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/map', exact: true, name: 'CoVid19', component: Charts },
  { path: '/growth', exact: true, name: 'Predictive Growth Model', component: Growth },
  { path: '/geojson', exact: true, name: 'Read GeoJSON', component: GeoJson },
];

export default routes;
