const token = "Token " + document.cookie.match(new RegExp("; |token=([0-z]+[^; ])"))[1];

async function onLoad(){
    var form = document.getElementById("modalForm");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);

    response = await fetch('/api/getAllTitles/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        }
    });

    if (response.status == 401) {
        document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        window.location.replace("/signin/")
    }

    response_json = await response.json();
    titles = response_json['titles'];

    var list_item = document.getElementById('originalItem');

    titles.forEach(title => {
        var clone = list_item.cloneNode(true);
        clone.id = title['id'];
        clone.style = "";
        clone.querySelector("h6").innerText = title['name'];
        list_item.parentNode.appendChild(clone);
    });

    list_item.remove();
}

function redirectToChapters(element) {
    window.location = '/title/' + element.id;
}

function createTitleModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modalCreate'));
    myModal.toggle();
}

async function createTitle() {
    data = {
        'name': document.getElementById("floatingName").value,
        'link': document.getElementById("floatingLink").value
    }

    if (data['name'] === "" | data['link'] === "") {
        if (document.getElementById('errorText') != null) {}
        else {
            errorText = document.createElement('p');
            errorText.id = "errorText";
            errorText.innerText = 'Нельзя оставлять строки пустыми!';
            errorText.classList.add('text-danger')
            document.getElementById('modalForm').append(errorText)
        }
    }

    else {
        response = await fetch("/api/title/createTitle/", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              "Authorization": token
            },
            body: JSON.stringify(data)
        });

        window.location.reload();
    }

}

function logout() {
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.href = "/";
}

document.addEventListener("DOMContentLoaded", onLoad)