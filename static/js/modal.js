// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementsByClassName("backgroundButton")[0];

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Get the "Cancel" button
var cancelButton = document.querySelector(".buttonContainer button[type='reset']");

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x) or "Cancel" button, close the modal
span.onclick = cancelButton.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});
