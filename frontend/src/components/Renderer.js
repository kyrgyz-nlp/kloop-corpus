import React from 'react'
import { useSelector } from "react-redux"

function Renderer() {
  const { text } = useSelector(state => state.textData)
  return (
    <>
		  <div>Renderer</div>
      <p>Text: {text}</p>
    </>
  )
}

export default Renderer