function showHiddenMenu() {
    var x = document.getElementById("hamburger-contents");
    if (x.className === "hidden-navbar") {
      x.className = "shown-navbar";
    } else {
      x.className = "hidden-navbar";
    }
  }