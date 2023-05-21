import React, { useEffect, useState } from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown'
import axios from 'axios';
import { useAuth } from './auth';

const baseurl = 'http://127.0.0.1:8000'


function ColorSchemesExample() {
    
    const [categories, setCategories] = useState([])
    const auth = useAuth()
    
    useEffect(()=>{
        axios.get(`${baseurl}/api/categories`)
        .then(res => {
            console.log(res.data.results)
            setCategories(res.data.results)
        })
        .catch(err => console.log(err))
    },[])

  return (
    <>
        <Navbar bg="dark" variant="dark" expand="sm">
            <Container>
                <Navbar.Brand href="/home">SUKKAR</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                            <Nav.Link href="/home">Home</Nav.Link>
                            <NavDropdown title="Categories" id="basic-nav-dropdown">
                                {
                                    categories.map((cat)=>
                                    <NavDropdown.Item key={cat.id} href= {`/categoreis/${cat.id}`}>{cat.name}</NavDropdown.Item>
                                    )
                                    
                                }
                            </NavDropdown>
                    </Nav>
                    <Nav className="ms-auto">
                        <Nav.Link  href="/cart">Cart</Nav.Link>
                        {
                            !auth.authnticated ?
                            <>
                            <Nav.Link  href="/login">login</Nav.Link> 
                            <Nav.Link  href="/register">register</Nav.Link> 
                            </> :
                            <>
                            <Nav.Link  href="/logout">logout</Nav.Link>
                            <Nav.Link  href="/orders">orders</Nav.Link>
                            </>
                        }
                       
                      
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    </>
  );
}

export default ColorSchemesExample;