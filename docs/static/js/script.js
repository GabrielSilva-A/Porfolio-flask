// Form validation
(function () {
    'use strict'
    
    var forms = document.querySelectorAll('.needs-validation')
    
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                
                form.classList.add('was-validated')
            }, false)
        })
})()

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault()
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        })
    })
})

// Animation on scroll
function animateOnScroll() {
    const elements = document.querySelectorAll('.skill-item, .card')
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top
        const elementVisible = 150
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.style.opacity = "1"
            element.style.transform = "translateY(0)"
        }
    })
}

// Set initial state for animation
document.querySelectorAll('.skill-item, .card').forEach(element => {
    element.style.opacity = "0"
    element.style.transform = "translateY(20px)"
    element.style.transition = "opacity 0.6s ease, transform 0.6s ease"
})

window.addEventListener('scroll', animateOnScroll)
animateOnScroll() // Initial check