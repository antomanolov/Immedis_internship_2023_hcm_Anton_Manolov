const depSelect = document.querySelector('#department-select')
const jobTitleSelect = document.querySelector('#job-title-select')

function validateForm() {
    const password = document.querySelector('[name="password"]').value
    const password2 = document.querySelector('[name="password2"]').value
    const telephone = document.querySelector('[name="telephone_number"]').value
    let alertModal = []

   if (password != password2 || password === '' || password2 === '') {
        alertModal.push('Passwords must be the same !')
        
    }

    if(password.length < 8){
        alertModal.push('Password must be at least 9 characters')
    }

    if(!/(?=.*[A-Z])(?=.*[a-z])/.test(password)){
        alertModal.push('Password must have at least one uppercase and one lowercase char')
    }

    
    if(!/\d/.test(password)){
        alertModal.push('Password must have at least one digit')
    }
    
    if(!/[!@#$%^&*]/.test(password)){
        alertModal.push('Password must have at least one special character (e.g., @, #, $, %, etc.)')
    }
    
    if(alertModal.length == 0){
        return true
    }

    const alerts = alertModal.join('\n')
    alert(alerts)
    return false
}   


fetch('/bff/api/departments/')
    .then(response => response.json())
    .then(data => {
        data.forEach(dep => {
            const option = document.createElement('option')
            option.value = dep.id
            option.textContent = dep.name
            depSelect.appendChild(option)
        });
        
    })
    .catch(error => {
        console.error('Error fetching departments:', error);
    });

fetch('/bff/api/job-titles/')
    .then(response => response.json())
    .then(data => {
        data.forEach(title => {
            const option = document.createElement('option')
            option.value = title.id
            option.textContent = title.title
            jobTitleSelect.appendChild(option)
        })
    })

document.getElementById('registration-form').addEventListener('submit', function (event) {
    event.preventDefault();
        if(validateForm()) {
            const formData = new FormData(this);
            const csrfToken = formData.get('csrfmiddlewaretoken');
            const userData = {};
            formData.forEach((value, key) => {
                if (key != 'password2'){
                    userData[key] = value;
                }
           
            });
        fetch('/bff/api/add-user/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken.toString(),
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            })
        .then (response => console.log(response.json()))
        }
        
        
})