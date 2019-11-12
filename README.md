## Conan package recipe for [*lyra*](https://github.com/bfgroup/Lyra)

A simple to use, composable, command line parser for C++ 11 and beyond https://bfgroup.github.io/Lyra/

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/beta/#/swissdotnet/public-conan/lyra:swissdotnet).

## For Users

### Basic setup

    $ conan install lyra/1.1.0@swissdotnet/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    lyra/1.1.0@swissdotnet/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . swissdotnet/testing


## Add Remote

    $ conan remote add <REMOTE> https://api.bintray.com/conan/swissdotnet/public-conan


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package expected.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/swissdotnet-sa/conan-clara/blob/master/LICENSE)