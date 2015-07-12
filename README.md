# AoA
Ashes of Apocalypse: An OpenMW Game.


# Validation process
Unpacked Morrowind, Tribunal, Bloodmoon BSA files and used md5sum to create a list of all Bethesda assets and their checksum. They can be found in the ./copyright directory.

BSA Unpacker: http://www.nexusmods.com/morrowind/mods/12189

We made another checksum manifest of AoA 1.0 and 1.1 and cross-check the checksums to see if there are Bethesda assets in AoA.

Using `validate.py`, it compared all AoA md5sums against those in Bethesda's BSA files.

## Result of validation

The original AoA releases (1.0 and 1.1) did contain Bethesda's files.

Comparing md5sum of AoA version 1.0 to the contents Bethesda's BSA files.
Out of 4304 files, found 139 bethesda files.

Comparing md5sum of AoA version 1.1 to the contents Bethesda's BSA files.
Out of 194 files, found 0 bethesda files.

## Conclusion

We'll need to replace the 139 files in order to make a CC-BY-SA game for OpenMW.
