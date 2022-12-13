from django.test import TestCase
from django.template.defaultfilters import slugify


# class ModelsTestCase(TestCase):
#     def test_post_has_slug(self):
#         """Posts are given slugs correctly when saving"""
#         post = Post.objects.create(title="My first post")

#         post.author = "John Doe"
#         post.save()
#         self.assertEqual(post.slug, slugify(post.title))
