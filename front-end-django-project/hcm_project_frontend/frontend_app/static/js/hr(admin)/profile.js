const userInfo = JSON.parse(localStorage.getItem('userInfo'))
const titleSeniority = document.querySelector('.title-seniority')
const locationP = document.querySelector('.location-p')
const firstNameP = document.querySelector('.first-name-p')
const lastNameP = document.querySelector('.last-name-p')
const emailP = document.querySelector('.email-p')
const telephoneP = document.querySelector('.telephone-p')
const dateOfBirthP = document.querySelector('.date-of-birth-p')
const genderP = document.querySelector('.gender-p')


if (userInfo){
    //#TODO make the get-user-by-id view in the backend to return user departments
    // and job titles not like ints but like strings !   
}