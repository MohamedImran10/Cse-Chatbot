function sendMessage() {
    let inputField = document.getElementById("user-input");
    let message = inputField.value;
    let chatBox = document.getElementById("chat-box");

    if (message.trim() === "") return;

    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
    inputField.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
    });
}
