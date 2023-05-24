function NextBtn()
{
    if (document.getElementById('selectedFlightId').value == "")
    {
        alert('please select the flight ticket');
        return false;
    }

    if (document.getElementById('selectedReturnFlightId').value == "")
    {
        alert('please select the return flight ticket');
        return false;
    }

    else
    {
        document.getElementById('next').addEventListener('click', function()
        {
            document.getElementById('flightForm').submit();
        });
    }
}