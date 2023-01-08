"use strict"
// alert("connected!!!!!")


//upon clicking on collection from collection list page, it should load all the art objects on page

///view museum faves on patron profile
//it'd be a link to click on

//create a function that add an element object thats a div 
//with a pic inside at before end of inner adjacent html

// function showMuseumFave() 
//fetch resource from server (the museum fave resource that 
    //returns response json with )
    //figure out what type of responses server can send in fetch request


// function replaceCardText(results) {
//     document.querySelector('#ajax-test').innerHTML = results;
//     }


//DIDNT WORK
// document.querySelector('#ajax').addEventListener('click', ()=>{
//     fetch('/collections/${id}/${art}')
//         // .then((response) => response.json())
//         .then((response) => response.text())
//         .then((result)=> {
//         document.querySelector('#ajax-test').innerHTML = result;
//         });
// })


// Qselect event target in html by id or class
// add EL (evtType, ()=> {anon function with fetch() and .then((response)) .then((result))); 
//                      }); });

//grab the html object via id or class
//add EL
//event type
//anon func:
    //fetch the url of image


///for tab1: museum faves on patron profile
// document.querySelector('#museumfavecard').addEventListener('click', () => {
//         // send a fetch request to the show-museum-fave route
//         fetch('/api/museum-faves')
//         .then((response) => {
//             if (not 'Must Login' == response) {		//<——js references the response being true or not in a conditional 
//                 document.querySelector(`span.show-muse-fave_${museum.id}`).innerHTML = response; //<—need help
//             } else {
//                 alert(‘Check out museums, sounds, art and collections to favorite!’);
//             });
//         });



// //dell tab click events
// https://www.delldesignsystem.com/components/tabs/
// const element = document.getElementById("#dell-tabs");
// DDS.Tabs(element, { moreLabel: More });