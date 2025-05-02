// Function to search through header elements
function searchHeaders() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const headers = document.querySelectorAll('h2');
   for (var i = 0, length = headers.length; i < length; i++)
    {
       if (headers[i].innerHTML.toLowerCase().indexOf(searchInput) > -1) {
           console.log(searchInput+' hello' + headers[i].innerHTML.toLowerCase());
          headers[i].closest('div.containerM').style.display = "block";
          console.log(headers[i].closest('div.containerM'));
     } else {
         headers[i].closest('div.containerM').style.display = "none";

      }
  }

 //   headers.forEach(header => {
      //  const headerText = header.textContent.toLowerCase();
    //    header.closest('div').style.display = headerText.includes(searchInput) ? 'block' : 'none';
  //  });
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
        // Apply the search input event listener
            var input = document.getElementById("input")|
                input.addEventListener('keyup', searchHeaders, false)
        }

<<<<<<< Updated upstream
=======
        // Call searchHeaders function on page load
        searchHeaders();

        // Fix for the input event listener
        var input = document.getElementById("search");
        input.addEventListener('keyup', searchHeaders, false);
    }
>>>>>>> Stashed changes
});




