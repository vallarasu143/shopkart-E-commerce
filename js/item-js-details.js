
//user menu bar show function
const button=document.querySelector('.click');
button.onclick=function(){
document.getElementById('id-arasu').style.display='block';
}


//user menu bar close function
const closemenubar=document.querySelector('.close');
const list=document.querySelector('.user-menu');
closemenubar.onclick = function(){
    document.getElementById('id-arasu').style.display='none';
}

//login form error message closing function
