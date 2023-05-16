function TicketPicker(button) {
  var flightId = button.id.replace("istheflight_btn_", "");
  var parentDiv = button.closest(".container_flight");
  var divs = document.querySelectorAll('.container_flight');
  divs.forEach(function(div) {
    if (div !== parentDiv) {
      if (div.style.display === "none") {
        div.style.display = "block";
      } else {
        div.style.display = "none";
      }
    }
  });
}
