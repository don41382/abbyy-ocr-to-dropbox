# Runs ABBYY OCR recognition and uploads a searchable pdf to dropbox 

This is simple script to run ocr detection of a given set of files (jpg, png) and run ABBYY's OCR detection. 

## Usage

Install all required dependencies

` # pip install -r requirements.txt `  

Export all required auth key to the environment

```
export abbyy_app_id=...
export abbyy_app_secret=...
export dropbox_token=...
```

Run the script

``` # python ocr-to-dropbox.py document1.jpg document2.jpg --output /folder-dropbox/output.pdf  ```

