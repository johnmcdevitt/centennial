from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.six import BytesIO
import PIL.Image

# TODO create temporary media_root for testing

from images.models import Image

def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = BytesIO()
    PIL.Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class ImagesViewTest(TestCase):

    @classmethod
    def setUp(self):
        self.client = Client()

    @classmethod
    def tearDown(self):
        # TODO create and remove temporary files
        pass

    def test_image_create_view(self):
        # get URL
        get_response = self.client.get(reverse('create-image'))
        self.assertEqual(get_response.status_code, 200)

        # create image for upload
        test_image = create_image(None, 'test_image.png')
        test_image_file = SimpleUploadedFile('test_image.png', test_image.getvalue())
        form_data = {'image':test_image_file, 'image_type':'a'}

        # post and test successfully redirected
        response = self.client.post(reverse('create-image'), form_data, follow=True)
        self.assertRedirects(response,reverse('images'),status_code=302,target_status_code=200)
