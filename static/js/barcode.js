document.addEventListener("DOMContentLoaded", () => {
    const startCameraButton = document.getElementById("startCamera");
    const cameraStreamContainer = document.getElementById("cameraStreamContainer");
    const resultContainer = document.getElementById("resultContainer");
    const inputField = document.getElementById("inputField");
    let cameraStream;
    let barcodeFound = false;

    startCameraButton.addEventListener("click", async() => {
        cameraStream = await navigator.mediaDevices.getUserMedia({ video: true });
        const cameraStreamElement = document.getElementById("cameraStream");
        cameraStreamElement.srcObject = cameraStream;
        cameraStreamContainer.style.display = "block";
        startBarcodeDetection();
    });

    function startBarcodeDetection() {
        const intervalId = setInterval(async() => {
            if (barcodeFound) {
                clearInterval(intervalId);
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStreamContainer.style.display = "none";
                return;
            }

            const mediaStreamTrack = cameraStream.getVideoTracks()[0];
            const imageCapture = new ImageCapture(mediaStreamTrack);

            const capturedImage = await imageCapture.takePhoto();
            const imageData = new FormData();
            imageData.append("image", capturedImage);

            const response = await fetch("/extract_barcode", {
                method: "POST",
                body: imageData
            });

            const result = await response.text();
           
            inputField.value = result;
            if (result !== "No barcode found.") {
                barcodeFound = true;
            }
        }, 1000);
    }
});