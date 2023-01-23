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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////     COLLECTION OBJ FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//logged-in/out + add collection fave-APPROVED
let btn1 = document.querySelector("#addfave");

btn1.addEventListener("click", (evt)=>{
    let collectionId = evt.target.value;
    fetch(`/collections/${collectionId}/collectionfavorites`, {method:"POST"})
    .then((response)=> response.json())
    .then((result)=>{
            //conditional;if result
            if (result.status === "FAIL"){
                alert("You must log in to favorite a collection.")
            }
        }
    )
})

// logged-in + remove collection fave-APPROVED
let btn2 = document.querySelector("#removefave"); 

btn2.addEventListener("click", (evt)=>{
    const collectionId=evt.target.value  
    // console.log(collectionId)
    fetch(`/collections/${collectionId}/removecollectionfavorites`, {method:"POST"}) //AJAX request to db
})

