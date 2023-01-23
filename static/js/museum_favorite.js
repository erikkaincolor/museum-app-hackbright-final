"use strict"
// alert("connected!!!!!")

let btn = document.querySelector("#addmusefave"); //for the add to faves btn
let btn1 = document.querySelector("#removemusefave"); //for the add to faves btn
// let btn3 = document.querySelector("#login2addfave"); //for the add to faves btn
// https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById

//logged-in/out + add fave
//works
btn.addEventListener("click", (evt)=>{
    const museumId=evt.target.value  
    fetch(`/museumdirectory/${museumId}/museumfavorites`, {method:"POST"}) 
    .then((response)=> response.json())
    .then((result)=>{
            //conditional;if result
            if (result.status === "FAIL"){
                alert("You must log in to favorite a museum.")
            }
        }
    )
})

//logged-in + remove fave
//works
btn1.addEventListener("click", (evt)=>{
    const museumId=evt.target.value  
    fetch(`/museumdirectory/${museumId}/removemuseumfavorites`, {method:"POST"}) //AJAX request to db
})