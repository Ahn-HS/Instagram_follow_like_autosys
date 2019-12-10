# from distutils.core import setup
# import py2exe
#
# setup(
#     options = {"py2exe": {"packages": ["encodings"],
#                           "bundle_files": 1}},
#     zipfile = None,
#     windows = ["loading.py"],
# )
#


from cx_Freeze import setup, Executable

base = None

addtional_mods = ['numpy.core._methods', 'numpy.lib.format']
executables = [Executable("test.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
        'includes':addtional_mods,
    },

}

setup(
    name = "yes",
    options = options,
    version = "1.1",
    description = 'no',
    executables = executables
)