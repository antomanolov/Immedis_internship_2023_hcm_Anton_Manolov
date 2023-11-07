const wellcomeSign = document.querySelector('.wellcome')
const logoutBtns = document.querySelectorAll('.logout-btn')
const addEmployeeBtn = document.querySelector('.add-employee')
const homeBtn = document.querySelector('.home-btn')

homeBtn.addEventListener('click', ()=>{
    window.location.href = '/'
})
addEmployeeBtn.addEventListener('click', () =>{
    window.location.href = '/register/'
})

logoutBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        const token = localStorage.getItem('authToken');
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        fetch('/bff/api/logout/', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                    mode: 'cors',
                    cache: 'no-cache'
            
        })
        
        .then(response => {
            if (response.status == 200) {
                
                localStorage.removeItem('authToken');
                window.location.href = '/login';
                alert('Logged out')
                
            } else {
                // Handle login failure
                console.error('No token AnoNymoyus');
            }
        })
        
        .catch(error => {
            console.error('Error during login:', error);
        });
    });
    
    const token = localStorage.getItem('authToken');
    fetch('/bff/api/current-user', {
        method: 'GET',
        headers: {
            'Authorization': `Token ${token}`,
        },
        // for the headers to work 
        // properly when you add new header must put mode and cache!
        mode: 'cors',
        cache: 'no-cache',
    })
        .then(response => {
            
            if (response.status === 200) {
                
                return response.json();
            } else if (response.status === 403) {
                
                window.location.href = '/login'; 
            } else {
                
                console.error('An error occurred. Redirecting to login page.');
                window.location.href = '/login'; 
            }
        })
        .then(data => {
            
            wellcomeSign.textContent = `Wellcome, ${data['name']}`
        })
    
    
})

