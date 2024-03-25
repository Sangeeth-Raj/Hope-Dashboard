document.addEventListener("DOMContentLoaded", function () {
    var logoutButton = document.getElementById("logoutButton");
    var logoutModal = document.getElementById("logoutModal");
    var closeModal = document.querySelector(".close");
    var cancelButton = document.querySelector(".borderButton");

    // Function to open the logout modal
    logoutButton.addEventListener("click", function () {
        logoutModal.style.display = "block";
    });

    // Function to close the logout modal when clicking on the close button
    closeModal.addEventListener("click", function () {
        logoutModal.style.display = "none";
    });

    // Function to close the logout modal when clicking on the cancel button
    cancelButton.addEventListener("click", function () {
        logoutModal.style.display = "none";
    });

    // Function to close the logout modal when clicking outside of it
    window.onclick = function (event) {
        if (event.target == logoutModal) {
            logoutModal.style.display = "none";
        }
    };
});
