from conans import ConanFile, tools, os


class BoostChronoConan(ConanFile):
    name = "Boost.Chrono"
    version = "1.65.1"
    generators =  "boost"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-chrono"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["chrono"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    build_requires = "Boost.Build/1.65.1@bincrafters/testing", "Boost.Generator/1.65.1@bincrafters/testing"
    requires =  "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Integer/1.65.1@bincrafters/testing", \
                      "Boost.Move/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Predef/1.65.1@bincrafters/testing", \
                      "Boost.Ratio/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.System/1.65.1@bincrafters/testing", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Typeof/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing", \
                      "Boost.Winapi/1.65.1@bincrafters/testing"

                      #assert1 config0 core2 integer3 move3 mpl5 predef0 ratio7 static_assert1 system3 throw_exception2 type_traits3 typeof5 utility5 winapi1

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)
    
    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        self.copy(pattern="*", dst="lib", src="stage/lib")
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_info(self):
        self.user_info.lib_short_names = ",".join(self.lib_short_names)
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")
