// // Elements
const sendButton = document.getElementById('sendButton');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');
const motivationAudio = document.getElementById('motivationAudio');

// Function to add a message to the chat
function addMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', sender);
    messageDiv.innerText = content;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;  // Scroll to the bottom
}

// Function to handle user's input
function handleUserInput() {
    const inputText = userInput.value.trim();

    if (inputText) {
        // Display user's message
        addMessage(inputText, 'user');

        console.log("Input when : " + inputText)

        // Clear the input field
        userInput.value = '';

        // Make a POST request to the /chat route with the user's input
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: inputText })
        })
        .then(response => response.json())
        .then(data => {
            // Display the chatbot's response
            console.log("hello");
            console.log(data.response);
            
            addMessage(data.response, 'bot');

            // Optionally, play the motivational audio if chatbot response requires it
            if (data.playMotivation) {
                motivationAudio.play();
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
}

// Event listener for the send button
sendButton.addEventListener('click', handleUserInput);

// Event listener for pressing "Enter" key to submit input
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        handleUserInput();
    }
});

