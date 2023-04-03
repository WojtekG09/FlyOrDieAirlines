window.CheckDropDowns = function(thisSelect)
{
    var otherSelectId = ("select_from_box" == thisSelect.id) ? "select_to_box" : "select_from_box";
    var otherSelect = document.getElementById(otherSelectId);

    for (i = 0; otherSelect.options.length; i++)
    {
        otherSelect.options[i].style.display = 'block';
        if (otherSelect.options[i].value == thisSelect.value)
        {
            otherSelect.options[i].style.display = 'none';
        }
    }
}
