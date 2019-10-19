from ABBYY import CloudOCR
from io import BytesIO
import os
import dropbox
import argparse

parser = argparse.ArgumentParser(description="runs ocr on the given files and uploads it to dropbox")
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
parser.add_argument('--output', required=True)
args = parser.parse_args()

dropbox = dropbox.Dropbox(os.environ['dropbox_token'])
ocr = CloudOCR(application_id=os.environ['abbyy_app_id'], password=os.environ['abbyy_app_secret'])

def ocrImages(files, exportFormat="pdfSearchable"):
        task = None
	for file in files:
		if task is None:
			task = ocr.submitImage(file={file.name: file})
		else:
			task = ocr.submitImage(file={file.name: file}, taskId=task['id'])

	task = ocr.processDocument(taskId=task['id'], exportFormat=exportFormat)
	result = ocr.wait_for_task(task)
        print("%s credits were used." % result['credits'])
        download = ocr.session.get(result['resultUrl'])

        return download

def dropboxUpload(download):
	dropbox.files_upload(BytesIO(download.content).read(),args.output)

download = ocrImages(files=args.file,exportFormat="pdfSearchable")
dropboxUpload(download)
