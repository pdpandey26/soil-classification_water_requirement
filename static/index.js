function openNav() {
    document.getElementById("myNav").style.width = "100%";
  }
function openNav1() {
    document.getElementById("myNav1").style.width = "100%";
  }
function openNav2() {
    document.getElementById("myNav2").style.width = "100%";
  }
function openNav3() {
    document.getElementById("myNav3").style.width = "100%";
  }
function openNav4() {
    document.getElementById("myNav4").style.width = "100%";
  }
function openNav5() {
    document.getElementById("myNav5").style.width = "100%";
  }
function openNav6() {
    document.getElementById("myNav6").style.width = "100%";
  }
function closeNav() {
    document.getElementById("myNav").style.width = "0%";
  }
function closeNav1() {
    document.getElementById("myNav1").style.width = "0%";
  }
  function closeNav2() {
    document.getElementById("myNav2").style.width = "0%";
  }
  function closeNav3() {
    document.getElementById("myNav3").style.width = "0%";
  }
  function closeNav4() {
    document.getElementById("myNav4").style.width = "0%";
  }
  function closeNav5() {
    document.getElementById("myNav5").style.width = "0%";
  }
  function closeNav6() {
    document.getElementById("myNav6").style.width = "0%";
  }
  function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  $(window).load(function() {
    $('form').get(0).reset(); //clear form data on page load
});