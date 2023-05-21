import React, { useEffect, useState } from 'react'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { useAuth } from './auth';
import CartItem from './CartItem';
import { Navigate, useNavigate } from 'react-router-dom';
import OrderItem from './OrderItem';
const baseurl = 'http://127.0.0.1:8000'

const Orders = () => {

    const [orders , setOrders] = useState([])
    const auth = useAuth()

    const config = {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
        
      }
      useEffect(() => {
      
        axios.get(`${baseurl}/api/orders`, config)
        .then(res => {setOrders(res.data.results); console.log(res.data.results)})
        .catch(err => console.log(err))

      },[])

      return (
        !auth.authnticated ? <Navigate to="/login"/>  :
        <section className="h-100 h-custom" style={{ backgroundColor: "#eee", minHeight:'calc(100vh - 45px)' }}>
          <Container className="py-5 h-100">
            <Row style={{minWidth:'400px'}}className="justify-content-center align-items-center h-100">
              <Col>
                <Card>
                  <Card.Body className="p-4">
                    <Row>
  
                      <Col lg="7">
                        <h5 className='mb-4'>
                          <a href="#!" className="text-body" style={{textDecoration:'none'}}>
                            <FontAwesomeIcon icon={faArrowLeft} className='me-2' />
                            Continue shopping
                          </a>
                        </h5>
                       
                                            
                      
                        
                        {
                         orders.map((order)=>
                       
                          <OrderItem key={order.id} order = {order}/>
                         )
                        }
  
                      </Col>
                    </Row>  {/* cart body */}

                  </Card.Body>
  
                </Card>
              </Col>
            </Row>
          </Container>
        </section> 
        ) 
}

export default Orders