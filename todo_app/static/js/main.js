document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('animate-fade-in');
        }, index * 100);
    });

    // Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('a[href*="delete"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Auto-save form data to localStorage
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        // Load saved data
        inputs.forEach(input => {
            const savedValue = localStorage.getItem(input.name);
            if (savedValue && input.type !== 'password') {
                input.value = savedValue;
            }
        });
        
        // Save data on input
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                if (input.type !== 'password') {
                    localStorage.setItem(input.name, input.value);
                }
            });
        });
        
        // Clear saved data on submit
        form.addEventListener('submit', function() {
            inputs.forEach(input => {
                localStorage.removeItem(input.name);
            });
        });
    });

    // Add toggle functionality for task completion
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const listItem = this.closest('li');
            if (this.checked) {
                listItem.classList.add('completed-task');
            } else {
                listItem.classList.remove('completed-task');
            }
        });
    });
});
