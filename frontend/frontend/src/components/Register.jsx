import React, { useEffect, useState , useRef} from 'react'
import axios from 'axios'
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { useAuth } from './auth';
import { Navigate, useNavigate } from 'react-router-dom';

const Register = () => {
    const baseurl = "http://127.0.0.1:8000"

    const auth = useAuth()
    const userRef = useRef(null);
    const emailRef = useRef(null);
    const passwordRef = useRef(null);
    const passwordConfirmRef = useRef(null);
    const navigate = useNavigate()

    const register = () => {
        const data = {
            username: userRef.current.value,
            email: emailRef.current.value,
            password: passwordRef.current.value,
            password2: passwordConfirmRef.current.value
        }
        axios.post(`${baseurl}/api/register`, data)
        .then(()=>console.log(data))
    }



  return (
    auth.authnticated ? <Navigate to="/home" /> : 
    <section className="d-flex justify-content-center align-items-center" style={{ backgroundColor: "#eee", minHeight:'calc(100vh - 45px)' }}>
            <Card className="d-flex justify-content-center algin-items-center p-4"
            style={{width: '300px' }}>
            <Form onSubmit={register}>

              <Form.Group className="mb-3" controlId="usernameInput">
                <Form.Label>username</Form.Label>
                <Form.Control required ref={userRef} type="text" name="usernameInput" />
              </Form.Group>
              
              <Form.Group className="mb-3" controlId="emailInput">
                <Form.Label>email</Form.Label>
                <Form.Control required ref={emailRef} type="text" name="emailInput" />
              </Form.Group>

              <Form.Group className="mb-3" controlId="password1">
                <Form.Label>password</Form.Label>
                <Form.Control  required ref={passwordRef} type="password" name="password1" />
              </Form.Group>
              
              <Form.Group className="mb-3" controlId="password2">
                <Form.Label>confirm password</Form.Label>
                <Form.Control required ref={passwordConfirmRef} type="password" name="password2" />
              </Form.Group>
            <Button className="w-100" variant='dark' type="submit" >login</Button>
            </Form>
              
            </Card>
      </section>
    
  )
}

export default Register