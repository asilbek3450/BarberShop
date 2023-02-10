import qrcode
from django.core.files.base import ContentFile


def make_qr_code(instance, data=None):
    original_file_path = 'media/sample.png'
    qr = qrcode.make(data)
    qr.save(original_file_path)
    fh = open(original_file_path, "rb")
    if fh:
        file_content = ContentFile(fh.read())
        instance.qr_code.save(original_file_path, file_content)
        instance.save()
    fh.close()
