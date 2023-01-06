"use strict"
//may have to put these on collections page
// alert("connected!!!!!")

// test:
// #1
// btn.value
// output:"1"
// #2
// btn.addEventListener("click", (evt)=>{
//     console.log(evt)  
//     })
// output:clicking on button shows us info

let btn = document.querySelector("#addfave"); //for the add to faves btn

//logged-in + add fave
btn.addEventListener("click", (evt)=>{
    const artId=evt.target.value  
    fetch('/collections/' + collectionId + '/' + artId + '/artfavorites', {method:"POST"})
// camelCase for js vars from now on
})

//logged-in + remove fave
let btn2 = document.querySelector("#removefave"); //for the add to faves btn

btn2.addEventListener("click", (evt)=>{
    const artId=evt.target.value  
    fetch('/collections/' + collectionId + '/' + artId + '/removeartfavorites', {method:"POST"}) //AJAX request to db
})