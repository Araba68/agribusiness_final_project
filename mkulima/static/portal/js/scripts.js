document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registration-form');

    form.addEventListener('submit', function(event) {
        let isValid = true;
        const inputs = form.querySelectorAll('input[required]');

        // Reset previous error messages
        clearAllErrors(inputs);

        // Validate required inputs
        inputs.forEach(input => {
            if (!input.value) {
                isValid = false;
                showError(input, `${input.name} is required`);
            }
        });

        // Check if passwords match
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirm-password');
        if (password.value !== confirmPassword.value) {
            isValid = false;
            showError(confirmPassword, "Passwords don't match");
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });

    function showError(input, message) {
        const error = document.createElement('span');
        error.classList.add('error');
        error.textContent = message;
        input.parentElement.appendChild(error);
    }

    function clearError(input) {
        const error = input.parentElement.querySelector('.error');
        if (error) {
            error.remove();
        }
    }

    function clearAllErrors(inputs) {
        inputs.forEach(input => {
            clearError(input);
        });
    }

    // Slideshow functionality
    let slideIndex = 1;
    showSlides(slideIndex);

    // Next/previous controls
    window.plusSlides = function(n) {
        showSlides(slideIndex += n);
    };

    // Thumbnail image controls
    window.currentSlide = function(n) {
        showSlides(slideIndex = n);
    };

    function showSlides(n) {
        const slides = document.getElementsByClassName("slide");
        const indicators = document.getElementsByClassName("indicators")[0].children;

        // Wrap around the slides
        if (n > slides.length) { slideIndex = 1; }
        if (n < 1) { slideIndex = slides.length; }

        // Hide all slides
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }

        // Remove "active" class from all indicators
        for (let i = 0; i < indicators.length; i++) {
            indicators[i].className = indicators[i].className.replace(" active", "");
        }

        // Display the current slide
        slides[slideIndex - 1].style.display = "block";  
        indicators[slideIndex - 1].className += " active";
    }

    // Event listeners for dots
    const dots = document.querySelectorAll('.indicators button');

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlides(index + 1); // Call showSlides with index + 1 (1-based)
        });
    });
});
