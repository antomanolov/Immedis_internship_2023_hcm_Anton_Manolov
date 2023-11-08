const token = localStorage.getItem('authToken')
const userId = JSON.parse(localStorage.getItem('userInfo')).id


document.getElementById('task-form').addEventListener('submit', function (event) {
    event.preventDefault();
        
            const formData = new FormData(this);
            const csrfToken = formData.get('csrfmiddlewaretoken');
            const taskData = {};
            formData.forEach((value, key) => {
                
                taskData[key] = value;
            });
            
        fetch('/bff/api/add_task/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken.toString(),
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'For-User-ID': userId,
                },
                mode:'cors',
                cache:'no-cache',
                body: JSON.stringify(taskData),
            })
        .then (response => {
            console.log(response.status)
            if (response.status === 201) {
                // Successful response
                alert('Task created');
                window.location.href = '/';
            } else if (response.status === 403) {
                alert('You forgot your credentials!');
            } else {
                alert('The task is not created');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
        
        
        
})
