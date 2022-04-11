function incrementButton() {

    var element = document.getElementById('incrementUnit');
    var value = element.innerHTML;

    ++value;
    // console.log(value)
    document.getElementById('incrementUnit').innerHTML = value;
}