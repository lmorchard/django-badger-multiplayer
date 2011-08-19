import logging

from django.conf import settings

from django.http import HttpRequest
from django.test.client import Client

from commons import LocalizingClient

from pyquery import PyQuery as pq

from nose.tools import assert_equal, with_setup, assert_false, eq_, ok_
from nose.plugins.attrib import attr

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

try:
    from commons.urlresolvers import reverse
except ImportError, e:
    from django.core.urlresolvers import reverse

from . import BadgerTestCase

from badger.models import (Award, Progress,
        BadgeAwardNotAllowedException)

from badger_multiplayer.models import (Badge, Nomination,
        NominationApproveNotAllowedException,
        NominationAcceptNotAllowedException)


class BadgerViewsTest(BadgerTestCase):

    def setUp(self):
        self.testuser = self._get_user()
        self.client = LocalizingClient()

    def tearDown(self):
        Nomination.objects.all().delete()
        Award.objects.all().delete()
        Badge.objects.all().delete()

    def test_create(self):
        """Can create badge with form"""
        # Login should be required
        r = self.client.get(reverse('badger_multiplayer.views.create'))
        eq_(302, r.status_code)
        ok_('/accounts/login' in r['Location'])

        # Should be fine after login
        self.client.login(username="tester", password="trustno1")
        r = self.client.get(reverse('badger_multiplayer.views.create'))
        eq_(200, r.status_code)

        # Make a chick check for expected form elements
        doc = pq(r.content)

        form = doc('form#create_badge')
        eq_(1, form.length)

        eq_(1, form.find('input[name=title]').length)
        eq_(1, form.find('textarea[name=description]').length)
        # For styling purposes, we'll allow either an input or button element
        eq_(1, form.find('input.submit,button.submit').length)

        r = self.client.post(reverse('badger_multiplayer.views.create'), dict(
        ), follow=True)
        doc = pq(r.content)
        eq_(1, doc.find('form .error > input[name=title]').length)

        badge_title = "Test badge #1"
        badge_desc = "This is a test badge"

        r = self.client.post(reverse('badger_multiplayer.views.create'), dict(
            title=badge_title,
            description=badge_desc,
        ), follow=True)
        doc = pq(r.content)

        eq_('badge_detail', doc.find('body').attr('id'))
        eq_(badge_title, doc.find('.badge .title').text())
        eq_(badge_desc, doc.find('.badge .description').text())

        slug = doc.find('.badge').attr('data-slug')

        badge = Badge.objects.get(slug=slug)
        eq_(badge_title, badge.title)
        eq_(badge_desc, badge.description)

    def test_edit(self):
        """Can edit badge detail"""
        user = self._get_user()
        badge = Badge(creator=user, title="Test II",
                      description="Another test")
        badge.save()

        self.client.login(username="tester", password="trustno1")

        r = self.client.get(reverse('badger.views.detail',
            args=(badge.slug,)), follow=True)
        doc = pq(r.content)

        eq_('badge_detail', doc.find('body').attr('id'))
        edit_url = doc.find('a.edit_badge').attr('href')
        ok_(edit_url is not None)

        r = self.client.get(edit_url)
        doc = pq(r.content)
        eq_('badge_edit', doc.find('body').attr('id'))

        badge_title = "Edited title"
        badge_desc = "Edited description"

        r = self.client.post(edit_url, dict(
            title=badge_title,
            description=badge_desc,
        ), follow=True)
        doc = pq(r.content)

        eq_('badge_detail', doc.find('body').attr('id'))
        eq_(badge_title, doc.find('.badge .title').text())
        eq_(badge_desc, doc.find('.badge .description').text())

        slug = doc.find('.badge').attr('data-slug')

        badge = Badge.objects.get(slug=slug)
        eq_(badge_title, badge.title)
        eq_(badge_desc, badge.description)

    def _get_user(self, username="tester", email="tester@example.com",
            password="trustno1"):
        (user, created) = User.objects.get_or_create(username=username,
                defaults=dict(email=email))
        if created:
            user.set_password(password)
            user.save()
        return user
