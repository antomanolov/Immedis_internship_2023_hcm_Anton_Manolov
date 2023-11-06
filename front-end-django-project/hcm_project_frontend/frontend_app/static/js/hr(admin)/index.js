const depBoxes = document.querySelector('.department-boxes')
const token = localStorage.getItem('authToken');
console.log(token)
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
    .then(response => console.log(response))


fetch('/bff/api/departments/')
    .then(response => response.json())
    .then(data => {
        data.forEach(dep => {
            const divBox = document.createElement('div')
            const divBoxTitle = document.createElement('div')
            const h2 = document.createElement('h2')
            const h4 = document.createElement('h4')
            const ulDep = document.createElement('ul')
            
            divBox.className = 'box'
            divBoxTitle.className = 'box-title'
            ulDep.className = 'dep-col'

            h2.textContent = `${dep['name']}`
            h4.textContent = 'employees'
            divBoxTitle.appendChild(h2)
            divBoxTitle.appendChild(h4)
            divBox.appendChild(divBoxTitle)
            divBox.appendChild(ulDep)
            depBoxes.appendChild(divBox)

            dep['employees'].forEach(
                emp => {
                    
                    const liDep = document.createElement('li')
                    const onlineDiv = document.createElement('div')
                    const nameDiv = document.createElement('div')
                    const aDep = document.createElement('a')

                    liDep.className = 'li-dep'
                    onlineDiv.classList.add('online-status', 'online')
                    
                    aDep.textContent = `${emp.first_name} ${emp.last_name}`
                    aDep.href = '#'
                    
                    nameDiv.appendChild(aDep)
                    liDep.appendChild(onlineDiv)
                    liDep.appendChild(nameDiv)
                    
                    ulDep.appendChild(liDep)
                }
            )
        });
    })