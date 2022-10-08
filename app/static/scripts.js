function validateInput() {
    let query = document.getElementById("txtInput").value;
    console.log("Validate Input")
    if (query != "") {
        const queryForm = document.getElementById("queryForm");
        queryForm.submit();
        return true;
    }
    return false;
}