#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "lyra"
    version = "1.1"
    description = "A simple to use, composable, command line parser for C++ 11 and beyond"
    topics = ("command line", "parsing", "cli")
    url = "https://github.com/swissdotnet-sa/conan-lyra"
    homepage = "https://github.com/bfgroup/Lyra"
    author = "Simon Lepasteur <simon.lepasteur@swissdotnet.ch>"
    license = "MIT"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/Lyra-{1}.tar.gz".format(self.homepage, self.version), sha256="767dc1718e53678cbea00977adcd0a8a195802a505aec3c537664cf25a173142")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", self._source_subfolder)
        self.copy(pattern="*.h*", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_info(self):
        self.info.header_only()
