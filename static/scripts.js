document.getElementById('chatForm').onsubmit = function(event) {
    event.preventDefault();

    var userInput = document.getElementById('userInput').value;
    var chatBox = document.getElementById('chat');

    // Append user message to chat
    var userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.textContent = 'You: ' + userInput;
    chatBox.appendChild(userMessage);

    // Make a POST request to get_response
    fetch('/get_response', {
        method: 'POST',
        body: new URLSearchParams('user_input=' + encodeURIComponent(userInput)),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Append GPT response to chat
        var gptResponse = document.createElement('div');
        gptResponse.className = 'message gpt';
        gptResponse.textContent = 'OleGPT: ' + data.response;
        chatBox.appendChild(gptResponse);
    });

    // Clear the input field
    document.getElementById('userInput').value = '';
};
