const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav__link');

navToggle.addEventListener('click', () => {
    document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', ()=> {
        document.body.classList.remove('nav-open')
    })
})

// Error handling mail form 
const name = document.getElementById('name')
const email = document.getElementById('email')
const subject = document.getElementById('subject')
const message = document.getElementById('message')
const errorElement = document.getElementById('error')


FormData.addEventListener('submit', (e) => {
    let messages = []
    if (name.value === '' || name.value == null){
        messages.push('Name is required')
        errorElement.innerText = messeges.join(', ')
    }

    if (messages.length > 0)
    {
        e.preventDefault()

    }

})