const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '..', 'src', 'public')));

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'src', 'public', 'index.html'));
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString()
  });
});

app.post('/api/generate', (req, res) => {
  const { prompt } = req.body;
  
  if (!prompt) {
    return res.status(400).json({
      success: false,
      error: 'Prompt is required'
    });
  }

  // Enhanced AI response system with topic detection
  let response;
  const lowerPrompt = prompt.toLowerCase();
  
  if (lowerPrompt.includes('quantum') || lowerPrompt.includes('computing')) {
    response = `🔬 Quantum Computing Insight: "${prompt}" - Quantum computing leverages quantum mechanical phenomena like superposition and entanglement to process information. Unlike classical bits that are either 0 or 1, quantum bits (qubits) can exist in multiple states simultaneously, enabling exponentially faster calculations for specific problems like cryptography, optimization, and molecular simulation.`;
  } else if (lowerPrompt.includes('ai') || lowerPrompt.includes('artificial intelligence') || lowerPrompt.includes('machine learning')) {
    response = `🤖 AI/ML Analysis: "${prompt}" - Artificial Intelligence and Machine Learning are transforming industries through pattern recognition, predictive analytics, and automated decision-making. Modern AI systems use neural networks, deep learning architectures, and large language models to understand, process, and generate human-like responses across various domains.`;
  } else if (lowerPrompt.includes('code') || lowerPrompt.includes('programming') || lowerPrompt.includes('software')) {
    response = `💻 Programming Insight: "${prompt}" - Modern software development emphasizes clean code, scalable architectures, and efficient algorithms. Best practices include version control, automated testing, continuous integration, and following design patterns to create maintainable and robust applications.`;
  } else if (lowerPrompt.includes('business') || lowerPrompt.includes('startup') || lowerPrompt.includes('entrepreneur')) {
    response = `📈 Business Strategy: "${prompt}" - Successful businesses focus on customer value, market analysis, and innovative solutions. Key elements include identifying market needs, developing minimum viable products (MVPs), iterating based on feedback, and scaling operations efficiently while maintaining quality.`;
  } else if (lowerPrompt.includes('story') || lowerPrompt.includes('creative') || lowerPrompt.includes('write')) {
    response = `✨ Creative Response: "${prompt}" - In a world where technology and imagination converge, every idea has the potential to spark innovation. Your creative prompt opens doorways to endless possibilities, where artificial intelligence serves as a collaborative partner in bringing visions to life through the power of language and storytelling.`;
  } else {
    response = `🚀 GenAI Response: Your query "${prompt}" has been processed by our advanced AI system. This intelligent response demonstrates the capabilities of modern language models in understanding context, providing relevant information, and engaging in meaningful dialogue across diverse topics and domains.`;
  }
  
  res.json({
    success: true,
    result: response,
    timestamp: new Date().toISOString(),
    model: 'Nexnova-GenAI-v1.0'
  });
});

module.exports = app;