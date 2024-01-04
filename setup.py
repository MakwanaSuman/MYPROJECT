from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    print(long_description)

setup(
    name='mycli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mycli=mycli.cli:cli',
        ],
    },
    author='suman',
    author_email='yl@logicode.in',
    description='Your CLI Tool Description',
    long_description=long_description,  # Include the contents of README.md
    long_description_content_type='text/markdown',
    url='https://github.com/MakwanaSuman/MYCLI',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
