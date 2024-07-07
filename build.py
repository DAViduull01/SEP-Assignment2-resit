from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "your_project_name"
version = "0.1.0"
default_task = ["clean", "install_dependencies", "publish"]

@init
def initialize(project):
    project.build_depends_on("mock")
    project.set_property("dir_source_unittest_python", "tests")
