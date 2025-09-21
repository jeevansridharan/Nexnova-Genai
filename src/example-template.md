# Example: AI-Powered Code Assistant

## Quick Start Template
This is a sample implementation of a GenAI prototype. Customize it for your specific use case.

### Basic Structure
```javascript
// app.js - Main application entry point
const express = require('express');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// AI Integration (example with OpenAI)
const openai = require('openai');
const client = new openai.OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// API Endpoints
app.post('/api/generate', async (req, res) => {
  try {
    const { prompt } = req.body;
    
    const completion = await client.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: prompt
        }
      ],
      max_tokens: 500,
    });
    
    res.json({
      success: true,
      result: completion.choices[0].message.content
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Frontend Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>GenAI Prototype</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { background: #f5f5f5; padding: 20px; border-radius: 8px; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #007cba; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background: white; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GenAI Prototype</h1>
        <textarea id="prompt" placeholder="Enter your prompt here..." rows="4"></textarea>
        <button onclick="generateResponse()">Generate</button>
        <div id="result" class="result" style="display: none;"></div>
    </div>

    <script>
        async function generateResponse() {
            const prompt = document.getElementById('prompt').value;
            const resultDiv = document.getElementById('result');
            
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = 'Generating...';
            
            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt })
                });
                
                const data = await response.json();
                resultDiv.innerHTML = data.success ? data.result : 'Error: ' + data.error;
            } catch (error) {
                resultDiv.innerHTML = 'Error: ' + error.message;
            }
        }
    </script>
</body>
</html>
```

## Usage Instructions

1. **Backend Integration**: Use the JavaScript code above for your Express server
2. **Frontend Integration**: Use the HTML code for your user interface
3. **API Configuration**: Add your OpenAI API key to the `.env` file
4. **Testing**: Test the endpoints with the provided frontend interface

This template provides a complete foundation for building AI-powered applications for hackathons.
