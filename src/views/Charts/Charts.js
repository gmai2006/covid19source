import React, { useState } from 'react';
import { Card, CardBody, CardHeader } from 'reactstrap';
import {Col, Row } from 'reactstrap';
import LeafletChart from './LeafletChart';

const initState = {
  current: new Date()
}

function Charts() {
  const [state, setState] = useState(initState);
    return (
      <div className="animated fadeIn">
      <Row>
          <Col xs="12" xl="12">
          <Card>
            <CardHeader data={state.current}>
              Daily Status
              <div className="card-header-actions">
                <a href="https://github.com/CSSEGISandData/COVID-19" className="card-header-action">
                  <small className="text-muted">Data source</small>
                </a>
              </div>
            </CardHeader>
            <CardBody>
              <LeafletChart />
            </CardBody>
          </Card>
          
        </Col>
      </Row>
      </div>
    );
  }

export default Charts;
