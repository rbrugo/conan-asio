from conans import ConanFile, tools, os

class AsioConan(ConanFile):
    name = "Asio"
    version = "1.10.8"
    url = "https://github.com/bincrafters/conan-asio"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "https://github.com/chriskohlhoff/asio/blob/master/asio/LICENSE_1_0.txt"
    options = {"shared": [True, False], "with_boost_regex": [True, False], "with_openssl": [True, False]}
    default_options = "shared=False", "with_boost_regex=False", "with_openssl=False"
    
    def requirements(self):
        if self.options.with_boost_regex:
            self.requires.add("Boost.Regex/1.64.0@bincrafters/stable")

        if self.options.with_openssl:
            self.requires.add("OpenSSL/1.0.2@conan/stable")
                      
    def source(self):
        source_url = "https://github.com/chriskohlhoff/asio"
        archive_name = "asio-" + self.version.replace(".", "-")
        tools.get("{0}/archive/{1}.tar.gz".format(source_url,  archive_name))

    def package(self):
        extracted_dir = self.name + "-" + self.name + "-" + self.version.replace(".", "-")
        include_dir = os.path.join(extracted_dir, self.name, "include")
        self.copy(pattern="*.hpp", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()