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
/////////////////////////     SOUNDS in COLLECTION, MUSEUM OBJ FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

let btn5 = document.querySelector("#addsoundfave");

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
btn5.addEventListener("click", soundBtn)









// logged-in + remove sound fave-APPROVED
let btn6 = document.querySelector("#removesoundfave"); 

btn6.addEventListener("click", (evt)=>{
    const soundId=evt.target.value  
    // console.log(collectionId)
    fetch(`/${soundId}/removesoundfavorites`, {method:"POST"}) //AJAX request to db
})

