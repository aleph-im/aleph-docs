## Preparing Your Node.js Code

Before uploading a Node.js application, ensure it meets the platform's requirements for a seamless deployment process.

Here is an example [NodeJs Sample](https://github.com/aleph-im/aleph-vm/tree/main/examples/example_http_js)

### Selecting Your Language

Ensure the project is developed in Node.js.

To ready a Node.js application for deployment, follow these outlined steps:

### Create the `run.sh` Script

Craft a shell script named run.sh to set the working directory and initiate the Node.js server:

   ```bash
   #!/bin/sh

   set -euf

   cd /opt/code
   node /opt/code/server.js
   ```

   This script positions the application in the correct directory for server file execution.

### Packaging Your Project

Consider this structure for a Node.js project packaging:

```plaintext
my_nodejs_project/
│
├── index.js  # Your main application file.
│
├── run.sh
│
├── package.json  # Lists your project dependencies and scripts.
│
├── package-lock.json  # Generated after running npm install, ensures consistent installs.
│
└── node_modules/  # Contains all your npm dependencies, can be omitted if using package.json correctly.
```

1. **Main File**: The main Node.js file, like `index.js`, should be easily accessible at the package's root.
2. **run.sh**: Acts as the project's entry point.
2. **Dependencies**: The `package.json` at the project's root must list necessary dependencies. After setting up `package.jso`n, execute `npm install` to create a node_modules directory and a package-lock.json. 
3. **Compression**: Compress your project directory into a `.zip` or `.squashfs` file.

### Defining the Entry Point

For Node.js projects, the entry point is specified in the `package.json` file under the `main` field. It typically points to the main application file (e.g., `index.js`).

## Example Code

Given an `index.js:

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send({ message: 'Hello World' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

- **Express Application**: This snippet creates an instance of an Express app.
- **Route Definition**: Defines a route that listens for GET requests at the root URL (`/`). It sends a JSON response with a message.
- **Server Listening**: The application listens on a specified port, defaulting to 3000 if not specified by the environment.

## Uploading Your Code

For Node.js application upload to the platform:

1. **Navigate to Code Upload**: Access the code upload section by creating a new function.
2. **Choose File**: Select your packaged `.zip` or `.squashfs` file.
3. **Select Language**: Choose Node.js as the language.
4. **Specify Entry Point**: Ensure your `package.json` has the correct entry point defined.
5. **Upload**: Submit your package for processing.
