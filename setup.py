from distutils.core import setup
import clortho

long_description = open('README.md').read()

setup(
    name='django-clortho',
    version=clortho.VERSION,
    packages=['clortho'],
    description='A Django authentication backend for Facebook via Open Graph.',
    author='Chad Paulson',
    license='BSD License',
    url='http://github.com/chadpaulson/django-clortho',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)