// Function to send message to the server and handle response
// Function to send message to the server and handle response
async function sendMessage() {
    var input = document.getElementById('input').value.trim(); // Trim input
    if (input === '') return; // Return if input is empty

    appendMessage('user', input); // Append user message to chat window

    try {
        // Send POST request to server with input
        const response = await axios.post('/ask', { input: input });
        var output = response.data.response; // Extract response from data
        appendMessage('bot', output); // Append bot response to chat window
    } catch (error) {
        console.log(error); // Log any errors
    }

    document.getElementById('input').value = ''; // Clear input field
}


// Function to append message to the chat window
function appendMessage(sender, message) {
    var chatWindow = document.getElementById('output'); // Get chat window element
    var div = document.createElement('div'); // Create a new div element
    div.classList.add(sender); // Add sender class to div
    div.textContent = message; // Set text content of div to message
    chatWindow.appendChild(div); // Append div to chat window
}
