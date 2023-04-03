var depature = document.getElementById("depature");
var arrival = document.getElementById("arrival");
arrival.min = depature.value;
depature.max = arrival.value;

depature.addEventListener("input", function ()
{
    arrival.min = depature.value;
});
arrival.addEventListener("input", function ()
{
    depature.max = arrival.value;
});