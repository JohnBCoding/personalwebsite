window.onload = function(){

    function toggleDropdown(){

        // Check if drop down is visible or not, then toggle it.
        if(document.getElementById("collapse").style.display == "block"){
            document.getElementById("collapse").style.display = "none";
        } else{
            document.getElementById("collapse").style.display = "block";
        }
    }

    document.getElementById("dropdownBtn").onclick = toggleDropdown;

    window.onclick = function(event){
        // Click anywhere in the window, don't trigger if click was on the dropdown button.
        if(event.target.id !== "dropdownBtn"){
            // Check if class is already added, remove if it is.
            if(document.getElementById("collapse").style.display == "block"){
                document.getElementById("collapse").style.display = "none";
            }
        }
    }
}
