const userInfo = JSON.parse(localStorage.getItem('userInfo'))

if (!userInfo){
    window.location.href = '/'
}else
{
    const depSelect = document.querySelector('#department-select')
    const jobTitleSelect = document.querySelector('#job-title-select')
    
// prepopulate fields
    const firstName = document.querySelector('input[name="first_name"]');
    const lastName = document.querySelector('input[name="last_name"]');
    const telephone = document.querySelector('input[name="telephone_number"]');
    const userLocation = document.querySelector('input[name="location"]');
    const department = document.querySelector('select[name="department"]');
    const jobTitle = document.querySelector('select[name="job_title"]');
    const gender = document.querySelector('select[name="gender"]');
    const seniority = document.querySelector('select[name="seniority"]');
    
    
    firstName.value = userInfo.firs_name;
    lastName.value = userInfo.last_name;
    telephone.value = userInfo.telephone;
    userLocation.value = userInfo.location;
    department.value = userInfo.department
    jobTitle.value = userInfo.job_title
    gender.value = userInfo.gender
    seniority.value = userInfo.seniority

// start fetching first fetch for all departments/job titles
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

    // the PUT request and fetch for editing the employee
    document.getElementById('edit-form').addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this)
        const token = localStorage.getItem('authToken');
        const csrfToken = formData.get('csrfmiddlewaretoken')
        const editedData = {};
        formData.forEach((value, key) => {
            editedData[key] = value;
        })
        fetch('/bff/api/edit-user/', {
            method: 'PATCH',
            headers: {
                'X-CSRFToken': csrfToken.toString(),
                'Content-Type': 'application/json',
                'Employee-id': userInfo.id,
                'Authorization': `Token ${token}`,
            },
            mode: 'cors',
            cache: 'no-cache',
            body: JSON.stringify(editedData),
        })
        .then(response => {
            if (response.status == 200){
                alert('You\'ve made changes to this user successfuly')
                window.location.href = '/'
            }
            else{
                response.json()
            };
        })
        .then(data => console.log(data))
        .catch(error => {
            console.error('Error during login:', error);
        });

    })

}



