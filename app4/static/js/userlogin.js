function button() {
    var username = document.getElementById('username')
    var password = document.getElementById('Password')
    if (username.value == "") {
        document.getElementById('username').innerHTML = 'enter username'
        return false

    }
    if (password.value == "") {
        document.getElementById('password').innerHTML = 'enter password'
        return false
    }

}

// var modal = document.getElementById('id01');

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }