import streamlit as st
import datetime
import time
import random

# Page configuration
st.set_page_config(
    page_title="Nexnova GenAI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        color: #718096;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #68d391;
        margin-right: 8px;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
    }
    
    .response-box {
        background: #f0fff4;
        border: 2px solid #68d391;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .api-status {
        background: #e6fffa;
        border: 2px solid #81e6d9;
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'api_status' not in st.session_state:
    st.session_state.api_status = "✅ Online"

# Header
st.markdown('<h1 class="main-header">🤖 Nexnova GenAI Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle"><span class="status-indicator"></span>Powered by Advanced AI Technology</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📡 API Status")
    st.markdown(f"""
    <div class="api-status">
        <h4>System Information</h4>
        <ul>
            <li><strong>Server:</strong> {st.session_state.api_status}</li>
            <li><strong>Model:</strong> Nexnova-GenAI-v1.0</li>
            <li><strong>Version:</strong> 1.0.0</li>
            <li><strong>Status:</strong> Ready for Queries</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("💡 Sample Prompts")
    sample_prompts = [
        "Explain quantum computing in simple terms",
        "Write a creative story about AI",
        "How does machine learning work?",
        "What are the best programming practices?",
        "Tell me about startup business strategies"
    ]
    
    for prompt in sample_prompts:
        if st.button(f"💫 {prompt}", key=f"sample_{hash(prompt)}"):
            st.session_state.current_prompt = prompt

# Enhanced AI response function
def generate_ai_response(prompt):
    """Generate intelligent AI responses based on topic detection"""
    
    # Simulate processing time
    time.sleep(random.uniform(1, 2))
    
    lower_prompt = prompt.lower()
    
    if any(word in lower_prompt for word in ['quantum', 'computing', 'qubit']):
        return f"""🔬 **Quantum Computing Insight:**

"{prompt}"

Quantum computing leverages quantum mechanical phenomena like **superposition** and **entanglement** to process information. Unlike classical bits that are either 0 or 1, quantum bits (qubits) can exist in multiple states simultaneously, enabling exponentially faster calculations for specific problems like:

• **Cryptography** - Breaking current encryption methods
• **Optimization** - Solving complex logistical problems  
• **Molecular Simulation** - Drug discovery and materials science
• **Machine Learning** - Quantum algorithms for AI

The technology is still emerging, but companies like IBM, Google, and others are making significant progress toward practical quantum advantage."""

    elif any(word in lower_prompt for word in ['ai', 'artificial intelligence', 'machine learning', 'neural network']):
        return f"""🤖 **AI/ML Analysis:**

"{prompt}"

Artificial Intelligence and Machine Learning are transforming industries through:

• **Pattern Recognition** - Identifying complex data patterns
• **Predictive Analytics** - Forecasting trends and behaviors
• **Natural Language Processing** - Understanding and generating human language
• **Computer Vision** - Image and video analysis
• **Automated Decision Making** - Smart systems that adapt and learn

Modern AI systems use neural networks, deep learning architectures, and large language models to understand, process, and generate human-like responses across various domains. The field continues to evolve rapidly with breakthroughs in transformer models, reinforcement learning, and multimodal AI."""

    elif any(word in lower_prompt for word in ['code', 'programming', 'software', 'development']):
        return f"""💻 **Programming Insight:**

"{prompt}"

Modern software development emphasizes several key principles:

• **Clean Code** - Readable, maintainable, and well-documented
• **Scalable Architectures** - Systems that grow with demand
• **Version Control** - Git workflows for collaboration
• **Automated Testing** - Unit, integration, and end-to-end tests
• **Continuous Integration/Deployment** - Automated build and release pipelines
• **Design Patterns** - Proven solutions to common problems

Best practices include following SOLID principles, writing comprehensive tests, using meaningful variable names, and keeping functions small and focused. Modern development also emphasizes DevOps practices, cloud deployment, and microservices architectures."""

    elif any(word in lower_prompt for word in ['business', 'startup', 'entrepreneur', 'strategy']):
        return f"""📈 **Business Strategy:**

"{prompt}"

Successful businesses focus on creating value through:

• **Customer-Centric Approach** - Understanding and solving real problems
• **Market Analysis** - Identifying opportunities and competition
• **Minimum Viable Product (MVP)** - Testing ideas quickly and cheaply
• **Iterative Development** - Learning from feedback and adapting
• **Scalable Operations** - Building systems that grow efficiently
• **Strong Team Building** - Attracting and retaining talent

Key startup principles include validating assumptions early, focusing on product-market fit, managing cash flow carefully, and building strong customer relationships. Modern businesses also leverage data analytics, digital marketing, and technology automation to gain competitive advantages."""

    elif any(word in lower_prompt for word in ['story', 'creative', 'write', 'imagination']):
        return f"""✨ **Creative Response:**

"{prompt}"

*In a world where technology and imagination converge...*

Your creative prompt opens doorways to endless possibilities, where artificial intelligence serves as a collaborative partner in bringing visions to life. Every story begins with a spark of curiosity, much like the one you've ignited here.

Imagine a future where AI and humans work together to:
• **Craft compelling narratives** that resonate with diverse audiences
• **Generate innovative ideas** that push creative boundaries  
• **Explore new storytelling mediums** through interactive experiences
• **Bridge cultures and perspectives** through shared stories
• **Inspire the next generation** of creators and innovators

The power of creative expression lies not just in the final product, but in the journey of discovery, the questions asked, and the boundaries pushed. Your imagination, combined with AI capabilities, creates infinite possibilities for storytelling and creative expression."""

    else:
        return f"""🚀 **GenAI Response:**

"{prompt}"

Your query has been processed by our advanced AI system. This intelligent response demonstrates the capabilities of modern language models in:

• **Context Understanding** - Analyzing the meaning and intent behind your question
• **Knowledge Synthesis** - Drawing from vast information sources
• **Relevant Information Retrieval** - Providing targeted, useful responses
• **Natural Language Generation** - Creating human-like, engaging dialogue
• **Multi-domain Expertise** - Covering diverse topics and fields

The Nexnova GenAI system is designed to assist with various tasks including creative writing, technical explanations, problem-solving, and educational content. Each response is tailored to provide maximum value while maintaining accuracy and relevance to your specific inquiry."""

# Main chat interface
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.subheader("💬 Chat with Nexnova GenAI")
    
    # Text input
    if 'current_prompt' in st.session_state:
        prompt = st.text_area(
            "Enter your AI prompt:",
            value=st.session_state.current_prompt,
            height=100,
            placeholder="Try: 'Explain quantum computing in simple terms' or 'Write a creative story about AI'..."
        )
        del st.session_state.current_prompt
    else:
        prompt = st.text_area(
            "Enter your AI prompt:",
            height=100,
            placeholder="Try: 'Explain quantum computing in simple terms' or 'Write a creative story about AI'..."
        )
    
    # Generate button
    if st.button("🚀 Generate AI Response", type="primary"):
        if prompt.strip():
            with st.spinner("🤖 Nexnova AI is thinking..."):
                response = generate_ai_response(prompt)
                
                # Add to chat history
                st.session_state.chat_history.append({
                    'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
                    'prompt': prompt,
                    'response': response
                })
                
                # Display response
                st.markdown('<div class="response-box">', unsafe_allow_html=True)
                st.markdown("### 🤖 AI Response:")
                st.markdown(response)
                st.markdown(f"*Generated at {datetime.datetime.now().strftime('%H:%M:%S')} by Nexnova-GenAI-v1.0*")
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a prompt first!")

# Chat history
if st.session_state.chat_history:
    st.subheader("📝 Chat History")
    
    for i, chat in enumerate(reversed(st.session_state.chat_history[-5:])):  # Show last 5
        with st.expander(f"💬 {chat['timestamp']} - {chat['prompt'][:50]}..."):
            st.markdown("**Your Question:**")
            st.write(chat['prompt'])
            st.markdown("**AI Response:**")
            st.markdown(chat['response'])

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🌟 Nexnova GenAI**")
    st.markdown("Advanced AI Technology")

with col2:
    st.markdown("**🔗 Links**")
    st.markdown("[GitHub Repository](https://github.com/jeevansridharan/Nexnova-Genai)")

with col3:
    st.markdown("**📊 Stats**")
    st.markdown(f"Queries Processed: {len(st.session_state.chat_history)}")

# Clear chat history button
if st.session_state.chat_history:
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.experimental_rerun()