from setuptools import setup

setup(
    author='Jonathan Sharpe',
    author_email='mail@jonrshar.pe',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pelican :: Themes',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='Bulrush theme for Pelican',
    install_requires=['markupsafe', 'webassets', 'yuicompressor'],
    license='ISC',
    name='bulrush',
    package_data={
        'bulrush': [
            'templates/*.html',
            'static/css/*.less',
        ]
    },
    packages=['bulrush'],
    test_suite='tests',
    tests_require=['pelican'],
    url='https://github.com/yostos/bulrush',
    version='0.1.2',
)
