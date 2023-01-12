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
let btn4 = document.querySelector("#addartfave"); //for the add to faves btn

btn4.addEventListener("click", (evt)=>{
    let artId = evt.target.value;
    fetch(`/${artId}/artfave`, {method:"POST"})
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
let btn5 = document.querySelector("#removeartfave"); //for the add to faves btn

btn5.addEventListener("click", (evt)=>{
    const artId=evt.target.value  
    fetch(`/${artId}/removeartfave`, {method:"POST"}) //AJAX request to db
})
