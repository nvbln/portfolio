// Include the navbar on the page.
fetch('navbar.html')
.then(response => response.text())
.then(data => document.getElementById('navbar').innerHTML = data);

// Hide the navbar after clicking on any of its elements.
document.querySelector(".navbar").addEventListener('click', function() {
  document.querySelectorAll('.navbar .collapse').forEach(function (element) {
    new bootstrap.Collapse(element).hide();
  });
});
