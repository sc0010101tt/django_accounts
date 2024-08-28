from setuptools import setup, find_packages

setup(
    name='django-accounts',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A reusable Bootstrap Django app for user authentication and account management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sc0010101tt/django-accounts',
    author='Scott Benson',
    author_email='scottnicholasbenson@hotmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2.15',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9.13',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
