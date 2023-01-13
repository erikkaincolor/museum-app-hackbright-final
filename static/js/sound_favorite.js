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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////     SOUNDS in COLLECTION OBJ FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//logged-in/sound + add sound fave
let btn5 = document.querySelector("#addsoundfave"); //for the add to faves btn

const soundBtn = (evt)=>{
    let soundId = evt.target.value;
    fetch(`/${soundId}/soundfavorites`, {method:"POST"})
    .then((response)=> response.json())
    .then((result)=>{
            //conditional;if result
            if (result.status === "FAIL"){
                alert("You must log in to favorite a sound.")
            }
        }
    )
};

btn5.addEventListener("click", soundBtn); //i want this to be for first button 
btn7.addEventListener("click", soundBtn); //and the second to be for the second

//logged-in + remove sound fave
let btn6 = document.querySelector("#removesoundfave"); //for the add to faves btn

btn6.addEventListener("click", (evt)=>{
    const soundId=evt.target.value  
    fetch(`/${soundId}/removesoundfavorites`, {method:"POST"}) //AJAX request to db
})



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////     SOUNDS in MUSEUM OBJ FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//logged-in/sound + add sound fave
let btn7 = document.querySelector("#addsoundfave"); //for the add to faves btn

// btn7.addEventListener("click", (evt)=>{
//     let soundId = evt.target.value;
//     fetch(`/${soundId}/soundfavorites`, {method:"POST"})
//     .then((response)=> response.json())
//     .then((result)=>{
//             //conditional;if result
//             if (result.status === "FAIL"){
//                 alert("You must log in to favorite a sound.")
//             }
//         }
//     )
// })

//logged-in + remove sound fave
let btn8 = document.querySelector("#removesoundfave"); //for the add to faves btn

btn8.addEventListener("click", (evt)=>{
    const soundId=evt.target.value  
    fetch(`/${soundId}/removesoundfavorites`, {method:"POST"}) //AJAX request to db
})
