
document.addEventListener("DOMContentLoaded", function () {
    const currentPage = window.location.pathname.split("/").pop();

    // Show horror warning on specific pages
    if (currentPage === "index.html" && !localStorage.getItem("horrorWarningAccepted")) {
        alert("⚠ WARNING: This website contains horror content, including disturbing images, eerie sounds, and unsettling themes. Viewer discretion is advised.");
        localStorage.setItem("horrorWarningAccepted", "true");
    }

    // Show different warning for another page
    if (currentPage === "movie.html" && !localStorage.getItem("spoilerWarningAccepted")) {
        alert("⚠ WARNING: This page page contains spoilers!!");
        localStorage.setItem("spoilerWarningAccepted", "true");
    }

    document.addEventListener("DOMContentLoaded", function () {
        const menuToggle = document.querySelector(".menu-toggle");
        const menu = document.querySelector(".htop");

        if (!menuToggle) {
            console.log("Menu toggle button not found");
        }

        if (!menu) {
            console.log("Menu not found");
        }

       
        menuToggle.addEventListener("click", function () {
            console.log("Hamburger button clicked");
            menu.classList.toggle("active");
        });
    });


    // Function to search through header elements
    function searchHeaders() {
        const searchInput = document.getElementById('search').value.toLowerCase();
        const headers = document.querySelectorAll('h1, h2, h3');

        headers.forEach(header => {
            const headerText = header.textContent.toLowerCase();
            header.closest('div').style.display = headerText.includes(searchInput) ? 'block' : 'none';
        });
    }
});

