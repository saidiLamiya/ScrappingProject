import React,{useEffect,useState,useRef} from 'react'

import Header from './Header'
import Event from './Event'


function EventPage() {
  let ev = useRef([])
  const [background,setBackground] = useState("colorPY")
  const [events,setEvents] =useState([]);
  useEffect(() => {
    getEvents();
    
  },[]);
  const changeBackground = () =>{
    console.log(window.scrollY)
    
    if((window.scrollY >= 340 && window.scrollY <1000) || (window.scrollY >= 1500)){
       setBackground("bg-color-white");
        
        }else{setBackground("colorPY")} 
    
    }

  
      
  
  window.addEventListener('scroll', changeBackground)
  
  const getEvents = async () => {
    
    const response = await fetch("/api/get-all-events", {
      "method": "GET",
      "headers": { "Content-Type": "application/json" }
    });
    const datas = await response.json();
    // setProducts(datas.products);
    // useEffect(()=>{ setEvents(datas) }, [])
    // console.log(events)
    //ref={el => ev = el}
    let eventss = datas
    setEvents(eventss)
    
    console.log(eventss.title)
    console.log(eventss)
  }
  

  return (

    <div className={background}>
     <Header logo={"static/images/logoB.png"} class1="nav-item colorB" class2="nav-item colorB" />
     <section className="part2 addMargin " id="part2">
        <div className="container container1">
        <h6 className="littleHeadline">What's this ?</h6>

          <div className="no-animation ">
            <h6 className=" eventDesc">
          Our best events with details are here for you to choose from, you will find people who shares the same motivation and goal.
            </h6>
          </div>
          <div className="arrowAnimation">
            <a href="#events">
              <img
                className="arrow1 arrow90"
                src={"static/images/arrow1.svg"}
              />
            </a>
          </div>
          </div>
     </section>
       <div id="events">
     {events.map(event=>(
        <Event title={event.title} description={event.description} image={event.photo} />
      ))}
     </div>
      
    </div>
  )
}

export default EventPage
