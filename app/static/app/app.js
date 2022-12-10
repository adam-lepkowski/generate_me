var icons = document.querySelectorAll(".clipboard-icon")

for (i=0; i < icons.length; i++) {
    icons[i].addEventListener("click", function() {
        var icon = this;
        navigator.clipboard.writeText(icon.parentElement.children[1].value);
    })
}
