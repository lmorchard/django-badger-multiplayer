from setuptools import setup


setup(
    name='django-badger-multiplayer',
    version='0.0.1',
    description='Django app for playing badges with friends',
    long_description=open('README.md').read(),
    author='Leslie Michael Orchard',
    author_email='me@lmorchard.com',
    url='http://github.com/lmorchard/django-badger-multiplayer',
    license='BSD',
    packages=['badger_multiplayer'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        # I don't know what exactly this means, but why not?
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
