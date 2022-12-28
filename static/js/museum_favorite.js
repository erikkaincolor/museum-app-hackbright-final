"use strict"
// alert("connected!!!!!")


let btn = document.querySelector("button");

// test:
// #1
// btn.value
// output:"1"
// #2
// btn.addEventListener("click", (evt)=>{
//     console.log(evt)  
//     })
// output:clicking on button shows us info

btn.addEventListener("click", (evt)=>{
    const museum_id=evt.target.value  
    
    fetch(`/museumdirectory/${museum_id}/museumfavorites`, {method:"POST"})
// camelCase for js vars from now on
})
