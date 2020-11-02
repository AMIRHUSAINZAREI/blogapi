from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUp(self):
        testuser1 = User.objects.create(username='testuser', password='123asd')
        testuser1.save()
        testpost1 = Post.objects.create(author=testuser1, title='sample title', body='sample body')
        testpost1.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = post.title
        body = post.body
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'sample title')
        self.assertEqual(body, 'sample body')
