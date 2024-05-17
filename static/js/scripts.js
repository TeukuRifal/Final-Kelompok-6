document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById('imagePreview');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
            document.getElementById('uploadForm').classList.remove('show-input'); // Hide input after upload
        }
        reader.readAsDataURL(file);
    }
});

document.getElementById('clearButton').addEventListener('click', function() {
    const imagePreview = document.getElementById('imagePreview');
    imagePreview.src = '';
    imagePreview.style.display = 'none';
    document.getElementById('uploadForm').reset();
    document.getElementById('uploadForm').classList.add('show-input'); // Show input when cleared
});
