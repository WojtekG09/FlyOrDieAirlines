function CheckRadio(val)
{
    if(val == 1)
    {
        document.getElementById('select_arrival').style.display = 'block';
        document.getElementById('arrival').disabled = false;

    }
    else
    {
        document.getElementById('select_arrival').style.display = 'none';
        document.getElementById('arrival').disabled = true;
        // document.getElementById('return_column_title').style.display = 'none';
        // document.getElementById('return_flight_noflight').style.display = 'none';
        // document.getElementById('return_flight').style.display = 'none';
    }
}

