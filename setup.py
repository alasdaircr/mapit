from setuptools import setup, find_packages
from functools import reduce
import os
import sys

file_dir = os.path.abspath(os.path.dirname(__file__))


static_dir = os.path.join(file_dir, 'mapit', 'static', 'mapit')
sass_dir = os.path.join(static_dir, 'sass')
sass_mtime = reduce(max, (os.stat(os.path.join(root, f)).st_mtime
                    for root, dirs, files in os.walk(sass_dir)
                    for f in files))
css_file = os.path.join(static_dir, 'css', 'mapit.css')
try:
    css_mtime = os.stat(css_file).st_mtime
except OSError:
    css_mtime = 0

packaging = False
for arg in sys.argv:
    if arg == 'sdist' or 'bdist' in arg:
        packaging = True
        break

if css_mtime < sass_mtime and packaging:
    raise Exception("Make sure the CSS is up-to-date and compiled before packaging.")


def read_file(filename):
    filepath = os.path.join(file_dir, filename)
    return open(filepath).read()


setup(
    name='django-mapit',
    version='1.3.1.post1',
    description=(
        'A web service for mapping postcodes and points to current or past '
        'administrative area information and polygons.'),
    long_description=read_file('README.rst'),
    author='mySociety',
    author_email='mapit@mysociety.org',
    url='https://github.com/mysociety/mapit',
    license='LICENSE.txt',
    packages=find_packages(exclude=['project']),
    scripts=['bin/mapit_make_css'],
    include_package_data=True,
    install_requires=[
        'Django >= 1.4.18',
        'South == 1.0.2',
        'psycopg2',
        'PyYAML',
        'Shapely',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
    ],

    zip_safe=False,  # So that easy_install doesn't make an egg
)
