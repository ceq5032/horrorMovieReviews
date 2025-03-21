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

// Function to set active link
function setActive(element) {
    // Remove active class from all list items
    document.querySelectorAll("ul.htop li").forEach(li => li.classList.remove("active"));
    // Add active class to the clicked item's parent
    element.parentElement.classList.add("active");

    // Save the active page to localStorage
    localStorage.setItem("activePage", element.href);
}

window.onbeforeunload = function() {
    localStorage.clear(); // Clear the localStorage when the page is about to be closed
};



