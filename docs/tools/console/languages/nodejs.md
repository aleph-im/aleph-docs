## Preparing Your Node.js Code

Before uploading your Node.js application, make sure it's properly set up according to our platform's requirements.

Here is an example [NodeJs Sample](https://github.com/aleph-im/aleph-vm/tree/main/examples/example_http_js)

### Selecting Your Language

Confirm that your project is developed in Node.js.

To prepare your Node.js application for deployment on the specified platform, follow these steps:

### Create the `run.sh` Script

Create a shell script named `run.sh` with the following content, which sets the working directory to `/opt/code` and starts the Node.js server:

   ```bash
   #!/bin/sh

   set -euf

   cd /opt/code
   node /opt/code/server.js
   ```

   This script ensures that your application starts within the correct directory and executes the Node.js server file.

### Packaging Your Project

Here’s a sample structure for a Node.js project ready for packaging:

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

1. **Main File**: Place your main Node.js file, such as `index.js`, at the root of your package. This file is the entry point to your application.
2. **Dependencies**: Include a `package.json` file in your project root. This file should list all dependencies needed for your project. After defining your `package.json`, run `npm install` to generate a `node_modules` directory and a `package-lock.json` file. However, for uploading, it's often recommended to exclude the `node_modules` folder and ensure your platform installs dependencies from `package.json`.
3. **Compression**: Compress your project directory into a `.zip` or `.sqsh` file. Include the `index.js`, `package.json`, and `package-lock.json`. Omitting the `node_modules` directory can significantly reduce the size of your upload package.

### Defining the Entry Point

For Node.js projects, the entry point is specified in the `package.json` file under the `main` field. It typically points to your main application file (e.g., `index.js`).

## Example Code

Assuming your `index.js` file looks like this:

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

To upload your Node.js application to our platform, follow these steps:

1. **Navigate to Code Upload**: Access the code upload section by creating a new function.
2. **Choose File**: Select your packaged `.zip` or `.sqsh` file.
3. **Select Language**: Choose Node.js as the language.
4. **Specify Entry Point**: Ensure your `package.json` has the correct entry point defined.
5. **Upload**: Submit your package for processing.

Adhering to these guidelines will ensure that your Node.js application integrates smoothly with our platform.