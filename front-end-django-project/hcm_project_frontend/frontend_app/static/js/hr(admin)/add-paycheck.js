const token = localStorage.getItem('authToken')
const userId = JSON.parse(localStorage.getItem('userInfo')).id


document.getElementById('paycheck-form').addEventListener('submit', function (event) {
    event.preventDefault();
        
            const formData = new FormData(this);
            const csrfToken = formData.get('csrfmiddlewaretoken');
            const paycheckData = {};
            formData.forEach((value, key) => {
                
                paycheckData[key] = value;
            });
            
        fetch('/bff/api/add-paycheck/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken.toString(),
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'For-User-ID': userId,
                },
                mode:'cors',
                cache:'no-cache',
                body: JSON.stringify(paycheckData),
            })
        .then (response => {
            
            if (response.status === 201) {
                // Successful response
                alert('paycheck created');
                window.location.href = '/';
            } else if (response.status === 403) {
                alert('You forgot your credentials!');
            } else {
                alert('The paycheck is not created');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
        
        
        
})
