from distutils.core import setup

setup(
        name='customizable_django_profiler',
        version='0.1',
        url='https://github.com/someshchaturvedi/django_profiler',
        description='Django middleware based on cProfile',
        author='Somesh Chaturvedi',
        author_email='somesh.08.96@gmail.com',
        license='MIT',
        packages=['django_profiler'],
        keywords = ['django','middleware','cProfile', 'Profile'],
        zip_safe=False,
        download_url = 'https://github.com/someshchaturvedi/django_profiler/archive/0.1.tar.gz'
      )
