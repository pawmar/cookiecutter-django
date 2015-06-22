# -*- coding: utf-8 -*-
"""Basic functional tests."""

from django_webtest import WebTest


class BasicSiteTest(WebTest):

    """Test basic stuff about the website."""

    def test_brand_and_page_title(self):
        """Test if brand and page title contain project name string."""
        project_name = '{{cookiecutter.project_name}}'
        response = self.app.get('/', auto_follow=True)
        brand = response.html.find(class_='navbar-brand').string
        self.assertEqual(project_name, brand)
        title = response.html.find('title').string
        self.assertEqual(project_name, title)
