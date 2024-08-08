document.addEventListener("DOMContentLoaded", function () {
  var urlPath = window.location.pathname;
  var path = String(urlPath);

  function showSubmenu(option) {
    if (option === "Us" && path.includes("pre_standalone")) {
      document.getElementById("navbar").style.display = "flex";
      document.getElementById("ru_navbar").style.display = "none";
    }
    if (option === "Ru" && path.includes("Ru")) {
      document.getElementById("ru_navbar").style.display = "flex";
      document.getElementById("navbar").style.display = "none";
    }
  }

  // Show the corresponding page based on the URL path
  for (var pageId in urlPaths) {
    if (urlPaths[pageId] === urlPath) {
      showPage(pageId);
      break;
    }
  }

  // Initialize Select2
  $("#table").select2();

  // Handle the first form submission
  $("#jurisdictionForm").submit(function (event) {
    event.preventDefault(); // Prevent the defaul t form submission

    // Send an AJAX request to submit the form data
    $.ajax({
      type: "POST",
      url: $(this).attr("action"), // Ensure the form action is set correctly
      data: $(this).serialize(),
      success: function (response) {
        // Keep the page visible and show the second form
        $("#juri_table").removeClass("hidden").addClass("visible");
      },
      error: function (xhr, status, error) {
        // Handle the error if needed
        console.error("Form submission failed:", status, error);
      },
    });
  });

  // Function to show the specified page and hide others
  function showPage(pageId) {
    var pages = document.querySelectorAll(".page");
    pages.forEach(function (page) {
      if (page.id === pageId) {
        page.classList.remove("hidden");
        page.classList.add("visible");
      } else {
        page.classList.remove("visible");
        page.classList.add("hidden");
      }
    });
    showSubmenu("Us");
    showSubmenu("Ru");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const cells = document.querySelectorAll(".text-cell");
  cells.forEach((cell) => {
    const fullText = cell.getAttribute("data-full-text");
    const words = fullText.split(" ");
    if (words.length > 5) {
      const truncatedText = words.slice(0, 5).join(" ");
      cell.innerHTML = `${truncatedText} <span class="more-link">...more</span>`;
      cell.querySelector(".more-link").addEventListener("click", function () {
        cell.innerHTML = `${fullText} <span class="less-link">...less</span>`;
        cell.querySelector(".less-link").addEventListener("click", function () {
          cell.innerHTML = `${truncatedText} <span class="more-link">...more</span>`;
        });
      });
    }
  });
});
