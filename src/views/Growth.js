import React, { useState} from 'react';
import { Card, CardBody, CardHeader } from 'reactstrap';
import {Col, Row } from 'reactstrap';

function Growth() {
  return (
    <div className="animated fadeIn">
      <Row>
          <Col xs="12" xl="12">
          <Card>
            <CardHeader>
              Predicted COVID-19 Growth Rate in 7 days
              <div className="card-header-actions">
                <a href="https://github.com/CSSEGISandData/COVID-19" className="card-header-action">
                  <small className="text-muted">Data source</small>
                </a>
              </div>
            </CardHeader>
            <CardBody>
              <img src={ require('./predicted_confirmed_growth_rate.png') } />  
            </CardBody>
          </Card>
          
        </Col>
      </Row>
      </div>
  );
}

export default Growth;