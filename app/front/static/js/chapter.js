errors = {
    "TitleNotExistError": "Тайтла не существует!"
}

const token = "Token " + document.cookie.match(new RegExp("; token=([0-z]+[^; ])"))[1];
const id = window.location.pathname.split("/").reverse().filter(a => a)[0];
let workersCache = {};

async function onLoad(){
    var form = document.getElementById("modalCreate");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);
    var form = document.getElementById("modalForm");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);

    const regexToken = new RegExp("; token=([0-z]+[^; ])");

    data = {'id': id};

    response = await fetch("/api/getAllWorkers/", {
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
        workers = response_json['workers'];

        var list_item = document.getElementById('originalItem');
    
        workers.forEach(worker => {
            var clone = list_item.cloneNode(true);
            clone.id = worker['id'];
            clone.style = "";
            clone.querySelector(".float-start").innerText = worker['nickname'];
            clone.querySelector(".float-end").innerText = worker['occupation'];
            clone.querySelector("p").innerText = worker['contact'];
            list_item.parentNode.appendChild(clone);

            workersCache[worker['id'].toString()] = {
                'nickname': worker['nickname'],
                'contact': worker['contact'],
                'occupation': worker['occupation']
            };
        });
    
        list_item.remove();

        response = await fetch("/api/getChapter/", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              "Authorization": "Token " + document.cookie.match(regexToken)[1]
            },
            body: JSON.stringify(data)
        });

        response_json = await response.json();

        updateChapterData(response_json['chapter']);
    }
}

function editChapterModal(){
    var myModal = new bootstrap.Modal(document.getElementById('modalEdit'));
    myModal.toggle();
}

async function editChapter(){
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
        response = await fetch("/api/chapter/editChapter/", {
           method: 'POST',
           headers: {
              'Content-Type': 'application/json',
              "Authorization": token
            },
            body: JSON.stringify(data)
       });

        response_json = await response.json();

        updateChapterData(response_json['chapter']);

        document.getElementById('modelEditClose').click();

        // console.log(response_json);
    }
}

function updateChapterData(chapter) {
    document.getElementById("chapterName").innerText = chapter['name'];
    document.getElementById("chapterStatus").innerText = !chapter['status'] ? '[В РАБОТЕ]' : '[ЗАВЕРШЁН]';
    document.getElementById("chapterLink").innerText = chapter['original'];
    document.getElementById("chapterLink").href = chapter['original'];

    
    document.getElementById("floatingChapterName").value = chapter['name'];
    document.getElementById("floatingOriginal").value = chapter['original'];
    document.getElementById(!chapter['status'] ? '0' : '1').click();
}

function deleteChapterModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modalChoice'));
    myModal.toggle();
}

async function deleteChapter() {
    response = await fetch("/api/chapter/deleteChapter/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        },
        body: JSON.stringify({'id': id})
    });
    history.back();
}

function createWorkerModal(){
    var myModal = new bootstrap.Modal(document.getElementById('modalCreate'));
    myModal.toggle();
}

async function createWorker() {
    data = {
        'id': id,
        'nickname': document.getElementById('floatingWorkerName').value,
        'contact': document.getElementById('floatingContact').value,
        'occupation': document.getElementById('floatingOccupation').value
    }

    if (data['nickname'] === "" | data['contact'] === "" | data['occupation'] === "") {
        if (document.getElementById('errorText') != null) {}
        else {
            errorText = document.createElement('p');
            errorText.id = "errorText";
            errorText.innerText = 'Нельзя оставлять строки пустыми!';
            errorText.classList.add('text-danger')
            document.getElementById('modalCreate').append(errorText)
        }
    } else {
        response = await fetch("/api/worker/createWorker/", {
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

function editWorkerModal(element) {
    var myModal = new bootstrap.Modal(document.getElementById('modalWorkerEdit'));

    worker = workersCache[element.id];

    document.querySelectorAll(".lalala").forEach(button => {
        button.id = element.id;
    })

    document.getElementById('floatingWorkerNameEdit').value = worker['nickname'];
    document.getElementById('floatingContactEdit').value = worker['contact'];
    document.getElementById('floatingOccupationEdit').value = worker['occupation'];

    myModal.toggle();
}

async function editWorker(element) {
    data = {
        'id': element.id,
        'nickname': document.getElementById('floatingWorkerNameEdit').value,
        'contact': document.getElementById('floatingContactEdit').value,
        'occupation': document.getElementById('floatingOccupationEdit').value
    }

    console.log(data);

    if (data['nickname'] === "" | data['contact'] === "" | data['occupation'] === "") {
        if (document.getElementById('errorText') != null) {}
        else {
            errorText = document.createElement('p');
            errorText.id = "errorText";
            errorText.innerText = 'Нельзя оставлять строки пустыми!';
            errorText.classList.add('text-danger')
            document.getElementById('modalForm3').append(errorText);
        }
    } else {
        response = await fetch("/api/worker/editWorker/", {
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

async function deleteWorker(element) {
    data = {
        'id': element.id,
    }

    response = await fetch("/api/worker/deleteWorker/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          "Authorization": token
        },
        body: JSON.stringify(data)
    });

    window.location.reload();
}

document.addEventListener("DOMContentLoaded", onLoad);