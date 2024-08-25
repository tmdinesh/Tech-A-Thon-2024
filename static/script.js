document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-button");
    const userInput = document.getElementById("user-input");
    const messages = document.getElementById("messages");
    const activityButton = document.getElementById("activity-button");
    const recordButton = document.getElementById("record-button");

    let isRecording = false;
    let mediaRecorder;
    let audioChunks = [];

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    activityButton.addEventListener("click", requestActivity);
    recordButton.addEventListener("click", toggleRecording);

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            appendMessage("user", message);
            fetch(`/get?msg=${encodeURIComponent(message)}`)
                .then(response => response.json())
                .then(data => {
                    appendMessage("bot", data.response);
                })
                .catch(error => {
                    console.error('Error:', error);
                    appendMessage("bot", "I'm sorry, but I encountered an error. Please try again.");
                });
            userInput.value = "";
        }
    }

    function requestActivity() {
        fetch('/activity')
            .then(response => response.json())
            .then(data => {
                appendMessage("bot", data.response);
            })
            .catch(error => {
                console.error('Error:', error);
                appendMessage("bot", "I'm sorry, but I couldn't fetch an activity right now. Please try again.");
            });
    }

    function toggleRecording() {
        if (!isRecording) {
            startRecording();
        } else {
            stopRecording();
        }
    }

    function startRecording() {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();

                audioChunks = [];
                mediaRecorder.addEventListener("dataavailable", event => {
                    audioChunks.push(event.data);
                });

                mediaRecorder.addEventListener("stop", sendAudioToServer);

                recordButton.textContent = "Stop Recording";
                isRecording = true;
            })
            .catch(error => {
                console.error('Error accessing microphone:', error);
                appendMessage("bot", "I'm sorry, but I couldn't access your microphone. Please check your browser settings and try again.");
            });
    }

    function stopRecording() {
        if (mediaRecorder && mediaRecorder.state !== "inactive") {
            mediaRecorder.stop();
            recordButton.textContent = "Start Recording";
            isRecording = false;
        }
    }

    function sendAudioToServer() {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        const formData = new FormData();
        formData.append("audio", audioBlob, "recording.webm");

        fetch('/voice', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                appendMessage("bot", `Error: ${data.error}`);
            } else {
                appendMessage("user", `You said: ${data.transcription}`);
                appendMessage("bot", data.response);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage("bot", "I'm sorry, but I encountered an error processing your audio. Please try again or type your message.");
        });
    }

    function appendMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add(`${sender}-message`);
        messageElement.textContent = message;
        messages.appendChild(messageElement);
        messages.scrollTop = messages.scrollHeight;
    }
});