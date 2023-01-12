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

//logged-in + add art fave
let btn8 = document.querySelector("#addsoundfave"); //for the add to faves btn

btn8.addEventListener("click", (evt)=>{
    let soundId = evt.target.value;
    fetch(`/${soundId}/soundfavorites`, {method:"POST"})
    .then((response)=> response.json())
    .then((result)=>{
            //conditional;if result
            if (result.status === "FAIL"){
                alert("You must log in to favorite a collection.")
            }
        }
    )
})

//logged-in + remove art fave
let btn9 = document.querySelector("#removesoundfave"); //for the add to faves btn

btn9.addEventListener("click", (evt)=>{
    const soundId=evt.target.value  
    fetch(`/${soundId}/removesoundfavorites`, {method:"POST"}) //AJAX request to db
})
