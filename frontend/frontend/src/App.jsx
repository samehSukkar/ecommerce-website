import { useState } from 'react'
import './App.css'
import {Routes , Route, Router} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar'
import Home from './components/Home'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Navbar/>
    <Routes>
      <Route path='home' element={<Home/>}/>
    </Routes>
    </>
  )
}

export default App
