import React, {useState} from 'react';
import Modal  from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTrash, faCheck, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons'
import { useAuth } from './auth';
import { Navigate, useNavigate } from 'react-router-dom';


function CartModal({item}) {
    
    const [quantity, setQuantity] = useState(1);
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const navigate = useNavigate()

    const auth = useAuth()

    const addToCart = (item) =>{
      const config = {
          headers: { 
              'Authorization': `Token ${localStorage.getItem('token')}`
            },
      };
      const data = {
          "product": item.id,
          "quantity": quantity
      }
      if (localStorage.getItem('token')) {
        axios.post(`http://127.0.0.1:8000/api/cart`,data,config)
        .then(res=> {
                    console.log(res.data)
        })
        .catch(err=>console.log(err))
      }

    }
    return (
      <>

        <Button  variant="dark"  style ={{marginTop: '20px'}} onClick={()=> 
           !auth.authnticated ? navigate("/login") : handleShow()
        }>
          Add to Cart</Button>
       
        <Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Add to cart</Modal.Title>
          </Modal.Header>
          <Modal.Body>Would you like to add {item.name} to cart ?
          <div className="d-flex mt-4 align-items-center">
                    <Button className="d-flex justify-content-center align-items-center" style={{height: '30px',width:'30px', borderRadius:'50%' }} variant='dark' onClick= {()=> {setQuantity(quantity+1);  }}>
                    <FontAwesomeIcon icon={faPlus} />
                    </Button>
                    <h5 className='m-2'>{quantity}</h5>
                    <Button className="d-flex justify-content-center align-items-center" style={{height: '30px', width:'30px', borderRadius:'50%'}} variant='dark' onClick= {()=> {setQuantity(quantity > 1 ? quantity-1 : 1); }}>
                    <FontAwesomeIcon icon={faMinus} />
                    </Button>
                </div>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
            </Button>
            <Button variant="primary" onClick={()=> {
               addToCart(item)
               handleClose()
            }}>   Submit   </Button>

          </Modal.Footer>
        </Modal> 
      </>
    );
  }

export default CartModal;
 