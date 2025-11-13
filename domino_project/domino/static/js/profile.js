// profile.js: preview image & basic front-end validation
document.addEventListener('DOMContentLoaded', function () {
const imgInput = document.querySelector('input[type=file]');
if (imgInput) {
imgInput.addEventListener('change', function (ev) {
const file = ev.target.files[0];
if (!file) return;
if (!file.type.startsWith('image/')) return;
const reader = new FileReader();
reader.onload = () => {
const preview = document.getElementById('preview');
if (preview) preview.src = reader.result;
};
reader.readAsDataURL(file);
});
}


// Simple client-side email check before submit
const profileForm = document.getElementById('profile-form');
if (profileForm) {
profileForm.addEventListener('submit', function (e) {
const email = document.querySelector('input[name="email"]').value;
if (!email || !email.includes('@')) {
e.preventDefault();
alert('Please enter a valid email address.');
}
});
}
});