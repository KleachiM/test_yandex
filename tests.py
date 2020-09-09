import unittest
from main import YaUploader, token


class MyTestCase ( unittest.TestCase ):
    def setUp(self):
        self.upl = YaUploader(token)

    def test_create_folder(self):
        self.assertEqual(self.upl.create_folder('test'), 201)

    def test_folder_found(self):
        self.assertEqual(self.upl.folder_info('test'), 'Folder found')

    def test_folder_not_found(self):
        self.assertEqual(self.upl.folder_info('Зasdf'), None)

if __name__ == '__main__':
    unittest.main ()
