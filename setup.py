from setuptools import setup, find_packages
import sys

with open('generate_background_image/README.md', encoding='utf-8') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='generate_background_image',
    version='0.0.1',
    description='Generate a background image of words in a given string using the wordcloud module.',
    long_description=README,
	long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    author='Mohd Saqib',
    author_email='mohdsaqibhbi@gmail.com',
    keywords=['generate image', 'background image', 'image for blog', 'image for git repo'],
    url='https://github.com/mohdsaqibhbi/How-to-build-Python-Package.git',
    download_url='https://pypi.org/project/generate_background_image/'
)
install_requires = ["wordcloud"]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
