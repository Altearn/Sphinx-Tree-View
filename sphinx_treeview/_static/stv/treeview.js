document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.stv .collapse-trigger').forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.stopPropagation();
            const listItem = this.closest('li');
            listItem.classList.toggle('collapsed');
        });
    });
}); 