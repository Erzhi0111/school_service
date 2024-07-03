'use strict'

<<<<<<< HEAD

// Логика добавления группы в Базу Данных

function addData() {
    const data = {
        group_name: document.getElementById('group_name_input').value
    }

    fetch('http://127.0.0.1:8000/groups', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
=======
const data = {
    name: 'Название группу'
}

const group_add_btn = document.getElementById('group_add_btn')

group_add_btn.onclick = () => {
    fetch('http://localhost:5000/groups', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
>>>>>>> myrepo/main
        },
        body: JSON.stringify(data),
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json()
    }).then(data => {
<<<<<<< HEAD
        if (data.status == 'FAILED') {
            alert('Такая группа уже существует в БД')
        } else {
            alert('Данные успено сохранены в БД')
            window.location.reload()
        }
=======
        console.log('Данные успено сохранены в БД,', data)
>>>>>>> myrepo/main
    }).catch(error => {
        console.log('Ошибка при добавлении в БД,', error)
    })
}


<<<<<<< HEAD
// Логика удаления группы из базы данных

function deleteGroup(groupId) {
    const data = {group_id: groupId}

    fetch('http://127.0.0.1:8000/groups', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json()
    }).then(data => {
        alert('Группа удалена из БД')
        window.location.reload()
    }).catch(error => {
        alert('Группа связана с другой сущностью в БД, невозможно удалить', error)
    })
}

const group_name_input = document.getElementById('edit_group_name')
let group_id = null

function editGroup(group) {
    group_name_input.value = group.name
    group_id = group.id
}

function saveGroupData() {
    const data = {
        group_name: group_name_input.value,
        group_id: group_id
    }

    fetch('http://127.0.0.1:8000/groups', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json()
    }).then(data => {
        alert('Данные обновлены успешно в БД!')
        window.location.reload()
    }).catch(error => {
        alert('Ошибка при обновлении данных в БД', error)
    })
}
=======
const getCookie = (name) => {
    return document.cookie.split(';').reduce((prev, c) => {
        let arr = c.split('=');
        return (arr[0].trim() === name) ? arr[1] : prev;
    }, undefined);
};
>>>>>>> myrepo/main
