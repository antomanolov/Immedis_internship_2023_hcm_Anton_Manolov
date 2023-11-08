const token = localStorage.getItem('authToken')

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
                },
                mode:'cors',
                cache:'no-cache',
                body: JSON.stringify(taskData),
            })
        // .then (response => {
            
        //     if (response.status === 201) {
        //         // Successful response
        //         alert('Employee created');
        //         window.location.href = '/';
        //     } else if (response.status === 403) {
        //         alert('Something');
        //     } else {
        //         alert('The email must be unique! User with this email is existing!');
        //     }
        // })
        // .catch(error => {
        //     console.error('Error:', error);
        // });
        
        
        
        
})
