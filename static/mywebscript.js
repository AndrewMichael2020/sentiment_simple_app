let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };

    // Prepare the data to send in the POST request
    let data = new FormData();
    data.append("textToAnalyze", textToAnalyze);  // Send the text in form data

    // Open the POST request and send the data
    xhttp.open("POST", "/sent_analyze", true);
    xhttp.send(data);
};
