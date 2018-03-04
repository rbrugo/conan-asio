#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools
from conans.errors import ConanException

class AsioConan(ConanFile):
    name = "asio"
    version = "1.11.0"
    url = "https://github.com/bincrafters/conan-asio"
    description = (
        "Asio is a cross-platform C++ library for network and low-level I/O "
        "programming that provides developers with a consistent asynchronous "
        "model using a modern C++ approach."
    )
    license = "BSL-1.0"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    options = {
        "standalone": [True, False],
        "with_boost_regex": [True, False],
        "with_openssl": [True, False]
    }
    default_options = (
        "standalone=True",
        "with_boost_regex=False",
        "with_openssl=False"
    )
    settings = "os"

    def configure(self):
        if self.options.standalone and self.options.with_boost_regex:
            raise ConanException(
                "'standalone' and 'with_boost_regex' are mutually exclusive! "
                "Please disable one of them."
            )

    def requirements(self):
        if self.options.with_boost_regex:
            self.requires.add("Boost.Regex/[>=1.64.0]@bincrafters/stable")

        if self.options.with_openssl:
            self.requires.add("OpenSSL/[>=1.0.2]@conan/stable")

    def source(self):
        source_url = "https://github.com/chriskohlhoff/asio"
        archive_name = "asio-" + self.version.replace(".", "-")
        tools.get("{0}/archive/{1}.tar.gz".format(source_url,  archive_name))
        extracted_name =  "asio-" + archive_name
        os.rename(extracted_name, self.source_subfolder)

    def package(self):
        root_dir = os.path.join(self.source_subfolder, self.name)
        include_dir = os.path.join(root_dir, "include")
        self.copy(pattern="LICENSE_1_0.txt", dst="license", src=root_dir)
        self.copy(pattern="*.hpp", dst="include", src=include_dir)
        self.copy(pattern="*.ipp", dst="include", src=include_dir)

    def package_info(self):
        if self.options.standalone:
            self.cpp_info.cppflags = ['-DASIO_STANDALONE']
        if self.settings.os == 'Linux':
            self.cpp_info.libs.append('pthread')

    def package_id(self):
        self.info.header_only()
