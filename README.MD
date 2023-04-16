# Key-mapper

This is a tool to map letters (keys) on your keyboard to other letters which cannot be typed without knowing the specific key combination (e.g. Alt-codes). It can also be used to map keys to macros or mouse buttons.

The tool is developed for Windows, but it should also work on Linux and Mac.

## Usage

The mapping can be changed to any other mapping via the `mappings.json` file which can be opened in a standard text editor. To use special key modifiers please refer to the Python module `keyboard` (`https://github.com/boppreh/keyboard`).

The 'toggle' key is the key which is used to toggle the mapping on and off. The 'hotkeys' are the keys to be mapped to the defined symbols.

### Example

To map the key `a` to the symbol `ɠ`, the following line can be added to the `mappings.json` file:`

`"a": "\u0260",`

Please note the comma at the end of the line, which is required to separate the lines. Also note that in this case the `ɠ` is defined as a Unicode character, see `https://unicode-table.com/en/0260/`

## Releases

The latest release can be found under the folder `releases`. Please note that files `key-mapper.exe` and `mappings.json` must be in the same folder.
The releases are compiled with `PyInstaller` and the program can therefore be run without having Python installed.

## Phonetic Symbols

As this tool first was developed to map keys to the International Phonetic Alphabet (IPA), it is by default configured for that. Other phonetic symbols can be found here: `https://www.phon.ucl.ac.uk/resource/sfs/wasp/ipa.htm`
