import paver
from paver.easy import *
from socket import gethostname
import paver.setuputils
paver.setuputils.install_distutils_tasks()
from os import environ
import pkg_resources

######## CHANGE THIS ##########
project_name = "pythonds"
###############################

# If you want to override the master url do it here.  Otherwise setting it to
# None configures it for the default case of wanting to use localhost for
# development and interactivepython for deployment

master_url = None
if master_url is None:
    if gethostname() == 'web407.webfaction.com':
        master_url = 'http://interactivepython.org'
        doctrees = '../../custom_courses/{}/doctrees'.format(project_name)
    else:
        master_url = 'http://127.0.0.1:8000'
        doctrees = './build/{}/doctrees'.format(project_name)

master_app = 'data_structures_and_algorithms_with_python_remixed'
serving_dir = './build/pythonds'
dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/"+project_name,
        sourcedir="./_sources/",
        outdir="./build/"+project_name,
        confdir=".",
        project_name = project_name,
        doctrees = doctrees,
        template_args = {
            'course_id':project_name,
            'login_required':'false',
            'appname':master_app,
            'loglevel':10,
            'course_url':master_url,
            'use_services': 'false',
            'python3': 'true',
            'basecourse': 'pythonds',
        }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

from runestone import build  # build is called implicitly by the paver driver.
