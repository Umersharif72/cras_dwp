document.addEventListener("DOMContentLoaded", () => {
  const body = document.querySelector("body");
  const darkLight = document.querySelector("#darkLight");
  const sidebar = document.querySelector(".sidebar");
  const submenuItems = document.querySelectorAll(".submenu_item");
  const sidebarOpen = document.querySelector("#sidebarOpen");
  const sidebarClose = document.querySelector(".collapse_sidebar");
  const sidebarExpand = document.querySelector(".expand_sidebar");
  const contentContainer = document.getElementById("contentContainer");

  if (sidebarOpen) {
    sidebarOpen.addEventListener("click", () => {
      sidebar.classList.toggle("close");
      contentContainer.classList.toggle("expanded");
    });
  }

  if (sidebarClose) {
    sidebarClose.addEventListener("click", () => {
      sidebar.classList.add("close", "hoverable");
      contentContainer.classList.remove("expanded");
    });
  }

  if (sidebarExpand) {
    sidebarExpand.addEventListener("click", () => {
      sidebar.classList.remove("close", "hoverable");
      contentContainer.classList.add("expanded");
    });
  }

  if (sidebar) {
    sidebar.addEventListener("mouseenter", () => {
      if (sidebar.classList.contains("hoverable")) {
        sidebar.classList.remove("close");
      }
    });

    sidebar.addEventListener("mouseleave", () => {
      if (sidebar.classList.contains("hoverable")) {
        sidebar.classList.add("close");
      }
    });
  }

  if (darkLight) {
    darkLight.addEventListener("click", () => {
      body.classList.toggle("dark");
      if (body.classList.contains("dark")) {
        darkLight.classList.replace("bx-sun", "bx-moon");
      } else {
        darkLight.classList.replace("bx-moon", "bx-sun");
      }
    });
  }

  if (submenuItems) {
    submenuItems.forEach((item, index) => {
      item.addEventListener("click", () => {
        item.classList.toggle("show_submenu");
        submenuItems.forEach((item2, index2) => {
          if (index !== index2) {
            item2.classList.remove("show_submenu");
          }
        });
      });
    });
  }

  function adjustMainContainerWidth() {
    if (window.innerWidth < 768) {
      sidebar.classList.add("close");
      contentContainer.classList.remove("expanded");
    } else {
      sidebar.classList.remove("close");
      contentContainer.classList.add("expanded");
    }
  }

  // Initial adjustment on page load
  adjustMainContainerWidth();

  // Adjust width when window is resized
  window.addEventListener("resize", adjustMainContainerWidth);
});


// script for dynamic hiding and showing the content of diffrent div of pre-standalone 

// script for the columns extraction logics 
