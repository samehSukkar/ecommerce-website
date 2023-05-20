import React, { useEffect, useState , useRef} from 'react'
import axios from 'axios'
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { useAuth } from './auth';
import { Navigate, useNavigate } from 'react-router-dom';

const Login = () => {

    // useEffect(()=>{
    //   getToken()
    // },[])
    const userRef = useRef(null);
    const passwordRef = useRef(null);

    const auth = useAuth()
    const navigate = useNavigate()

    let getToken = async () => {

      const user = userRef.current.value
      const password = passwordRef.current.value
      let data = JSON.stringify({
        username: user,
        password: password
      });
  
      let config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/auth',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      };
  
      axios.request(config)
        .then((response) => {
          console.log(response.data);
          auth.login(response.data.token)
          navigate(-1)
         
        })
        .catch((error) => {
          console.log(error);
        });
};



    return (
      <section className="d-flex justify-content-center align-items-center" style={{ backgroundColor: "#eee", minHeight:'calc(100vh - 45px)' }}>
            <Card className="d-flex justify-content-center algin-items-center p-4"
            style={{width: '300px' }}>
              <Form.Group className="mb-3" controlId="passwordInput">
                <Form.Label>username</Form.Label>
                <Form.Control ref={userRef} type="text" name="usernameInput" />
              </Form.Group>
              <Form.Group className="mb-3" controlId="username">
                <Form.Label>password</Form.Label>
                <Form.Control  ref={passwordRef} type="password" name="username" />
              </Form.Group>
              
              <Button variant='dark' onClick={getToken}>login</Button>
              
            </Card>

      </section>
   
  )
}

export default Login