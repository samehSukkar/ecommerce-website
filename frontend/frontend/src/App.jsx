import { useState } from 'react'
import './App.css'
import {Routes , Route, Router} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Item from './components/Item';
import Category from './components/Category';
import Tag from './components/Tag';
import Cart from './components/Cart';
import Login from './components/Login';
import Logout from './components/Logout';
import { AuthProvider } from './components/auth';

function App() {

  return (
    <AuthProvider>

      <Navbar/>
      <Routes>
        <Route path='home' element={<Home/>}/>
        <Route path='/products/:id' element={<Item/>}/>
        <Route path='/categoreis/:id' element={<Category/>}/>
        <Route path='/tags/:id' element={<Tag/>}/>
        <Route path='/cart' element={<Cart/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/logout' element={<Logout/>}/>
      </Routes>
      
    </AuthProvider>
  )
}

export default App
