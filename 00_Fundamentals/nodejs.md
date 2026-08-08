# Node.js Instruction manual

## What is Node.js
Node.js is a powerful, open-source, cross-platform JavaScript runtime environment that allows developers to run JavaScript code outside of a web browser. It is built on the V8 JavaScript engine and is designed for building scalable network applications. Node.js uses an event-driven, non-blocking I/O model, making it efficient and suitable for real-time applications.

## Step1: Download and Install Node.js
1. Visit the official Node.js website: [https://nodejs.org/](https://nodejs.org/)
2. Download the LTS (Long Term Support) version suitable for your operating system (Windows, macOS, or Linux).

## Step 2: Installation Key Steps Explanation
1. Welcome interface: Click "Next".
2. License Agreement: Check "I accept...", then click "Next".
3. Destination Folder: Choose the installation path or leave it as default, then click "Next".
4. Custom Setup: Select the components you want to install (default is recommended), then click "Next".
5. Tools for Native Modules: Do not check this option (unless you need to compile C++ modules). Otherwise, it will automatically download several gigabytes of VS Build Tools and Python for you, which will be very slow. Just click Next.
6. Installation: Click "Install", wait for the progress bar to complete, and then click "Finish".

## Step 3: Verify the installation
1. Open a terminal or command prompt, then type the following command to check the installed Node.js version:
```bash
node -v
```
2. To check the installed npm (Node Package Manager) version, type the following command:
```bash
npm -v
```

## Step 4: Environment Configuration (Core Steps)
This step is the most important! We need to move the globally installed packages and cache files of npm to the directory we just created, so as to facilitate management.

1. Create a directory for global npm packages and cache files. For example, you can create a directory named `.npm-global` in your home directory:
```bash
mkdir ~/.npm-global
mkdir ~/.npm-cache
```
2. Configure npm to use the new directory for global packages and cache files (please replace the actual paths with your own):
```bash
npm config set prefix '~/.npm-global'
npm config set cache '~/.npm-cache'
```
3. Configure environment variables, if this is not configured, any tools you install globally using npm install -g (such as vue, claude-code) will subsequently prompt "Command not found". 
   - For Windows:
     1. Open the Start menu and search for "Environment Variables".
     2. Click on "Edit the system environment variables".
     3. In the System Properties window, click on the "Environment Variables" button.
     4. Under "System variables", find and select the "Path" variable, then click "Edit".
     5. Click "New" and add the path to your global npm packages directory (e.g., `C:\Users\YourUsername\.npm-global\bin`).
     6. Click "OK" to save the changes.
   - For macOS/Linux:
     1. Open a terminal and edit your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`) using a text editor.
     2. Add the following line at the end of the file:
        ```bash
        export PATH="$HOME/.npm-global/bin:$PATH"
        ```
     3. Save the file and run `source ~/.bashrc` (or the appropriate file) to apply the changes.

## Step 5: Configure the domestic image source (for speed improvement)
```bash
npm config set registry https://registry.npmmirror.com
npm config get registry
```
If you return to `https://registry.npmmirror.com/`, it indicates that the speed increase has been successful!

## Step 6: Modify folder permissions
1. Open File Explorer and locate your installation directory: D:\software.
2. Right-click on the nodejs folder and select "Properties" (Properties).
3. Click on the "Security" (Security) tab at the top.
4. Click on the "Edit" (Edit) button in the middle.
5. In the "Groups or Users" list, select Users (which is the normal user group).
6. In the "Users' Permissions" section below, check the "Allow" box next to "Full Control".
7. Click "OK" and then "OK".

## Step 7: Final Test
In order to ensure that all configurations are perfect, we attempted to install a commonly used global module (such as `express` or `vue`).
1. Open a terminal or command prompt and run the following command to install a global package (e.g., `express`):
```bash
npm install -g express
```
2. After the installation is completed, go to your `D:\Environment\nodejs\node_global\node_modules` directory and check if you see the express folder. If you do, it means that all the configurations have been successfully completed! 🎉


