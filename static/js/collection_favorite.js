"use strict"
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

//logged-in + add fave
let btn = document.querySelector("#addfave"); //for the add to faves btn

btn.addEventListener("click", (evt)=>{
    let collectionId = evt.target.value;
    fetch(`/collections/${collectionId}/collectionfavorites`, {method:"POST"})
    // camelCase for js vars from now on
})

//logged-in + remove fave
let btn2 = document.querySelector("#removefave"); //for the add to faves btn

btn2.addEventListener("click", (evt)=>{
    const collectionId=evt.target.value  
    fetch(`/collections/${collectionId}/removecollectionfavorites`, {method:"POST"}) //AJAX request to db
})



//////////////ART OBJ FAVES
//logged-in + add fave
let btn4 = document.querySelector("#addartfave"); //for the add to faves btn

btn4.addEventListener("click", (evt)=>{
    let artId = evt.target.value;
    fetch(`/${artId}/artfave`, {method:"POST"})
    // camelCase for js vars from now on
})

//logged-in + remove fave
let btn5 = document.querySelector("#removeartfave"); //for the add to faves btn

btn5.addEventListener("click", (evt)=>{
    const artId=evt.target.value  
    fetch(`/${artId}/removeartfave`, {method:"POST"}) //AJAX request to db
})