## Preparing Your Python Code with FastAPI

Before uploading your FastAPI application, ensure it's properly prepared. Here’s how you can do this, following our platform's requirements.

Here is an example [Python Sample](https://github.com/aleph-im/aleph-vm/tree/main/examples/example_fastapi)

### Selecting Your Language

Ensure your project is developed in Python.

### Packaging Your Project

For a FastAPI application, follow these steps to package your project:

```bash
my_project/
│
├── main.py  # Your main FastAPI application file.
│
├── requirements.txt  # Lists all the dependencies for your project.
│
└── additional_files/  # Optional: Any additional files or directories.
    ├── models.py  # Optional: Defines data models.
    └── dependencies.py  # Optional: Contains any dependency functions.
```

1. **Main File**: Your main FastAPI file (e.g., `main.py`) should be at the root of your package. This file contains your application instance and routes.
2. **Dependencies**: Include a `requirements.txt` file that lists FastAPI and any other dependencies. Your `requirements.txt` might look something like this:
   ```
   fastapi==0.68.0
   uvicorn==0.15.0
   ```
3. **Compression**: Compress your project directory into a `.zip` or `.squashfs` file. Make sure the compression includes the `main.py` file and `requirements.txt`.

### Defining the Entry Point

For FastAPI projects, the entry point is crucial for our platform to know how to start your application. If your main file is `main.py`:

- **Entry Point**: Your entry point would be `main:app`, where `main` is the filename (without `.py`) and `app` is the FastAPI application instance.

## Example Code Explanation

Here is the explanation of your code snippet:

```python
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
  return {"message": "Hello World"}
```

- **FastAPI Instance**: `app = FastAPI()` creates an instance of a FastAPI application.
- **Route Definition**: `@app.get("/")` defines a route that listens for GET requests at the root URL (`/`). 
- **Async Function**: `async def root():` is an asynchronous function that handles requests to the root URL. It returns a JSON response with a message.
- **JSON Response**: `{"message": "Hello World"}` is the JSON response that clients will receive when they access the root URL.

## Uploading Your Code

After preparing your code, follow the platform's upload process:

1. **Navigate to Code Upload**: Go to the code upload section by creating a new function on our platform.
2. **Choose File**: Select your `.zip` or `.squashfs` file containing the FastAPI project.
3. **Select Language**: Choose Python as the language.
4. **Specify Entry Point**: Enter `main:app` as the entry point.
5. **Upload**: Complete the upload process.

By following these steps and ensuring your FastAPI application is correctly prepared, you'll facilitate a seamless integration.