var therapistRows = document.querySelectorAll("tbody tr");

// Add click event listener to each row
therapistRows.forEach(function (row) {
    row.addEventListener("click", function () {
        // Get the therapist ID from the row
        var therapistId = row.querySelector("td:nth-child(2)").textContent;

        // Redirect to the single page for the therapist
        window.location.href = "/user-admin/therapist/" + therapistId; // Change the URL structure as needed
    });
});
