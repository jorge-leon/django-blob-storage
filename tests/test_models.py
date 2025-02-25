from django.test.testcases import TestCase

from dbstorage.models import DBFile


class DBFileTests(TestCase):
    databases = {"default", "test"}

    def test_db_file_save(self):
        content = b"Hello World!"
        name = "my-files/hello-world.txt"

        db_file = DBFile.objects.create(content=content, name=name)

        self.assertEqual(db_file.content, content)
        self.assertEqual(db_file.name, name)
        self.assertTrue(db_file.created_on)
        self.assertTrue(db_file.updated_on)
        self.assertTrue(db_file.accessed_on)
        self.assertEqual(str(db_file), name)
