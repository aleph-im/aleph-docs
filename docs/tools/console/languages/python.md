## Preparing Your Python Code with FastAPI

Before deploying your FastAPI application, it's essential to prepare it according to the platform's guidelines.

Here is an example [Python Sample](https://github.com/aleph-im/aleph-vm/tree/main/examples/example_fastapi)

### Selecting Your Language

Confirm the project is developed in Python.

### Packaging Your Project

To package a FastAPI application, organize your project as follows:

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

1. **Main File**: Place the main FastAPI file (main.py), containing the application instance and routes, at the package's root.
2. **Dependencies**: List FastAPI and other dependencies in `requirements.txt`. Example content:
   ```
   fastapi==0.68.0
   uvicorn==0.15.0
   ```
3. **Compression**: Compress your project directory into a `.zip` or `.squashfs` file, ensuring it includes `main.py` and `requirements.txt`.

### Defining the Entry Point

The entry point is vital for the platform to recognize how to launch your FastAPI application. For a main file named `main.py`:

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

1. **Navigate to Code Upload**: Access the code upload section by initiating a new function on the platform.
2. **Choose File**: Select your `.zip` or `.squashfs` file containing the FastAPI project.
3. **Select Language**: Choose Python as the language.
4. **Specify Entry Point**: Enter `main:app` as the entry point.
5. **Upload**: Complete the upload process.

By following these steps and ensuring your FastAPI application is correctly prepared, you'll facilitate a seamless integration.