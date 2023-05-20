import React, {useEffect, useState} from 'react'
import axios from 'axios'
import { useParams } from 'react-router-dom';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col';
import ItemCard from './ItemCard';

const Category = () => {

    const [cat, setCat] = useState([]);
    const [items , setItems] = useState([])
    const {id} = useParams()

    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/api/categories/${id}`)
        .then(res=> setCat(res.data))
        .catch(err=>console.log(err))
        
        axios.get(`http://127.0.0.1:8000/api/products?category=${id}`)
        .then(res=> setItems(res.data.results))
        .catch(err=>console.log(err))


    },[])


  return (
    <Container style={{padding: '50px 30px'}}>
        <h2>@{cat.name}</h2>
        <Row>
                {items.map((item) => 
                    <Col key={item.id} sm={6} lg={4} xl={3} style={{marginBottom:'20px'}}>
                         <ItemCard item={item}/>
                     </Col>
                )}
            </Row>
    </Container>
  )
}

export default Category