errors = {"BadCredentialsError": "Неверный логин и/или пароль!"}

async function login() {
    data = { "username": document.getElementById("floatingInput").value, "password": document.getElementById("floatingPassword").value }

    response = await fetch('/api/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    response_json = await response.json();

    if (response.ok) {
        document.cookie = "token=" + response_json['token'] + '; path=/';
        window.location.replace('/app/');
    }
    else {
        var myModal = new bootstrap.Modal(document.getElementById('myModal'));
        document.getElementsByClassName("modal-title")[0].innerText = errors[response_json['error']];
        myModal.toggle();
    }
}