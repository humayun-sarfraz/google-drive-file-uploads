# google-drive-file-uploads
 

# Google Drive File Upload Application

This application allows you to upload files to Google Drive using a simple drag-and-drop interface. The application is built with Kivy for the UI and uses the Google Drive API for file uploads.

## Prerequisites

Before you begin, you will need:

1. **Python**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **Google Cloud Project**: Set up a Google Cloud project and enable the Google Drive API.
3. **Service Account**: Create a service account and download the JSON key file.
4. **Kivy**: Install Kivy to create the application UI.
5. **Google API Client**: Install the Google API client library.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/google-drive-upload-app.git
    cd google-drive-upload-app
    ```

2. **Install the required packages**:
    ```sh
    pip install kivy google-api-python-client google-auth
    ```

3. **Add the service account key file**:
    - Place the downloaded `drive-json-file.json` in the project directory.

4. **Update the Google Drive folder ID**:
    - Replace `'your-google-drive-folder-id'` in the code with the actual ID of the Google Drive folder where you want to upload the files.

## Running the Application

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Using the application**:
    - A window will open with a message "Drag and Drop a file to upload".
    - Drag and drop a file into the window.
    - The application will display the upload progress and show a popup once the upload is complete.

## Code Explanation

Here is a brief explanation of the main components of the application:

- **Imports**: The necessary libraries are imported, including Kivy components and Google API clients.
- **Google Drive Setup**: The service account credentials are loaded and the Drive API client is initialized.
- **Kivy App Class**: The `FileUploadApp` class defines the main application window and handles file drops.
- **File Upload**: The `_on_file_drop` method triggers the upload process, which is handled by the `upload_file` and `upload_progress` methods.
- **UI Components**: Labels, progress bar, and popups are used to provide feedback to the user.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request on GitHub.

---

Feel free to customize this README file as per your requirements.
