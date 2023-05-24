function ReturnTicketPicker(button)
{
  var flightId = button.id.replace("istheflight_btn_return_", "");
  var parentDiv = button.closest(".container_flight_return");
  var divs = document.querySelectorAll('.container_flight_return');
  divs.forEach(function(div)
  {
    if (div !== parentDiv)
    {
      if (div.style.display === "none")
      {
        div.style.display = "block";
        document.getElementById('selectedReturnFlightId').value = "";
      }
      else
      {
        div.style.display = "none";
        document.getElementById('selectedReturnFlightId').value = flightId;
      }
    }
  });
}