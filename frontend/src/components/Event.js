import React from 'react'

function Event({title,description,image}) {
  
  console.log("image before",image)
  let source = image.replace('http://127.0.0.1:8000/frontend/','')
  console.log("image after",source)

  return (
    <div>
      <section className="part3">
    <div className="container">
      <div className="container2">
        <div className="containerrr">
      <div>
        
        <h2  className="eventHeadline">
          
          {title}</h2>
          </div>
          
          
          <div  className="part3Desc">
                      <h6   className="eventDescription">{description}</h6>
                      <a  href="#" className="btn1">Be part of This<img   className="arrow1" src={"static/images/arrow1.svg"} /></a>
                      
                    </div>
                    
          

      </div>
      <div className="containerr">
       <img  className="eventImage" src={source} />
          
      </div>
      </div>
      </div>
    </section>
      
    </div>
  )
}

export default Event
