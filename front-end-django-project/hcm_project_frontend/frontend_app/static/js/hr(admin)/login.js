document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    // Make a fetch request to the BFF for user authentication
    fetch('/bff/api/login/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken.toString(),
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({'email': email, 'password': password}),
        
    })
    
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            
            

           console.log('Login successful')
            
        } else {
            // Handle login failure
            console.error('Login failed.');
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
});

