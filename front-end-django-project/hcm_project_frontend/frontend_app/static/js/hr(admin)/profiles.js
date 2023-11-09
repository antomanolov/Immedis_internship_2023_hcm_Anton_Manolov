const aDep = document.querySelectorAll('a[data-user-id]')
const token = localStorage.getItem('authToken')
aDep.forEach(element => {
    element.addEventListener('click', function (e) {
        e.preventDefault();
        const userId = this.getAttribute('data-user-id');
        fetch('/bff/api/get-user', {
            method: 'GET',
            headers: {
                'Search-User-ID': `${userId}`,
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            cache: 'no-cache'
        })
            .then(response => {
                if (response.status == 200){
                    return response.json()
                }
            })
            .then(userInfo => {
                localStorage.setItem('userInfo', JSON.stringify(userInfo))
                window.location.href = '/profile/'
               
            })
    })
});


    const searchInput = document.getElementById('searchInput');
    const departments = document.querySelectorAll('.profile-dep');
    const profiles = document.querySelectorAll('.profile');
    

    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase();

        // Initially hide all departments and profiles
        
        profiles.forEach(profile => profile.style.display = 'none');

        

        profiles.forEach(profile => {
            const profileText = profile.textContent.toLowerCase();
            const containsSearchTerm = profileText.includes(searchTerm);

            profile.style.display = containsSearchTerm ? 'flex' : 'none';
        });
    });
