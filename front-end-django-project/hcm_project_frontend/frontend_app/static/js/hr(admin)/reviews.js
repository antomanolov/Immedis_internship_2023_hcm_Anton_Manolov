const token = localStorage.getItem('authToken');
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
const depBoxes = document.querySelector('.department-boxes')

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

fetch('/bff/api/reviews/',{
    method: 'GET',
    headers: {
        'X-CSRFToken': csrfToken.toString(),
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
    },
    mode: 'cors',
    cache: 'no-cache',
    
}) 
.then(response => response.json())
.then(data => {
    data.forEach(element => {
        
        const divBox = document.createElement('div');

        const divBoxTitle = document.createElement('div');
        const h3 = document.createElement('h3');
        const linkName = document.createElement('a');
        
        const points = document.createElement('p');
        const pointsStrong = document.createElement('strong');
        
        const feedback = document.createElement('p');
        const feedbackStrong = document.createElement('strong');
        
        const goals = document.createElement('p');
        const goalsStrong = document.createElement('strong');
        
        const improvements = document.createElement('p');
        const improvementsStrong = document.createElement('strong');

        const divEditDel = document.createElement('div');
        const linkDelete = document.createElement('a');
        
        divBox.className = 'box';
        divBoxTitle.className = 'box-title';
        divEditDel.className = 'edit-del-btns';
        linkDelete.className = 'delete'

        element.employee.forEach(el => {
            linkName.textContent = `ID: ${el.id} ${el.first_name} ${el.last_name}`
        })
        pointsStrong.textContent = 'Points: '
        
        feedbackStrong.textContent = 'Feedback: '
        goalsStrong.textContent = 'Goals: '
        improvementsStrong.textContent = `Improvements: `
        linkDelete.textContent = 'Delete'
        linkDelete.setAttribute('review-id', element.id)
        linkDelete.addEventListener("click", () => {
            confirmButton.setAttribute('review-id', linkDelete.getAttribute('review-id'))
            openModal()

        });
        depBoxes.append(divBox)
        divBoxTitle.appendChild(h3)
        h3.appendChild(linkName)
        points.appendChild(pointsStrong)
        feedback.appendChild(feedbackStrong)
        goals.appendChild(goalsStrong)
        improvements.appendChild(improvementsStrong)
        divEditDel.appendChild(linkDelete)
        points.innerHTML += `${element.points}/10`
        feedback.innerHTML += `${element.feedback}`
        goals.innerHTML += `${element.goals_achieved}`
        improvements.innerHTML += `${element.improvement_areas}`
        divBox.append(divBoxTitle)
        divBox.append(points)
        divBox.append(feedback)
        divBox.append(goals)
        divBox.append(improvements)
        divBox.append(divEditDel)
        


    });
})


// modal for comfirmation





// Attach click event to the cancel button
cancelButton.addEventListener("click", closeModal);

// Delete the user logic
confirmButton.addEventListener('click', function (event) {
    event.preventDefault();
    const reviewId = confirmButton.getAttribute('review-id')
    const token = localStorage.getItem('authToken');
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    
    
    fetch('/bff/api/delete-review/', {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken.toString(),
            'Content-Type': 'application/json',
            'Review-id': reviewId,
            'Authorization': `Token ${token}`,
        },
        mode: 'cors',
        cache: 'no-cache',
        
    })
    .then(response => {
        if (response.status == 200){
            alert('You\'ve deleted the review!')
            window.location.reload()
        }else {
            // Log or inspect the response content
            console.error(response.statusText);
            response.json().then(data => console.error(data));
        }
        
    })
   

})
