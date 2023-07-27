# server.py
import os
import sys
import subprocess
import logging
import time  # Import the time module
import importlib.util

logging.basicConfig(level=logging.INFO)

def get_module_from_file_path(file_path: str):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def start_server(filename):
    p = None  # Declare p outside the try block to ensure access in the finally block
    try:
        # Get the directory containing the file and add it to the Python path
        file_directory = os.path.dirname(filename)
        sys.path.append(file_directory)

        my_env = os.environ.copy()
        my_env['FILE_PATH'] = filename
        logging.info(my_env['FILE_PATH'])
        p = subprocess.Popen(['uvicorn', 'textbase.backend:app', '--reload', '--host', '0.0.0.0', '--port', '8080'], env=my_env)

        # Import the module containing the decorated function
        module_name = os.path.basename(filename)[:-3] if filename.endswith('.py') else os.path.basename(filename)
        module = importlib.import_module(module_name)

        if hasattr(module, 'on_message'):
            print("Chatbot is running. Visit http://localhost:4000/ in your web browser to interact.")
            p.wait()
        else:
            print("Error: 'on_message' function not found in the file.")

    except Exception as e:
        # Log the exception or print a custom error message
        print(f"Error occurred: {e}")
        sys.exit(1)

    finally:
        # Ensure subprocess is terminated when the script exits
        if p:
            p.terminate()  # Try terminating the process first
            time.sleep(1)  # Add a short delay before killing the process
            p.kill()  # Kill the process if it did not terminate gracefully

if __name__ == '__main__':
    try:
        # Use test method to start the server
        chatbot_module_path = 'main.py'  # Replace with the actual path to your chatbot module
        start_server(chatbot_module_path)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Keyboard interrupt received. Terminating the server...")
        sys.exit(1)
