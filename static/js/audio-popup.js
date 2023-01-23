"use strict"

window.addEventListener("load", function(){
    setTimeout(
        function open(evt){
            document.querySelector(".audio-popup").style.display = "block";
        },
        1000
    )
});

document.querySelector("#audio-close").addEventListener("click", function(){
    document.querySelector(".audio-popup").style.display = "none";
});

// this popup didnt work when in the same .js file as the logout and home-alerts popups! 
