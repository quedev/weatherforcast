from setuptools import setup

setup(
    name='forcastweather',  # Your package will have this name
    packages=['forcastweather'],  # Name the package again
    version='1.0.0',  # To be increased every time you change your library
    license='MIT',  # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',  # Short description of your library
    author='Hamed Abbaszadeh',  # Your name
    author_email='mail2hamedaz@gmail.com',  # Your email
    url='https://github.com/quedev/weatherforcast.git',  # Homepage of your library (e.g. github or your website)
    keywords=['weather', 'forecast', 'openweather'],  # Keywords users can search on pypi.org
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Type a license again
        'Programming Language :: Python :: 3.5',  # Python versions that your library supports
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
