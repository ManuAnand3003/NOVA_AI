// Helper to POST JSON and get response
async function postJSON(url, data) {
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return res.json();
}

const chatHistory = document.getElementById('chatHistory');
const circularLoader = document.getElementById('circularLoader');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const calcBtn = document.getElementById('calcBtn');
const sentimentBtn = document.getElementById('sentimentBtn');
const visionBtn = document.getElementById('visionBtn');
const generateBtn = document.getElementById('generateBtn');
const imageGenBtn = document.getElementById('imageGenBtn');
imageGenBtn.onclick = async () => {
    const promptText = prompt('Enter prompt for image generation:');
    if (!promptText) return;
    chatHistory.textContent = 'Generating image...';
    const res = await postJSON('/api/image-generate', { prompt: promptText });
    if (res.image_url) {
        chatHistory.innerHTML = `<img src="${res.image_url}" alt="Generated Image" style="max-width:100%;border-radius:12px;box-shadow:0 2px 8px #4285F433;" />`;
    } else {
        chatHistory.textContent = res.error || 'No image generated.';
    }
};

sendBtn.onclick = async () => {
    const message = userInput.value.trim();
    if (!message) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${message}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/chat', { message });
    circularLoader.style.display = 'none';
    if (res.result) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>AI:</b> ${res.result}</div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No response.'}</div>`;
    }
};

calcBtn.onclick = async () => {
    const expression = prompt('Enter calculation:');
    if (!expression) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${expression}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/calculate', { expression });
    circularLoader.style.display = 'none';
    if (res.result) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>Result:</b> ${res.result}</div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No result.'}</div>`;
    }
};

sentimentBtn.onclick = async () => {
    const text = prompt('Enter text for sentiment analysis:');
    if (!text) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${text}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/sentiment', { text });
    circularLoader.style.display = 'none';
    if (res.result) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>Sentiment:</b> ${res.result}</div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No result.'}</div>`;
    }
};

visionBtn.onclick = async () => {
    const image_url = prompt('Enter image URL for analysis:');
    if (!image_url) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${image_url}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/vision', { image_url });
    circularLoader.style.display = 'none';
    if (res.result) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>Analysis:</b> ${res.result}</div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No result.'}</div>`;
    }
};

generateBtn.onclick = async () => {
    const promptText = prompt('Enter prompt for text generation:');
    if (!promptText) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${promptText}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/generate', { prompt: promptText });
    circularLoader.style.display = 'none';
    if (res.result) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>Generated:</b> ${res.result}</div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No result.'}</div>`;
    }
};
imageGenBtn.onclick = async () => {
    const promptText = prompt('Enter prompt for image generation:');
    if (!promptText) return;
    chatHistory.innerHTML = `<div class='user-msg'><b>You:</b> ${promptText}</div>`;
    circularLoader.style.display = 'block';
    const res = await postJSON('/api/image-generate', { prompt: promptText });
    circularLoader.style.display = 'none';
    if (res.image_url) {
        chatHistory.innerHTML += `<div class='ai-msg'><b>Generated Image:</b><br><img src="${res.image_url}" alt="Generated Image" style="max-width:100%;border-radius:12px;box-shadow:0 2px 8px #4285F433;" /><div class='caption'>Prompt: ${promptText}</div></div>`;
    } else {
        chatHistory.innerHTML += `<div class='ai-msg error'>${res.error || 'No image generated.'}</div>`;
    }
};

// Optional: Enter key triggers send
userInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') sendBtn.onclick();
});
