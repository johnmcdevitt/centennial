from django.test import TestCase
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

# project specific imports
from images.models import Image

# test methods
class ImageTest(TestCase):

    def test_image_create(self):
        image_file = SimpleUploadedFile("imgfile.jpeg", b"file_content", content_type="image/jpeg")
        image = Image.objects.create(image=image_file)
        self.assertTrue(isinstance(image, Image))
