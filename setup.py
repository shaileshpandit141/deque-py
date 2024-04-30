from setuptools import setup


setup(
    name='deque',
    version='1.0.0',
    author='Author',
    author_email='author@gmail.com',
    description='Write a short description for your project.',
    long_description='Write a long description for your project.',
    long_description_content_type='text/markdown',
    url='https://github.com/username/project_name',
    packages=['deque'],
    install_requires=[
        # List of dependencies your module requires.
    ],
    entry_points={
        'console_scripts': [
            # 'command_name=module_name:function name',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)