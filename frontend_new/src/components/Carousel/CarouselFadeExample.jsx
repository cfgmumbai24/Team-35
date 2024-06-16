// import React, { useState } from 'react';
// import { Carousel } from 'react-bootstrap';
// import './Carousel.css'; // Import your CSS file for styling (optional)

// const CarouselSlider = () => {
//   const [index, setIndex] = useState(0);
//   const slides = [
//     {
//       id: 1,
//       image: 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Disney%27s_Coco_logo.png',
//       bgImage: 'https://project-orion-production.s3.amazonaws.com/uploads/content/3315/Coco596d30d0192bd.jpg',
//       title: 'Coco',
//       description: 'Despite family\'s disapproval, Miguel dreams of music, magically travels to the afterlife, embarks on adventures.'
//     },
//     {
//       id: 2,
//       image: 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c2047868-eb3f-45a9-84ac-a12510bfedd9/dgnbje7-b84c9a04-bac2-489a-a22d-d0efd4fdc751.png?token=...',
//       bgImage: 'https://www.hollywoodreporter.com/wp-content/uploads/2024/02/sq110_s300_f206_2K_final-H-2024.jpg?w=1296',
//       title: 'Kung Fu Panda',
//       description: 'Po, now a spiritual leader, seeks a successor and unravels mysteries with a witty fox thief.'
//     },
//     {
//       id: 3,
//       image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Spider-Man_Across_the_Spider-Verse_logo.webp/1986px-Spider-Man_Across_the_Spider-Verse_logo.webp.png',
//       bgImage: 'https://d33hx0a45ryfj1.cloudfront.net/transform/cfb1fdab-a7d1-4b5d-9c39-a57f6df5ae6b/spider-man-into-the-spider-verse?io=transform:fill,width:1200,height:675',
//       title: 'Spider-Man: Into the Spider-Verse',
//       description: 'Miles Morales, reuniting with Gwen Stacy, traverses the Multiverse, clashing with other Spider-People over threats.'
//     }
//   ];

//   const handleSelect = (selectedIndex, e) => {
//     setIndex(selectedIndex);
//   };

//   const handleBack = () => {
//     setIndex((index - 1 + slides.length) % slides.length);
//   };

//   const handleNext = () => {
//     setIndex((index + 1) % slides.length);
//   };

//   return (
//     <Carousel activeIndex={index} onSelect={handleSelect} fade>
//       {slides.map(slide => (
//         <Carousel.Item key={slide.id}>
//           <div className="slide">
//             <img className="slide-bg" src={slide.bgImage} alt="Slide background" />
//             <div className="overlay"></div>
//             <div className="slide-info">
//               <img src={slide.image} alt="Slide logo" />
//               <p>{slide.description}</p>
//             </div>
//           </div>
//           <Carousel.Caption>
//             <h3>{slide.title}</h3>
//           </Carousel.Caption>
//         </Carousel.Item>
//       ))}
//       <button className="arrow back-arrow" onClick={handleBack}><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1jaGV2cm9uLWxlZnQiPjxwYXRoIGQ9Im0xNSAxOC02LTYgNi02Ii8+PC9zdmc+" alt="Back" /></button>
//       <button className="arrow next-arrow" onClick={handleNext}><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1jaGV2cm9uLXJpZ2h0Ij48cGF0aCBkPSJtOSAxOCA2LTYtNi02Ii8+PC9zdmc+" alt="Next" /></button>
//     </Carousel>
//   );
// }

// export default CarouselSlider;
