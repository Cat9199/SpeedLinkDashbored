function selectForm() {
    const formSelect = document.getElementById("form-select");
    const form1 = document.getElementById("form1");
    const form2 = document.getElementById("form2");

    if (formSelect.value === "form1") {
        form1.style.display = "block";
        form2.style.display = "none";
    } else if (formSelect.value === "form2") {
        form1.style.display = "none";
        form2.style.display = "block";
    }
}

function showWithdrawPopup() {
    const popup = document.getElementById("popup");
    popup.style.display = "flex";
}

function closeWithdrawPopup() {
    const popup = document.getElementById("popup");
    popup.style.display = "none";
}


// -----------------------
const fileInput = document.getElementById('fileInput');
const uploadContainer = document.querySelector('.upload-container');

uploadContainer.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadContainer.classList.add('highlight');
});

uploadContainer.addEventListener('dragleave', () => {
    uploadContainer.classList.remove('highlight');
});

uploadContainer.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadContainer.classList.remove('highlight');
    const files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener('change', (e) => {
    const files = e.target.files;
    handleFiles(files);
});

function handleFiles(files) {
    for (const file of files) {
        console.log(file.name);
    }
}