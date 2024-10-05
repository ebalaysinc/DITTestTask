errors = {
    "TitleNotExistError": "Тайтла не существует!"
}

const token = "Token " + document.cookie.match(new RegExp("; |token=([0-z]+[^; ])"))[1];
const id = window.location.pathname.split("/").reverse().filter(a => a)[0];

async function onLoad(){
    var form = document.getElementById("modalCreate");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);

    const regexToken = new RegExp("; token=([0-z]+[^; ])");

    data = {'id': id};

    response = await fetch("/api/getAllChapters/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        },
        body: JSON.stringify(data)
    });

    response_json = await response.json();

    if (response.status == 401) {
        document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        window.location.replace("/signin/")
    } else if (response.status == 400) {
        var myModal = new bootstrap.Modal(document.getElementById('myModal'));
        document.getElementsByClassName("modal-title")[0].innerText = errors[response_json['error']];
        myModal.toggle();
    } else {
        chapters = response_json['chapters'];
    
        var list_item = document.getElementById('originalItem');
    
        chapters.forEach(chapter => {
            var clone = list_item.cloneNode(true);
            clone.id = chapter['id'];
            clone.style = "";
            clone.querySelector(".float-start").innerText = chapter['name'];
            clone.querySelector(".float-end").innerText = !chapter['status'] ? 'В РАБОТЕ' : 'ЗАВЕРШЁН';
            list_item.parentNode.appendChild(clone);
        });
    
        list_item.remove();

        response = await fetch("/api/getTitle/", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              "Authorization": "Token " + document.cookie.match(regexToken)[1]
            },
            body: JSON.stringify(data)
        });

        response_json = await response.json();

        updateTitleData(response_json['title']);
    }
}

function editTitleModal(){
    var myModal = new bootstrap.Modal(document.getElementById('modalEdit'));
    myModal.toggle();
}

async function editTitle(){
    data = {
        'id': id,
        'name': document.getElementById("floatingName").value,
        'link': document.getElementById("floatingLink").value
    }

    response = await fetch("/api/title/editTitle/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        },
        body: JSON.stringify(data)
    });

    response_json = await response.json();

    // console.log(data);

    updateTitleData(response_json['title']);

    document.getElementById('modelEditClose').click();

    // console.log(response_json);
}

function updateTitleData(title) {
    document.getElementById("titleName").innerText = title['name'];
    document.getElementById("titleLink").innerText = title['link'];
    document.getElementById("titleLink").href = title['link'];

    
    document.getElementById("floatingName").value = title['name'];
    document.getElementById("floatingLink").value = title['link'];
}

function deleteTitleModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modalChoice'));
    myModal.toggle();
}

async function deleteTitle() {
    response = await fetch("/api/title/deleteTitle/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        },
        body: JSON.stringify({'id': id})
    });
    window.location.href = "/";
}

function createChapterModal(){
    var myModal = new bootstrap.Modal(document.getElementById('modalCreate'));
    myModal.toggle();
}

async function createChapter() {
    data = {
        'id': id,
        'name': document.getElementById('floatingChapterName').value,
        'status': document.querySelector('input[name="wip"]:checked').id,
        'original': document.getElementById('floatingOriginal').value
    }

    if (data['name'] === "" | data['original'] === "") {
        if (document.getElementById('errorText') != null) {}
        else {
            errorText = document.createElement('p');
            errorText.id = "errorText";
            errorText.innerText = 'Нельзя оставлять строки пустыми!';
            errorText.classList.add('text-danger')
            document.getElementById('modalForm').append(errorText)
        }
    } else {
        response = await fetch("/api/chapter/createChapter/", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              "Authorization": token
            },
            body: JSON.stringify(data)
        });

        window.location.reload();
    }

    // console.log(data);
}

function redirectToChapter(element) {
    window.location = '/chapter/' + element.id;
}

document.addEventListener("DOMContentLoaded", onLoad);