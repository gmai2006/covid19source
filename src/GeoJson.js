import React, { useState } from 'react';
import { Button, Form, FormGroup, Input, Label } from 'reactstrap';


const getJson = async (url) => {
    const response = await fetch(url);
    const json = await response.json;
    localStorage.setItem(`geojson`, json);
}


const GeoJson = (props) => {
    const [input, setInput] = useState(``);
    const download = async (event) => {
        console.log(input);
        await getJson(input);
        props.history.push('/');
    }
    

    return (
        <div>
            <Form>
                <FormGroup>
                    <Label for="exampleEmail">
                        GeoJSON URL
                    </Label>
                    <Input onChange={(e) => setInput(e.target.value)}
                        id="exampleEmail"
                        name="geojson"
                        placeholder="GeoJson"
                        type="text"
                    />
                </FormGroup>
                <Button onClick={download}>
                    Submit
                </Button>
            </Form>
        </div>

    );
}

export default GeoJson;