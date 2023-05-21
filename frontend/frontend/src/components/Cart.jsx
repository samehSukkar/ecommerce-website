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
const baseurl = 'http://127.0.0.1:8000'

const Cart = () => {

    const [items , setItems] = useState([])
    const auth = useAuth()
    const navigate = useNavigate()

    const config = {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem('token')}`
      },
      
    }
    useEffect(() => {
      
        axios.get(`${baseurl}/api/cart`, config)
        .then(res => setItems(res.data.results))
        .catch(err => console.log(err))

      },[])



      const deleteItem = (itemId)=>{

          const config = {
            headers: { 
              
              'Authorization': `Token ${localStorage.getItem('token')}`
              },
          };

          axios.delete(`http://127.0.0.1:8000/api/cart/${itemId}`,config)
          .then(res=> {
                
                setItems(prevItems => prevItems.filter(item => item.id !== itemId));
              
          })
          .catch(err=>console.log(err))
          
      }

      const calctotal = ()=> {
        let total = 0
        items.forEach((item)=> {total+= item.product.price * item.quantity} )
        return total;
      }
      
      const createOrder = () => {
          let config = {
            method: 'post',
            maxBodyLength: Infinity,
            url: 'http://127.0.0.1:8000/api/order/create',
            headers: { 
              'Authorization': 'Token 3beff4c08e4083a4ff6519156dee9a84379004d2'
            }
          };
          
          axios.request(config)
          .then((response) => {
            console.log(JSON.stringify(response.data));
          })
          .catch((error) => {
            console.log(error);
          })
      }

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
                      <h5>
                        <a href="#!" className="text-body" style={{textDecoration:'none'}}>
                         
                          <FontAwesomeIcon icon={faArrowLeft} className='me-2' />
                          Continue shopping
                        </a>
                      </h5>
                      <h5>Total: {calctotal().toFixed(2)} JD</h5>
                      <hr />

                      <p className="mb-1">Shopping cart</p>
                      <p className="mb-4">You have {items.length} items in your cart</p>
                      
                    {
                      items.map((item)=>
                          <CartItem key={item.id} item = {item} deleteItem={deleteItem}/>
                      )
                    }

                    </Col>
                  </Row>  {/* cart body */}
                  {
                   items.length ?
                  <Row className='d-flex justify-content-center px-3 col-md-6'>
                    <Button variant="success" onClick={createOrder}>create order</Button>
                  </Row> : <></>
                  }
                </Card.Body>

              </Card>
            </Col>
          </Row>
        </Container>
      </section> 
      ) 

    }

  export  default  Cart;