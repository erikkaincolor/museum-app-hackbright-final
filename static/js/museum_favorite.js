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




// refence ajax-exercise.js, where it says updateMelons and has a .remove inside a conditional...like this:
//    document.querySelector('#order-status').classList.remove('order-error');






/////////////////////test when not logged in///////////////////////////////////////

//the below will work when conditions are met
// function handleClickOnFaves(){
//     alert('Must Login to Favorite');
// }
// btn3.addEventListener("click", handleClickOnFaves);

//NOT logged-in + add fave ....btn2
// btn3.addEventListener("click", (evt)=>{
//     const museumId=evt.target.value  
    
//     fetch(`/museumdirectory/${museumId}/museumfavorites`, {method:"POST"})
// })

// this i swha ti have in my server:
// session['patron_id'] = patron.p_id #logged in or not depends on where session is globally/locally

// if not "p_id" in session:
//     return redirect('/login') #do flash message
// p_id=session['patron_id'] #this is me retrieving the p_id via the dict.....put conditionals so its if-logged in

// current_users_uname=session.get("username") #username needed for favoriting










