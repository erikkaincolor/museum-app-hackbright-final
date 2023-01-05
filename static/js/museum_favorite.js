"use strict"
// alert("connected!!!!!")

let btn = document.querySelector("#addfave"); //for the add to faves btn
let btn2 = document.querySelector("#removefave"); //for the add to faves btn
let btn3 = document.querySelector("#login2addfave"); //for the add to faves btn
// https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById




//logged-in + add fave
//works

btn.addEventListener("click", (evt)=>{
    const museumId=evt.target.value  
    
    fetch(`/museumdirectory/${museumId}/museumfavorites`, {method:"POST"}) 
    //fetch function parameters...this doesnt need a then or return promises in the relay
// camelCase for js vars from now on
});

//logged-in + remove fave....how to make js remove the fave on click? 
//works
btn2.addEventListener("click", (evt)=>{
    const museumId=evt.target.value  
    fetch(`/museumdirectory/${museumId}/removemuseumfavorites`, {method:"POST"}) //AJAX request to db
})
//needed to change route 




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










