<a id="//apple_ref/doc/uid/TP40016239-CH34"></a><a id="//apple_ref/doc/uid/TP40016239-CH34-SW1"></a>
<a id="//apple_ref/doc/uid/TP40016239-CH57"></a><a id="//apple_ref/doc/uid/TP40016239-CH57-SW1"></a>

## Referencing Files and Folders

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW39"></a>

### Referencing Files and Folders in AppleScript

In AppleScript, file and folder paths are typically represented using `alias`, `file`, and `POSIX file` objects.

> **Note**
>
>
> Additional information about working with file and folder paths in AppleScript can be found in [Aliases and Files](https://developer.apple.com/library/archive/../../AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW28) in *[AppleScript Language Guide](https://developer.apple.com/library/archive/../../AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html#//apple_ref/doc/uid/TP40000983)*.

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW3"></a>

### Alias Objects

An `alias` object dynamically points to an existing item in the file system. Since an alias is dynamic, it continues pointing to the item even if the item is renamed or moved, the same way an alias file works when you manually create one in the Finder. With an AppleScript alias, the original item must exist at run time or an error will occur.

An `alias` object is displayed as a colon-delimited path preceded by an `alias` specifier, in the format shown in Listing 15-1.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=alias%20%22VolumeName%3AFolderName%3ASubfolderName%3AFileName%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW4"></a>
**Listing 15-1**AppleScript: Structure of an alias object

1. `alias "VolumeName:FolderName:SubfolderName:FileName"`

Listing 15-2 shows an example of an `alias` object that references the Desktop folder.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3A%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW5"></a>
**Listing 15-2**AppleScript: Example of an alias reference to a folder

1. `alias "Macintosh HD:Users:yourUserName:Desktop:"`

Listing 15-3 is an example of an `alias` object that references an existing file on the Desktop.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW6"></a>
**Listing 15-3**AppleScript: Example of an alias reference to a file

1. `alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

To create an alias, add the alias specifier prefix to a colon-delimited path string, as shown in Listing 15-4.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3A%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW10"></a>
**Listing 15-4**AppleScript: Creating an alias from a colon-delimited path string

1. `set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:"`

Many commands accept an alias as a parameter and/or return an alias as a result. In Listing 15-5, the `choose file` command accepts a folder `alias` object in its `default location` parameter. The command then returns an `alias` object that points to the chosen file.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theDefaultFolder%20to%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3A%22%0Achoose%20file%20default%20location%20theDefaultFolder)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW18"></a>
**Listing 15-5**AppleScript: Example of a command that accepts an alias parameter and returns an alias result

1. `set theDefaultFolder to alias "Macintosh HD:Users:yourUserName:Desktop:"`
2. `choose file default location theDefaultFolder`
3. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW7"></a>

### File Objects

A `file` object is a static reference to an item at a specific location in the file system. It’s not dynamic, and can even refer to an item that doesn’t exist yet. For example, a `save` command may accept a file reference when saving to a new file.

A `file` object is displayed as a colon-delimited path preceded by a `file` specifier, in the format shown in Listing 15-6.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=file%20%22VolumeName%3AFolderName%3ASubfolderName%3AFileName%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW8"></a>
**Listing 15-6**AppleScript: Structure of a file object

1. `file "VolumeName:FolderName:SubfolderName:FileName"`

Listing 15-7 shows an example of a `file` object that references a file that may or may not exist on the Desktop.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=file%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW9"></a>
**Listing 15-7**AppleScript: Example of a file reference to a file

1. `file "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

Unlike the way an `alias` object works, you can’t create a `file` object simply by prefixing a path string with the `file` specifier. For example, Listing 15-7 errors when run within a script.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFile%20to%20file%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW20"></a>
**Listing 15-8**AppleScript: Example of incorrect usage of a file object specifier

1. `set theFile to file "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

Instead, you must prefix the path with the `file` specifier at the time the file is targeted by a command, as shown in Listing 15-8.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFile%20to%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0Aread%20file%20theFile)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW21"></a>
**Listing 15-9**AppleScript: Example of correct usage of a file object specifier

1. `set theFile to "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
2. `read file theFile`

> **Note**
>
>
> A `file` object can refer to either a file or a folder, despite the `file` specifier prefix.

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW11"></a>

### POSIX File Objects

Some scriptable apps are designed to work with POSIX-style paths, rather than AppleScript `alias` and `file` objects. Like a `file` object, a `POSIX file` object is not dynamic and can also refer to an item that doesn’t exist yet.

A `POSIX file` object is displayed as a slash-delimited path preceded by a `POSIX file` specifier, in the format shown in Listing 15-10.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=POSIX%20file%20%22%2FFolderName%2FSubfolderName%2FFileName%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW12"></a>
**Listing 15-10**AppleScript: Structure of a POSIX file object

1. `POSIX file "/FolderName/SubfolderName/FileName"`

Listing 15-11 is an example of a `POSIX file` object that references a file that may or may not exist on the Desktop.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=POSIX%20file%20%22%2FUsers%2FyourUserName%2FDesktop%2FMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW13"></a>
**Listing 15-11**AppleScript: Example of a POSIX file reference to a file

1. `POSIX file "/Users/yourUserName/Desktop/My File.txt"`

> **Note**
>
>
> A `POSIX file` object can refer to either a file or a folder, despite the `POSIX file` specifier prefix.
>
> In a POSIX path, the startup disk’s name is omitted and represented by a leading slash. Other disks are referenced in relation to the `Volumes` directory of the startup disk, for example: `/Volumes/DiskName/FolderName/SubFolderName/FileName`.

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW15"></a>

### App-Specific References to Files and Folders

Some apps, such as the Finder and System Events, have their own syntax for referring to files and folders. Listing 15-12 shows how a Finder file reference appears.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=document%20file%20%22My%20File.txt%22%20of%20folder%20%22Desktop%22%20of%20folder%20%22yourUserName%22%20of%20folder%20%22Users%22%20of%20startup%20disk%20of%20application%20%22Finder%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW16"></a>
**Listing 15-12**AppleScript: Example of a reference to a file in the Finder

1. `document file "My File.txt" of folder "Desktop" of folder "yourUserName" of folder "Users" of startup disk of application "Finder"`

Listing 15-13 shows how a System Events folder reference appears.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=folder%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3A%22%20of%20application%20%22System%20Events%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW17"></a>
**Listing 15-13**AppleScript: Example of a reference to a folder in System Events

1. `folder "Macintosh HD:Users:yourUserName:Desktop:" of application "System Events"`

Since this terminology is app-specific, it doesn’t work in other apps. For example, you can’t write a script that tries to import a Finder reference to an audio file into iTunes because iTunes doesn’t understand Finder file references. In this case, you must coerce the Finder file reference to something iTunes can understand, like an alias. See [Converting Between Path Formats](#//apple_ref/doc/uid/TP40016239-CH34-SW19) below. In most cases, apps with their own path syntax also support standard AppleScript path types.

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW19"></a>

### Converting Between Path Formats

Since different situations may result in paths appearing in different formats, you may need to regularly convert one path format to another. Sometimes, this can be done by using the `as` coercion operator, as shown in Listing 15-14, Listing 15-15, Listing 15-16, and Listing 15-17.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFilePath%20to%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0Aset%20theFilePath%20to%20theFilePath%20as%20alias)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW23"></a>
**Listing 15-14**AppleScript: Coercing a string to an alias

1. `set theFilePath to "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
2. `set theFilePath to theFilePath as alias`
3. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFilePath%20to%20choose%20file%0A--%3E%20Result%3A%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0A%0Aset%20theFilePath%20to%20theFilePath%20as%20string%0A--%3E%20Result%3A%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW24"></a>
**Listing 15-15**AppleScript: Coercing an alias to a string

1. `set theFilePath to choose file`
2. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
3. ` `
4. `set theFilePath to theFilePath as string`
5. `--> Result: "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFilePath%20to%20POSIX%20file%20%22%2FUsers%2FyourUserName%2FDesktop%2FMy%20File.txt%22%0Aset%20theFilePath%20to%20theFilePath%20as%20alias%0A)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW25"></a>
**Listing 15-16**AppleScript: Coercing a POSIX file to an alias

1. `set theFilePath to POSIX file "/Users/yourUserName/Desktop/My File.txt"`
2. `set theFilePath to theFilePath as alias`
3. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=tell%20application%20%22Finder%22%0A%20%20%20%20set%20theFilePath%20to%20file%20%22My%20File.txt%22%20of%20desktop%0Aend%20tell%0A--%3E%20Result%3A%20document%20file%20%22My%20File.txt%22%20of%20folder%20%22Desktop%22%20of%20folder%20%22yourUserName%22%20of%20folder%20%22Users%22%20of%20startup%20disk%20of%20application%20%22Finder%22%0A%0Aset%20theFilePath%20to%20theFilePath%20as%20alias%0A--%3E%20Result%3A%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW37"></a>
**Listing 15-17**AppleScript: Coercing a Finder file reference to an alias

1. `tell application "Finder"`
2. ` set theFilePath to file "My File.txt" of desktop`
3. `end tell`
4. `--> Result: document file "My File.txt" of folder "Desktop" of folder "yourUserName" of folder "Users" of startup disk of application "Finder"`
5. ` `
6. `set theFilePath to theFilePath as alias`
7. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

Converting from a string or alias to a POSIX path can’t be done through coercion. Instead, you must access the `POSIX path` property of the path to convert, as shown in Listing 15-18.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theFilePath%20to%20choose%20file%0A--%3E%20Result%3A%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0A%0Aset%20theFilePath%20to%20POSIX%20path%20of%20theFilePath%0A--%3E%20Result%3A%20%22%2FUsers%2FyourUserName%2FDesktop%2FMy%20File.txt%22)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW26"></a>
**Listing 15-18**AppleScript: Converting an alias to a POSIX path string

1. `set theFilePath to choose file`
2. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
3. ` `
4. `set theFilePath to POSIX path of theFilePath`
5. `--> Result: "/Users/yourUserName/Desktop/My File.txt"`

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW27"></a>

### Using Conversion Handlers

Running paths through a conversion handler is a good way to ensure the format you expect.

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW28"></a>

### Converting a Path to an Aliases

The handler in Listing 15-19 converts strings, `path` objects, `POSIX file` objects, Finder paths, and System Events paths to `alias` format.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=on%20convertPathToAlias%28thePath%29%0A%20%20%20%20tell%20application%20%22System%20Events%22%0A%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20%28path%20of%20disk%20item%20%28thePath%20as%20string%29%29%20as%20alias%0A%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20%28path%20of%20disk%20item%20%28path%20of%20thePath%29%20as%20string%29%20as%20alias%0A%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20end%20tell%0Aend%20convertPathToAlias)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW29"></a>
**Listing 15-19**AppleScript: Handler that converts a path to an AppleScript alias

1. `on convertPathToAlias(thePath)`
2. ` tell application "System Events"`
3. ` try`
4. ` return (path of disk item (thePath as string)) as alias`
5. ` on error`
6. ` return (path of disk item (path of thePath) as string) as alias`
7. ` end try`
8. ` end tell`
9. `end convertPathToAlias`

Listing 15-19 shows how to call the handler in Listing 15-19 to convert a POSIX-style path string to an alias.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20%22%2FUsers%2FyourUserName%2FDesktop%2FMy%20File.txt%22%0Aset%20thePath%20to%20convertPathToAlias%28thePath%29)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW30"></a>
**Listing 15-20**AppleScript: Calling a handler to convert a path to an AppleScript alias

1. `set thePath to "/Users/yourUserName/Desktop/My File.txt"`
2. `set thePath to convertPathToAlias(thePath)`
3. `--> Result: alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW31"></a>

### Converting a Path to a String

The handler in Listing 15-21 converts a path to string format.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=on%20convertPathToString%28thePath%29%0A%20%20%20%20tell%20application%20%22System%20Events%22%0A%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20path%20of%20disk%20item%20%28thePath%20as%20string%29%0A%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20path%20of%20thePath%0A%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20end%20tell%0Aend%20convertPathToString)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW32"></a>
**Listing 15-21**AppleScript: Handler that converts a path to an a string

1. `on convertPathToString(thePath)`
2. ` tell application "System Events"`
3. ` try`
4. ` return path of disk item (thePath as string)`
5. ` on error`
6. ` return path of thePath`
7. ` end try`
8. ` end tell`
9. `end convertPathToString`

Listing 15-22 shows how to call the handler in Listing 15-21 to convert an alias to a path string.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0Aset%20thePath%20to%20convertPathToString%28thePath%29%0A)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW33"></a>
**Listing 15-22**AppleScript: Calling a handler to convert an AppleScript alias to a path string

1. `set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
2. `set thePath to convertPathToString(thePath)`
3. `--> Result: "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW34"></a>

### Converting a Path to a POSIX Path String

The handler in Listing 15-23 converts a path to POSIX path string format.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=on%20convertPathToPOSIXString%28thePath%29%0A%20%20%20%20tell%20application%20%22System%20Events%22%0A%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20thePath%20to%20path%20of%20disk%20item%20%28thePath%20as%20string%29%0A%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20thePath%20to%20path%20of%20thePath%0A%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20end%20tell%0A%20%20%20%20return%20POSIX%20path%20of%20thePath%0Aend%20convertPathToPOSIXString)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW35"></a>
**Listing 15-23**AppleScript: Handler that converts a path to an a POSIX path string

1. `on convertPathToPOSIXString(thePath)`
2. ` tell application "System Events"`
3. ` try`
4. ` set thePath to path of disk item (thePath as string)`
5. ` on error`
6. ` set thePath to path of thePath`
7. ` end try`
8. ` end tell`
9. ` return POSIX path of thePath`
10. `end convertPathToPOSIXString`

Listing 15-24 shows how to call the handler in Listing 15-23 to convert an alias to a path string.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20alias%20%22Macintosh%20HD%3AUsers%3AyourUserName%3ADesktop%3AMy%20File.txt%22%0Aset%20thePath%20to%20convertPathToPOSIXString%28thePath%29%0A)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW36"></a>
**Listing 15-24**AppleScript: Calling a handler to convert an AppleScript alias to a POSIX path string

1. `set thePath to alias "Macintosh HD:Users:yourUserName:Desktop:My File.txt"`
2. `set thePath to convertPathToPOSIXString(thePath)`
3. `--> Result: "/Users/yourUserName/Desktop/My File.txt"`

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW40"></a>

### Referencing Files and Folders in JavaScript

In JavaScript, file and folder paths are represented using `Path` objects.

To create a path, pass a POSIX-style string to the `Path` object, as shown in Listing 15-25.

**JAVASCRIPT**

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW38"></a>
**Listing 15-25**JavaScript: Creating a `Path` object

1. `Path("/FolderName/SubfolderName/FileName")`

To convert a path to a string, call the `toString()` method on the path, as shown in Listing 15-26.

**JAVASCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=var%20path%20%3D%20Path%28%22%2FUsers%2FyourUserName%2FDesktop%2FMy%20File.txt%22%29%0Avar%20string%20%3D%20path.toString%28%29%0Astring)

<a id="//apple_ref/doc/uid/TP40016239-CH34-SW41"></a>
**Listing 15-26**JavaScript: Converting a `Path` object to a string

1. `var path = Path("/Users/yourUserName/Desktop/My File.txt")`
2. `var string = path.toString()`
3. `string`
4. `// Result: "/Users/yourUserName/Desktop/My File.txt"`
