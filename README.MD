# Key-mapper

This is a tool to map keys on your keyboard to other keys. It can be used to map keys to keys that are not present on your keyboard, to map keys to macros or to map keys to mouse buttons. The tool is written in Python and make use of the module `keyboard` (`https://github.com/boppreh/keyboard`), where on the homepage you can find more information about which modifiers that can be used (e.g. Alt, Ctrl, Shift, Win, etc.). The tool is developed for Windows, but it should also work on Linux and Mac.

## Releases

The latest release can be found under the folder `releases`. Please note that files `key-mapper.exe` and `mappings.json` must be in the same folder.
The releases are compiled with PyInstaller and can be run without installing Python.

## Phonetic Symbols

As this tool first was developed to map keys to phonetic symbols, it is by default configured to map keys to International Phonetic Alphabet (IPA). The symbols are configured so it is possible to type them with a standard keyboard. The mapping however can be changed to any other mapping via the `mappings.json` file which can be opened in a standard text editor. Other phonetic symbols can be found here: `https://www.phon.ucl.ac.uk/resource/sfs/wasp/ipa.htm`
