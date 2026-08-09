# OpenClaw Installation Instructions
## What is OpenClaw
OpenClaw is a powerful and flexible software framework designed for building and deploying web applications. It provides a robust set of tools and libraries that simplify the development process, allowing developers to focus on creating high-quality applications.

- **Local Execution**  Data is stored on your device and does not need to be uploaded to the cloud. Complete control over privacy and data security

- **Real Execution**  Not only is it a conversation, but it can actually operate your computer. Automated handling of tasks such as emails, calendars, and file management

- **Multi-platform Messaging**  Supports WhatsApp, Telegram, Discord, Slack, etc. 10+ platforms. Manage all communications from a single entry point

- **Persistent Memory**  Saves context and user preferences across sessions. Becomes increasingly familiar with you over time, continuously improving efficiency

- **Open Source Free**  Completely open source. Just bring your own API Key. Free, fully autonomous control

## Step 1: Download the Node.js
1. Go to the official Node.js website: [https://nodejs.org/](https://nodejs.org/)
2. Download the LTS (Long Term Support) version suitable for your operating system (Windows, macOS, or Linux).
3. Follow the installation instructions provided on the website to install Node.js on your system.

## Step 2: Install OpenClaw
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to install OpenClaw.
3. Run the following command to clone the OpenClaw repository:
   ```bash
   # Global install OpenClaw
   npm install -g openclaw

   # Check the version of OpenClaw to verify the installation
   openclaw --version
   ```

## Step 3: Configure OpenClaw
After installation, you need to configure OpenClaw to work with your preferred settings.
```bash
# Openclaw configuration command
openclaw onboard
```
The guide will assist you in completing the following steps:
1. Select the AI model provider (Anthropic Claude / OpenAI GPT / local model)
2. Enter the API key
3. Choose the messaging platform (Telegram / Discord / WhatsApp, etc.)
4. Configure system permissions (it is recommended to select the sandbox mode first)

## Step 4: Start OpenClaw
1. After configuration, you can start OpenClaw by running the following command in your terminal:
   ```bash
   # Start OpenClaw
   openclaw
   # You can also launch Dashboard
   openclaw dashboard
   ```

## Step 5: Understand the core concepts
### Gateway
The gateway is the core component of OpenClaw that manages communication between the user and the AI model. It handles incoming messages, processes them, and sends responses back to the user.

### Skills
Skills are modular components that extend the functionality of OpenClaw. They can be thought of as plugins that allow the AI to perform specific tasks, such as sending emails, managing calendars, or interacting with third-party services.
1. Each Skill defines a specific set of tasks.
2. Third-party Skills can be installed from Clawhub.
3. Custom Skills can also be developed by oneself.

### Memory
The memory component of OpenClaw allows the AI to retain context and user preferences across sessions. This enables the AI to provide more personalized and efficient responses over time.
OpenClaw will remember:
1. Your preferences and habits
2. The previous conversation context
3. Important information and tasks

## Step 6: Explore Clawhub
Clawhub is a repository of third-party Skills that can be easily integrated into OpenClaw. It provides a wide range of functionalities that can enhance the capabilities of your AI assistant.
1. To explore Clawhub, visit the official Clawhub website: [https://clawhub.com/](https://clawhub.com/). Or use the command:
   ```bash
   # Search Skills
   openclaw skills search email
   # View Skill Info
   openclaw skills info @author/skill-name
   ```
2. Install common Skills, such as Email Manager, Calendar Manager, File Organizer, and Tavily Search, using the following commands:
   ```bash
   # Install Email Manager Skill
   openclaw skills install @openclaw/email-manager 
   # Install Calendar Manager Skill
   openclaw skills install @openclaw/calendar
   # Install File Organizer Skill
   openclaw skills install @openclaw/file-organizer
   # Install Tavily Search Skill
   openclaw skills install @openclaw/tavily-search