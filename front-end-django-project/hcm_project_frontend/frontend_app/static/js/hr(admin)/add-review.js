const token = localStorage.getItem('authToken')
const userId = JSON.parse(localStorage.getItem('userInfo')).id


document.getElementById('review-form').addEventListener('submit', function (event) {
    event.preventDefault();
        
            const formData = new FormData(this);
            const csrfToken = formData.get('csrfmiddlewaretoken');
            const reviewData = {};
            formData.forEach((value, key) => {
                
                reviewData[key] = value;
            });
            
        fetch('/bff/api/add-review/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken.toString(),
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'For-User-ID': userId,
                },
                mode:'cors',
                cache:'no-cache',
                body: JSON.stringify(reviewData),
            })
        .then (response => {
            
            if (response.status === 201) {
                // Successful response
                alert('Review created');
                window.location.href = '/';
            } else if (response.status === 403) {
                alert('You forgot your credentials!');
            } else {
                alert('The review is not created');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
        
        
        
})
