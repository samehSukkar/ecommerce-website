import React, { useEffect, useState } from 'react'
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';
import ItemCard from './ItemCard';
const baseurl = 'http://127.0.0.1:8000'


const Home = () => {
    

    const [items , setItems] = useState([])
    useEffect(() => {
        fetch(`${baseurl}/api/products`)
        .then(response => response.json())
        .then(data => setItems(data.results))
      },[])


  return (
    <>
        <Container style={{padding: '50px'}}>
            <Row>
                {items.map((item) => 
                    <Col key={item.id} sm={6} lg={4} xl={3} style={{marginBottom:'20px'}}>
                        <ItemCard item={item}/>
                     </Col>
                )}
            </Row>
        </Container>
    </>
  )
}



export default Home