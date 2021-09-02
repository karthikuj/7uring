import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="7uring", 
    version="1.0.0",
    author="Karthik UJ",
    author_email="karthikuj2001@gmail.com",
    description="An advanced cryptography tool.",
    long_description=' An advanced cryptography tool for hashing, encrypting, encoding, steganography and more.',
    long_description_content_type="text/markdown",
    url="https://github.com/karthikuj/7uring",
    project_urls={
        "Bug Tracker": "https://github.com/karthikuj/7uring/issues",
    },
    download_url = 'https://github.com/karthikuj/7uring/archive/refs/tags/v1.0.tar.gz',
    install_requires=[            
          'requests',
          'beautifulsoup4',
          'pyenchant',
      ],
    entry_points = {
        'console_scripts': [
            '7uring = turing.turing:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords = ['hashing', 'encoding', 'encryption', 'steganography', 'cryptanalysis', 'steganalysis', 'cipher'],
    zip_safe = False,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
