const navItems = document.querySelectorAll(".nav-item");
navItems.forEach((item) => {
    item.addEventListener("click", () => {
        navItems.forEach((item) => {
            item.classList.remove("active");
        });
        item.classList.add("active");
        console.log("object");
    });
});


document.addEventListener("DOMContentLoaded", function () {
    var table = document.getElementById("userTable");
    var rows = table.getElementsByTagName("tr");
    var rowsPerPage = 11;
    var currentPage = 0;

    function showPage(page) {
        var start = page * rowsPerPage;
        var end = start + rowsPerPage;
        for (var i = 0; i < rows.length; i++) {
            if (i >= start && i < end) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }

    function createPagination() {
        var pageCount = Math.ceil(rows.length / rowsPerPage);
        var pagination = document.getElementById("pagination");
        pagination.innerHTML = "";
        for (var i = 0; i < pageCount; i++) {
            var button = document.createElement("button");
            button.innerText = i + 1;
            button.addEventListener("click", function () {
                currentPage = parseInt(this.innerText) - 1;
                showPage(currentPage);
            });
            pagination.appendChild(button);
        }
    }

    function updatePagination() {
        var buttons = document.querySelectorAll(".pagination button");
        buttons.forEach(function (btn) {
            btn.classList.remove("active");
        });
        buttons[currentPage].classList.add("active");
    }

    createPagination();
    showPage(currentPage);

    var prevBtn = document.getElementById("prevBtn");
    var nextBtn = document.getElementById("nextBtn");

    prevBtn.addEventListener("click", function () {
        if (currentPage > 0) {
            currentPage--;
            showPage(currentPage);
            updatePagination();
        }
    });

    nextBtn.addEventListener("click", function () {
        if (currentPage < Math.ceil(rows.length / rowsPerPage) - 1) {
            currentPage++;
            showPage(currentPage);
            updatePagination();
        }
    });
});

// Get the current path of the page
var currentPath = window.location.pathname;

// Get all navigation links
var navLinks = document.querySelectorAll('nav a');

// Iterate through each navigation link
navLinks.forEach(function(link) {
    // Check if the current path matches the link's href attribute
    if (currentPath === link.getAttribute('href')) {
        // Add the active class to the link's parent <li> element
        link.parentElement.classList.add('active');
    }
});