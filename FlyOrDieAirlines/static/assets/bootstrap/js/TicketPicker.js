function TicketPicker(button)
{
    var flightId = button.id.replace("istheflight_btn_", "");
    var parentDiv = button.closest(".container_flight");
    var divs = document.querySelectorAll('.container_flight');
    // nextBtn = document.getElementById('next');
    divs.forEach(function(div)
    {
      if (div !== parentDiv)
      {
        if (div.style.display === "none")
        {
          div.style.display = "block";
          document.getElementById('selectedFlightId').value = "";
        }
        else
        {
          div.style.display = "none";
          document.getElementById('selectedFlightId').value = flightId;
        }
      }
    });

    // document.getElementById('selectedFlightId').value = flightId;

  }

// document.getElementById('next').addEventListener('click', function()
// {
//   document.getElementById('flightForm').submit();
// });