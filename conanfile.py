from os.path import join as path_join
from conans import ConanFile, CMake

class RapidJSONConan(ConanFile):
    name = "RapidJSON"
    version = '1.1.0'
    license = 'https://github.com/miloyip/rapidjson/blob/master/license.txt'
    exports = 'FindRapidJSON.cmake'
    url = 'https://github.com/Brunni/conan-rapidjson/'

    def source(self):
        self.run("git clone --depth=1 https://github.com/miloyip/rapidjson -b v%s" % self.version)

    def package(self):
        self.copy('*', dst='include', src='rapidjson/include')

    def build(self):
        pass
