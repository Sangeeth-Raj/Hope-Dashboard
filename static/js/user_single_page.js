var userRows = document.querySelectorAll("tbody tr");

// Add click event listener to each row
userRows.forEach(function (row) {
    row.addEventListener("click", function () {
        // Get the therapist ID from the row
        var userId = row.querySelector("td:nth-child(2)").textContent;

        // Redirect to the single page for the therapist
        window.location.href = "/user-admin/user/" + userId; // Change the URL structure as needed
    });
});
