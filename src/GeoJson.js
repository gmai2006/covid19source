import React, { useState } from "react";
import {
  Button,
  Col,
  Container,
  Form,
  FormGroup,
  Input,
  Label,
  Row,
} from "reactstrap";
import GeoMap from "./GeoMap";

//https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_shp.geojson

const GeoJson = (props) => {
  const [input, setInput] = useState(``);
  const [data, setData] = useState(``);

  const download = async (event) => {
    console.log(input);
    const response = await fetch(input);
    const json = await response.json();
    setData(json);
    console.log(data);
  };

  return (
    <Container>
      <Row>
        <Col>
          <Form>
            <FormGroup>
              <Label for="exampleEmail">GeoJSON URL</Label>
              <Input
                onChange={(e) => setInput(e.target.value)}
                id="exampleEmail"
                name="geojson"
                placeholder="GeoJson"
                type="text"
              />
            </FormGroup>
            <Button onClick={download}>Load GeoJson</Button>
          </Form>
        </Col>
      </Row>
       
        <Row>
        <Col>
        { (data) ? <GeoMap data={data} /> : ``}
        </Col>
      </Row>
      
      
    </Container>
  );
};

export default GeoJson;
