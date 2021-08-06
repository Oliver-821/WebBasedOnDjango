from django.test import TestCase
from rango.models import Category, Page
from django.urls import reverse


# Create your tests here.
def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes

    category.save()
    return category

def add_page(category, title, url):
    return Page.objects.get_or_create(category=category, title=title, url=url)[0]

class CategoryTests(TestCase):
    def test_ensure_views_are_positive(self):


        category = Category(name='CategoryTest', views=100, likes=200)
        category.save()
        self.assertEqual((category.views >= 0), True)
        print("test1 finished")


class PageTests(TestCase):
    def testPage(self):
        category = add_category('vue', 100, 100)
        page = add_page(category, 'LLL', 'https://vuejs.bootcss.com/examples/')

        self.assertTrue(page.category.views >= 0, True)
        print("test02 finished")

class IndexTests(TestCase):
    
    
    def testIndexAndView(self):
      
      
        add_category('vue', 100, 100)
        add_category('C#', 200, 300)
        add_category('Nodejs', 300, 400)
        add_category('AuglarJS', 300, 400)


        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'vue')
        self.assertContains(response, 'C#')
        self.assertContains(response, 'Nodejs')
        self.assertContains(response, 'AuglarJS')


        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 4)