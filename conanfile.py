from conans import ConanFile, tools, os


class BoostChronoConan(ConanFile):
    name = "Boost.Chrono"
    version = "1.64.0"
    generators = "txt", "boost"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-chrono"
    source_url = "https://github.com/boostorg/chrono"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["chrono"]
    build_requires = "Boost.Build/1.64.0@bincrafters/testing", "Boost.Generator/0.0.1@bincrafters/testing"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Ratio/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Typeof/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Winapi/1.64.0@bincrafters/testing"

                      #assert1 config0 core2 integer3 move3 mpl5 predef0 ratio7 static_assert1 system3 throw_exception2 type_traits3 typeof5 utility5 winapi1

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 
    
    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
