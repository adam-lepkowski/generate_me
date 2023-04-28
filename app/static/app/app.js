var icons = document.querySelectorAll(".clipboard-icon");

for (i=0; i < icons.length; i++) {
    icons[i].addEventListener("click", function() {
        var icon = this;
        navigator.clipboard.writeText(icon.parentElement.children[1].value);
        icon.children[1].innerText = "Copied!"
    })
    
    icons[i].addEventListener("mouseover", function(){
        var icon = this;
        icon.children[1].style.visibility = "visible";
    })

    icons[i].addEventListener("mouseout", function(){
        var icon = this;
        icon.children[1].style.visibility = "hidden";
        icon.children[1].innerText = "Copy";
    }) 
}

/**
 * Fetch randomly generated identity json. Insert result in appropriate form
 * fields.
 */
async function fetchIdentity() {
    var url = document.querySelector("#identity-form").getAttribute("identity-url");
    response = await fetch(url, {
        method: "GET",
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    });
    var data = await response.json();
    document.querySelector("#id_first_name").value = data.first_name
    document.querySelector("#id_last_name").value = data.last_name
    document.querySelector("#id_dob").value = data.dob
    document.querySelector("#id_nickname").value = data.nickname
    if (data.gender == "male") {
        document.querySelector(".fa-mars").classList.add("icon-male")
        document.querySelector(".fa-venus").classList.remove("icon-female")
    } else {
        document.querySelector(".fa-mars").classList.remove("icon-male")
        document.querySelector(".fa-venus").classList.add("icon-female")
    }
}
