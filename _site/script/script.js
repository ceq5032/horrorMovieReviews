window.onload = function() {
    // Check if user has already accepted the warning
    if (!localStorage.getItem("horrorWarningAccepted")) {
        alert("⚠ WARNING: This website contains horror content, including disturbing images, eerie sounds, and unsettling themes. Viewer discretion is advised.");
        localStorage.setItem("horrorWarningAccepted", "true");
    }
};

function setActive(element) {

    document.querySelectorAll("ul.htop li").forEach(li => li.classList.remove("active"));
    element.parentElement.classList.add("active");
}
document.addEventListener("DOMContentLoaded", function () {
    // Get the saved active page from localStorage
    let activePage = localStorage.getItem("activePage");

    // Select all links inside .htop
    let links = document.querySelectorAll("ul.htop li a");


    links.forEach(link => {
        // Check if the link matches the stored active page
        if (link.href === activePage) {
            document.querySelectorAll("ul.htop li").forEach(li => li.classList.remove("active"));
            link.parentElement.classList.add("active");
        }

        // Add onclick event to each link
        link.addEventListener("click", function () {
            document.querySelectorAll("ul.htop li").forEach(li => li.classList.remove("active"));
            this.parentElement.classList.add("active");

            // Store the clicked link's href in localStorage
            localStorage.setItem("activePage", this.href);
        });
    });
});