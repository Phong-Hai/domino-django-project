// Show green check when field is filled
document.querySelectorAll('.profile-form input, .profile-form select').forEach(el => {
    const updateCheck = () => {
        const group = el.closest('.form-group');
        if (el.value.trim()) {
            group.classList.add('valid');
        } else {
            group.classList.remove('valid');
        }
    };
    el.addEventListener('input', updateCheck);
    el.addEventListener('blur', updateCheck);
    updateCheck(); // initial state
});

// Avatar preview
document.getElementById('id_image')?.addEventListener('change', e => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = ev => document.getElementById('preview').src = ev.target.result;
        reader.readAsDataURL(file);
    }
});