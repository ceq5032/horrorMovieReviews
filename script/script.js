// Check if user has already accepted the warning on page load
window.onload = function () {
    if (!localStorage.getItem("horrorWarningAccepted")) {
        alert("⚠ WARNING: This website contains horror content, including disturbing images, eerie sounds, and unsettling themes. Viewer discretion is advised.");
        localStorage.setItem("horrorWarningAccepted", "true");
    }

    // Set the active link from localStorage when the page loads
    let activePage = localStorage.getItem("activePage");

    if (activePage) {
        let links = document.querySelectorAll("ul.htop li a");
        links.forEach(link => {
            // Compare the href of each link with the saved active page
            if (link.href === activePage) {
                // Remove active class from all items
                document.querySelectorAll("ul.htop li").forEach(li => li.classList.remove("active"));
                // Add active class to the corresponding link
                link.parentElement.classList.add("active");
            }
        });
    }
};


// Function to search through header elements
function searchHeaders() {
    // Get the search input and convert to lowercase
    const searchInput = document.getElementById('search').value.toLowerCase();

    // Select all header elements (h1, h2, h3)
    const headers = document.querySelectorAll('h1, h2, h3');

    // Loop through each header element
    headers.forEach(header => {
        const headerText = header.textContent.toLowerCase();

        // If the header contains the search input, show it; otherwise, hide it
        if (headerText.includes(searchInput)) {
            header.style.display = 'block'; // Show the header
        } else {
            header.style.display = 'none'; // Hide the header
        }
    });
}





