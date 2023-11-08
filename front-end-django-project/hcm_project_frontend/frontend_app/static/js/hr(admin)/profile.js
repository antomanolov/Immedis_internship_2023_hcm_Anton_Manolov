const userInfo = JSON.parse(localStorage.getItem('userInfo'))
const titleSeniority = document.querySelector('.title-seniority')
const locationP = document.querySelector('.location-p')
const firstNameP = document.querySelector('.first-name-p')
const lastNameP = document.querySelector('.last-name-p')
const emailP = document.querySelector('.email-p')
const telephoneP = document.querySelector('.telephone-p')
const dateOfBirthP = document.querySelector('.date-of-birth-p')
const genderP = document.querySelector('.gender-p')
const depP = document.querySelector('.dep-p')
const jobTitleP = document.querySelector('.job-title-p')
const locationP2 = document.querySelector('.location-p2')
const seniorityP = document.querySelector('.seniority-p2')
const dateOfHire = document.querySelector('.date-of-hire-p')
const telephoneP2 = document.querySelector('.telephone-p2')



if (userInfo){
    firstNameP.textContent += userInfo.firs_name
    lastNameP.textContent += userInfo.last_name
    titleSeniority.textContent = `${userInfo.seniority} ${userInfo.job_title}`
    locationP.textContent += `${userInfo.location}, Bulgaria`
    emailP.textContent += userInfo.email
    telephoneP.textContent += userInfo.telephone
    telephoneP2.textContent += userInfo.telephone
    dateOfBirthP.textContent += userInfo.birthdate
    genderP.textContent += userInfo.gender
    depP.textContent += userInfo.department
    jobTitleP.textContent += userInfo.job_title
    locationP2.textContent += userInfo.location
    seniorityP.textContent += userInfo.seniority
    dateOfHire.textContent += userInfo.hire_date

}else {
    window.location.href = '/'
}


// modal for comfirmation

const modal = document.querySelector(".modal-m");
const cancelButton = document.getElementById("cancelButton");
const confirmButton = document.getElementById("confirmButton");

// Show the modal
function openModal() {
    modal.style.display = "block";
}

// Hide the modal
function closeModal() {
    modal.style.display = "none";
}

// Attach click event to delete button (or any element that triggers delete action)
const deleteButton = document.querySelector('.delete-btn');
deleteButton.addEventListener("click", openModal);

// Attach click event to the cancel button
cancelButton.addEventListener("click", closeModal);

// Delete the user logic
confirmButton.addEventListener('click', function (event) {
    event.preventDefault();
    
    const token = localStorage.getItem('authToken');
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    
    
    fetch('/bff/api/delete-user/', {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken.toString(),
            'Content-Type': 'application/json',
            'Employee-id': userInfo.id,
            'Authorization': `Token ${token}`,
        },
        mode: 'cors',
        cache: 'no-cache',
        
    })
    .then(response => {
        if (response.status == 200){
            alert('You\'ve deleted the user!')
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
