const depBoxes = document.querySelector('.department-boxes')


fetch('/api/core/departments/')
    .then(response => response.json())
    .then(data => {
        data.forEach(dep => {
            const divBox = document.createElement('div')
            const divBoxTitle = document.createElement('div')
            const h2 = document.createElement('h2')
            const h4 = document.createElement('h4')
            divBox.className = 'box'
            divBoxTitle.className = 'box-title'
            h2.textContent = `${dep['name']}`
            h4.textContent = 'employees'
            divBoxTitle.appendChild(h2)
            divBoxTitle.appendChild(h4)
            divBox.appendChild(divBoxTitle)
            depBoxes.appendChild(divBox)
        });
    })