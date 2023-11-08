// TODO MAKE THE TOKEN AUTH NOT TO BE SAVED IN THE LOCAL STORAGE IF I HAVE MORE TIME!!!
// try document.cookie!
if (localStorage.getItem('authToken')) {
    window.location.href = '/'
}

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    // Make a fetch request to the BFF for user authentication
    
    fetch('/bff/api/login/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({'email': email, 'password': password}),
        
    })
    
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            
            localStorage.setItem('authToken', data.token);

            window.location.href = '/';
            
        } else {
            // Handle login failure
            console.error('Login failed.');
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
});

