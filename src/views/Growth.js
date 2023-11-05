import React, { useState} from 'react';
import { Card, CardBody, CardHeader, FormGroup, Input, Label } from 'reactstrap';
import {Col, Row } from 'reactstrap';

const stateNames = `Alaska
Alabama
Arkansas
American Samoa
Arizona
California
Colorado
Connecticut
Delaware
Florida
Georgia
Guam
Hawaii
Iowa
Idaho
Illinois
Indiana
Kansas
Kentucky
Louisiana
Massachusetts
Maryland
Maine
Michigan
Minnesota
Missouri
Mississippi
Montana
North Carolina
North Dakota
Nebraska
New Hampshire
New Jersey
New Mexico
Nevada
New York
Ohio
Oklahoma
Oregon
Pennsylvania
Puerto Rico
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Virginia
Virgin Islands
Vermont
Washington
Wisconsin
West Virginia
Wyoming`;

// let defaultChart = `./predicted_confirmed_growth_rate.png`;
const states = stateNames.split(`\n`);
console.log(states);
const update = (event) => {
  console.log(event);
}

function Growth() {
  const [image, setImage] = useState('./Arkansas_confirm_predicted_growth_rate.png');
  console.log(image);
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
            <FormGroup>
              <Label for="exampleSelect">
                Select
              </Label>
              <Input
                id="states"
                name="select"
                type="select"
                onClick={
                  event => {
                    console.log(event.target.value);
                    setImage(`./${encodeURIComponent(event.target.value)}_confirm_predicted_growth_rate.png`);
                  }
              }
              >
                {states.map((state) => (
                  <option key={state}>
                    {state}
                  </option>
                ))}
                
              </Input>
            </FormGroup>
              <img src={ require(`${image}`) } />  
            </CardBody>
          </Card>
          
        </Col>
      </Row>
      </div>
  );
}

export default Growth;