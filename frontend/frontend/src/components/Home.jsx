import React, { useState } from 'react'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import cardimg from '../assets/iphone12.png'
import Container from 'react-bootstrap/esm/Container';

const Home = () => {
    const item1 = {
        'id':1,
        'name': 'iphone12',
        'category': 'phones',
        'price': 140,
    }
    const [items , setItems] = useState([item1,])

  return (
    <>
        <Container  style={{padding: '50px'}}>
        
            <Card  className="text-center" style={{ width: '12rem' , padding: '20px 5px 0px 5px'}}>
                <Card.Img variant="top" src={cardimg} style={{width: '8rem', margin: 'auto'}}/>
                <Card.Body>
                    <Card.Title  style={{marginBottom: '5px'}}>iPhone12</Card.Title>
                    <Card.Text style={{marginBottom: '5px'}}>820 JD</Card.Text>
                    <Card.Link>#apple</Card.Link>
                    <Card.Link>#Black</Card.Link>
                    <Button variant="dark"  style={{display:'block', marginTop: '5px', marginInline: 'auto'}}>Add to Cart</Button>
                </Card.Body>
            </Card>    
        </Container>
    </>
  )
}

export default Home