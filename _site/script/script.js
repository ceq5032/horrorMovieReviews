// Function to search through header elements
function searchHeaders() {
    const searchInput = document.getElementById('search').value.toLowerCase(); // Get the search input value
    const headers = document.querySelectorAll('h2'); // Select all h2 elements

    for (var i = 0, length = headers.length; i < length; i++) {
        if (headers[i].innerHTML.toLowerCase().indexOf(searchInput) > -1) {
            console.log(searchInput + ' hello' + headers[i].innerHTML.toLowerCase());
            headers[i].closest('div.containerM').style.display = "block"; // Show the container
            console.log(headers[i].closest('div.containerM'));
        } else {
            headers[i].closest('div.containerM').style.display = "none"; // Hide the container
        }
    }
}

// Wait for the DOM content to load
window.addEventListener("DOMContentLoaded", function () {
    const currentPage = window.location.pathname.split("/").pop();

    // Show horror warning on specific pages
    if (currentPage === "index.html" && !localStorage.getItem("horrorWarningAccepted")) {
        alert("⚠ WARNING: This website contains horror content, including disturbing images, eerie sounds, and unsettling themes. Viewer discretion is advised.");
        localStorage.setItem("horrorWarningAccepted", "true");
    }

    // Show different warning for another page
    if (currentPage === "movie.html" && !localStorage.getItem("spoilerWarningAccepted")) {
        alert("⚠ WARNING: This page contains spoilers!!");
        localStorage.setItem("spoilerWarningAccepted", "true");

        // Call searchHeaders function on page load
        searchHeaders();

        // Fix for the input event listener
        var input = document.getElementById("search"); // Make sure the ID matches your HTML element
        input.addEventListener('keyup', searchHeaders, false); // Add event listener for keyup event
    }
});




