function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    var file = event.dataTransfer.files[0];
    readAddress(file);
}

function readAddress(file) {
    var reader = new FileReader();
    reader.onload = function(event) {
        var address = event.target.result;
        console.log("File address:", address);
        sendData(address); // Send address to the server
    };
    reader.readAsDataURL(file);
}

function sendData(address) {
    var redShift = document.getElementById("red_shift").value;
    var blueShift = document.getElementById("blue_shift").value;
    var greenShift = document.getElementById("green_shift").value;

    var data = {
        image_address: address,
        red_shift: redShift,
        blue_shift: blueShift,
        green_shift: greenShift
    };

    // Send data to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/process_image", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
        }
    };
    xhr.send(JSON.stringify(data));
}