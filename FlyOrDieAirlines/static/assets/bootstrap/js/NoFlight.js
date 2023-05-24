to_flight_noflight = document.getElementById('to_flight_noflight');
return_flight = document.getElementById('return_flight');
return_flight_noflight = document.getElementById('return_flight_noflight');


if (to_flight_noflight)
{
    return_flight.style.marginTop = "-3.5%";
    return_flight.style.marginLeft = "50%";
    document.getElementById('selectedFlightId').remove();
    document.getElementById('next').addEventListener('click', function()
    {
        document.getElementById('flightForm').submit();
    });
}

if (return_flight_noflight)
{
    return_flight_noflight.style.marginTop = "2%";
    document.getElementById('selectedReturnFlightId').remove();
    document.getElementById('next').addEventListener('click', function()
    {
        document.getElementById('flightForm').submit();
    });
}



