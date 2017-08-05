"""
Flask-Mptt
-------------

Flask extension to make mptt easier to use
"""
from setuptools import setup


setup(
    name='Flask-Mptt',
    version='1.0',
    url='http://abdullahsolutions.com/flask-mptt/',
    license='BSD',
    author='Abdullah Zainul Abidin',
    author_email='abdullah.zainul@gmail.com',
    description='Flask extension for mptt',
    long_description=__doc__,
    py_modules=['flask_mptt'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'sqlalchemy_mptt'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
