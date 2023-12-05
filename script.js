document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("input").addEventListener("input", function() {
        var inputValue = document.getElementById("input").value;
        var outputElement = document.getElementById("output");
        outputElement.innerHTML = inputValue;
    });
});