var icons = document.querySelectorAll(".clipboard-icon")

for (i=0; i < icons.length; i++) {
    icons[i].addEventListener("click", function() {
        var icon = this;
        navigator.clipboard.writeText(icon.parentElement.children[1].value);
        icon.parentElement.children[3].innerText = "Copied!"
    })
    
    icons[i].addEventListener("mouseover", function(){
        var icon = this;
        icon.parentElement.children[3].style.visibility = "visible";
    })

    icons[i].addEventListener("mouseout", function(){
        var icon = this;
        icon.parentElement.children[3].style.visibility = "hidden";
        icon.parentElement.children[3].innerText = "Copy";
    }) 
}
