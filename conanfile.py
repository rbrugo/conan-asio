from conans import ConanFile, tools, os


class AsioConan(ConanFile):
    name = "Asio"
    version = "1.10.8"
    url = "https://github.com/bincrafters/conan-asio"
    description = (
        "Asio is a cross-platform C++ library for network and low-level I/O "
        "programming that provides developers with a consistent asynchronous "
        "model using a modern C++ approach."
    )
    license = "https://github.com/chriskohlhoff/asio/blob/master/asio/LICENSE_1_0.txt"
    options = {
        "with_boost_regex": [True, False],
        "with_openssl": [True, False]
    }
    default_options = (
        "with_boost_regex=False",
        "with_openssl=False"
    )

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
        extracted_dir = "{0}-{0}-{1}".format(
            self.name.lower(),
            self.version.replace('.', '-')
        )
        include_dir = os.path.join(
            extracted_dir,
            self.name.lower(),
            "include"
        )
        print(include_dir)
        self.copy(pattern="*.hpp", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()
