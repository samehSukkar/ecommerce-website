import React, { useEffect } from 'react'
import { useAuth } from './auth'
const Logout = () => {
  const auth = useAuth()
  useEffect(()=>{
    auth.logout()
  })
  return (
    window.location.replace('/login')
  )
}

export default Logout