import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Set up the credentials and the Drive API client
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'drive-json-file.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

class FileUploadApp(App):
    def build(self):
        self.title = "Google Drive Uploader"
        layout = FloatLayout()

        self.label = Label(text="Drag and Drop a file to upload", font_size='20sp', size_hint=(1, 0.1), pos_hint={'top': 1})
        layout.add_widget(self.label)

        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1), pos_hint={'top': 0.2})
        layout.add_widget(self.progress_bar)

        Window.bind(on_drop_file=self._on_file_drop)

        return layout

    def _on_file_drop(self, window, file_path, x, y):
        self.upload_file(file_path.decode('utf-8'))

    def upload_file(self, file_path):
        if file_path:
            try:
                file_metadata = {'name': os.path.basename(file_path), 'parents': ['your-google-drive-folder-id']}
                media = MediaFileUpload(file_path, mimetype='application/octet-stream', resumable=True)
                request = drive_service.files().create(body=file_metadata, media_body=media, fields='id')

                # Upload the file with progress updates
                self.upload_progress(request, media, file_path)
            except HttpError as error:
                print(f"An error occurred: {error}")
                popup = Popup(title='Upload Failed',
                              content=Label(text=f'An error occurred: {error}'),
                              size_hint=(0.8, 0.8))
                popup.open()
        else:
            popup = Popup(title='No file selected',
                          content=Label(text='Please select a file to upload.'),
                          size_hint=(0.8, 0.8))
            popup.open()

    def upload_progress(self, request, media, file_path):
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                self.progress_bar.value = progress
                print(f'Upload Progress: {progress}%')
        
        print(f'Upload Complete: File ID: {response.get("id")}')
        popup = Popup(title='Upload Successful',
                      content=Label(text=f'File ID: {response.get("id")}'),
                      size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    # Set the window size
    Window.size = (600, 400)
    FileUploadApp().run()
