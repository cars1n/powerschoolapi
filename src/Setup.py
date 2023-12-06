from setuptools import setup, find_packages

setup(
    name='powerschoolapi',
    version='1.0',
    packages=find_packages(),
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourgithub/YourPackageName',
    install_requires=[
        'requests',
        'python-dotenv',
        'dotenv',
        'urllib3',
        'icecream'
        # other dependencies
    ],
    classifiers=[
        # Choose appropriate classifiers from
        # https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
