from setuptools import setup

setup(
    name='fields_testing',
    version='1.0.0',
    description='Allows to test django-models fields.',
    package_dir={'fields_testing': 'src'},
    author='Adam Lewandowski',
    author_email='adam_lewandowski_1998@outlook.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 5.1',
        'Framework :: Pytest',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)
