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
    const collection_id=evt.target.value  
    
    fetch(`/collections/${collection_id}/collectionfavorites`, {method:"POST"})
// camelCase for js vars from now on
})
