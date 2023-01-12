"use strict"
// THIS is the file i need a review on...test the ux w/ instructor 
//during q


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

//logged-in + add collection fave
let btn = document.querySelector("#addfave"); //for the add to faves btn

const toDo = (evt)=>{
    evt.preventDefault();
    
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
};


//logged-in + remove collection fave-APPROVED
let btn2 = document.querySelector("#removefave"); //for the add to faves btn

const toDo2 = (evt)=>{
    evt.preventDefault();

    const collectionId=evt.target.value  
    // console.log(collectionId)
    fetch(`/collections/${collectionId}/removecollectionfavorites`, {method:"POST"}) //AJAX request to db
    alert("You must log in to remove a favorite a collection.")
    //id have 2 logged in buttons and 1 logged out buttons
};

btn2.addEventListener("click", toDo2)

//logged-in + add collection fave-APPROVED
// btn.addEventListener("click", toDo);

// let btn = document.querySelector("#addfave"); //for the add to faves btn

// btn.addEventListener("click", (evt)=>{
//     let collectionId = evt.target.value;
//     fetch(`/collections/${collectionId}/collectionfavorites`, {method:"POST"})
//     .then((response)=> response.json())
//     .then((result)=>{
//             //conditional;if result
//             if (result.status === "FAIL"){
//                 alert("You must log in to favorite a collection.")
//             }
//         }
//     )
// })

//logged-in + remove collection fave-APPROVED
// let btn2 = document.querySelector("#removefave"); //for the add to faves btn

// btn2.addEventListener("click", (evt)=>{
//     const collectionId=evt.target.value  
//     // console.log(collectionId)
//     fetch(`/collections/${collectionId}/removecollectionfavorites`, {method:"POST"}) //AJAX request to db
// })

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////      ART OBJ FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// add evt.listener to the button...fetch the dog image 
// from api resource...make that response json...
// the jsonified response, put into result variable.
// declare a variable that will be the results message (const imageUrl = result.message;)
// grab the ENTIRE dive that image is supposed to be inside of and insert html innit
// html that is a div of and img element with the declared image url variable 

// FURTHER STUDY

// document.querySelector('#get-dog-image').addEventListener('click', () => {
//     fetch('https://dog.ceo/api/breeds/image/random')
//       .then((response) => response.json())
//       .then((result) => {
//         const imageUrl = result.message;
//         document
//           .querySelector('#dog-image')
//           .insertAdjacentHTML('beforeend', `<div><img src=${imageUrl}></div>`);
//       });
//   });