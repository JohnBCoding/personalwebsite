window.onload = function(){

    editable_focused = false;

    // Only allow buttons(bold, italic..) to be pressed if text-area is focused.
    document.getElementById("text-area").onclick = function(){
        editable_focused = true;
        console.log(editable_focused);
    }

    // If text-area is clicked out of, don't allow buttons(bold, italic..) to be pressed
    // Unless it is the buttons being pressed.
    window.onclick = function(event){
        if(!event.target.classList.contains("text-focus")){
            editable_focused = false;
            console.log(editable_focused);
        }
    }

    // Turn text bold.
    document.getElementById("boldBtn").onmousedown = function(event){
        if(editable_focused === true){
            document.execCommand("bold");
            this.classList.toggle("active");
            event.preventDefault();
        }
    }

    // Turn text italics.
    document.getElementById("italicsBtn").onmousedown = function(event){
        if(editable_focused === true){
            document.execCommand("italic");
            this.classList.toggle("active");
            event.preventDefault();
        }
    }

    // Turn text underline.
    document.getElementById("underlineBtn").onmousedown = function(event){
        if(editable_focused === true){
            document.execCommand("underline");
            this.classList.toggle("active");
            event.preventDefault();
        }
    }

    // Send div text-area content to form submittable text-area content.
    document.getElementById("postForm").onsubmit = function(){
        document.getElementById("body").value = document.getElementById("text-area").innerHTML;
    }
}