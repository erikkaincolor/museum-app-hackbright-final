"use strict"

// alert("connected!!!!!")

window.addEventListener("load", function(){
    setTimeout(
        function open(evt){
            document.querySelector(".home-popup").style.display = "block";
        },
        4000
    )
});

document.querySelector("#home-close").addEventListener("click", function(){
    document.querySelector(".home-popup").style.display = "none";
});

// this popup didnt work when in the same .js file as the logout popup! 
