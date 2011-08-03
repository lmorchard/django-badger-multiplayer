=========================
django-badger-multiplayer
=========================

Badger is a family of Django apps intended to help introduce badges into your
project, to track and award achievements by your users. This can be used to
help encourage certain behaviors, recognize skills, or just generally
celebrate members of your community.

For more about the thinking behind this project, check out this essay:
`Why does Mozilla need a Badger?  <http://decafbad.com/2010/07/badger-article/>`_

The ``django-badger-multiplayer`` package is intended as an add-on to
``django-badger``. It offers (or plans to offer) the following:

- Views and enhanced models that enable users to create their own badges and
  nominate each other for awards.


Installation
------------

- TBD, see `badger2 <https://github.com/lmorchard/badger2>`_ for an example
  site setup
- ``pip install git://github.com/lmorchard/django-badger-multiplayer.git#egg=django-badger-multiplayer``


Settings
--------

- TBD, see `badger2 <https://github.com/lmorchard/badger2>`_ for an example
  site setup


Other Badger apps
-----------------

Here are other apps in the Badger family, either in progress or proposed:

`django-badger <https://github.com/lmorchard/django-badger>`_
    The core Badger app. Offers facilities to create Badges, issue Awards,
    and track Progress.

`django-badger-api <https://github.com/lmorchard/django-badger-api>`_
    Augments ``django-badger`` with a REST API and OAuth so external scripts
    and bots can issue awards and nominations in response to events monitored
    in custom ways. Also, opens the way for things like mobile apps, etc.

`django-badger-federation <https://github.com/lmorchard/django-badger-federation>`_
    Builds on ``django-badger-api`` and Activity Streams with facilities to
    make badging a distributed feature. Your network of sites can be badge
    issuers and badge collection hubs, and you can allow sites outside your
    network to participate.

.. vim:set tw=78 ai fo+=n fo-=l ft=rst:
