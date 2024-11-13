

const btn = document.getElementById("btn");  
const names = document.getElementById("name");

btn.addEventListener('click', function() {
    names.innerText = 'Hello Venkatesh !';
    names.style.color = "blue";
});