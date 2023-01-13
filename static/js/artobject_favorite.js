"use strict"
// alert("connected!!!!!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////     ART OBJ in COLLECTION FAVES
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//logged-in/out + add art fave
let btn3 = document.querySelector("#addartfave"); //for the add to faves btn

btn3.addEventListener("click", (evt)=>{
    let artId = evt.target.value;
    fetch(`/${artId}/artfave`, {method:"POST"})
    .then((response)=> response.json())
    .then((result)=>{
            //conditional;if result
            if (result.status === "FAIL"){
                alert("You must log in to favorite artwork.")
            }
        }
    )
})

//logged-in + remove art fave
let btn4 = document.querySelector("#removeartfave"); //for the add to faves btn

btn4.addEventListener("click", (evt)=>{
    const artId=evt.target.value  
    fetch(`/${artId}/removeartfave`, {method:"POST"}) //AJAX request to db
})
