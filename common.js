// Hide the navbar after clicking on any of its elements.
document.querySelector(".navbar").addEventListener('click', function() {
  document.querySelectorAll('.navbar .collapse').forEach(function (element) {
    new bootstrap.Collapse(element).hide();
  });
});

