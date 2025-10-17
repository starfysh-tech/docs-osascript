<a id="//apple_ref/doc/uid/TP40000983-CH216-SW59"></a>

# Commands Reference

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_640"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_641"></a>This chapter describes the commands available to perform actions in AppleScript scripts. For information on how commands work, see [Commands Overview](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW8).

The commands described in this chapter are available to any script—they are either built into the AppleScript language or added to it through the standard scripting additions (described in [Scripting Additions](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW3)).

> <a id="//apple_ref/doc/uid/TP40000983-CH216-SW67"></a>
>
> **Note:** In the command descriptions below, if the first item in the Parameters list does not include a parameter name, it is the direct parameter of the command (described in [Direct Parameter](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW13)).

Table 7-1 lists each command according to the suite (or related group) of commands to which it belongs and provides a brief description. Detailed command descriptions follow the table, in alphabetical order.

<a id="//apple_ref/doc/uid/TP40000983-CH216-CHDCCDDB"></a>

**Table 7-1**  AppleScript commands

| Command | Description |
| *AppleScript suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_642"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_643"></a> |  |
| `activate` | Brings an application to the front, and opens it if it is on the local computer and not already running. |
| `log` | In Script Editor, displays a value in the Event Log History window or in the Event Log pane of a script window. |
| *Clipboard Commands suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_644"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_645"></a> |  |
| `clipboard info` | Returns information about the clipboard. |
| `set the clipboard to` | Places data on the clipboard. |
| `the clipboard` | Returns the contents of the clipboard. |
| *File Commands suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_646"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_647"></a> |  |
| `info for` | Returns information for a file or folder. |
| `list disks` | Returns a list of the currently mounted volumes.  *Deprecated* Use `tell application "System Events" to get the name of every disk`. |
| `list folder` | Returns the contents of a specified folder.  *Deprecated* Use `tell application "System Events" to get the name of every disk item of ...`. |
| `mount volume` | Mounts the specified AppleShare volume. |
| `path to (application)` | Returns the full path to the specified application. |
| `path to (folder)` | Returns the full path to the specified folder. |
| `path to resource` | Returns the full path to the specified resource. |
| *File Read/Write suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_648"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_649"></a> |  |
| `close access` | Closes a file that was opened for access. |
| `get eof` | Returns the length, in bytes, of a file. |
| `open for access` | Opens a disk file for the `read` and `write` commands. |
| `read` | Reads data from a file that has been opened for access. |
| `set eof` | Sets the length, in bytes, of a file. |
| `write` | Writes data to a file that was opened for access with write permission. |
| *Internet suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_650"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_651"></a> |  |
| `open location` | Opens a URL with the appropriate program. |
| *Miscellaneous Commands suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_652"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_653"></a> |  |
| `current date` | Returns the current date and time. |
| `do shell script` | Executes a shell script using the `sh` shell. |
| `get volume settings` | Returns the sound output and input volume settings. |
| `random number` | Generates a random number. |
| `round` | Rounds a number to an integer. |
| `set volume` | Sets the sound output and/or input volume. |
| `system attribute` | Gets environment variables or attributes of this computer. |
| `system info` | Returns information about the system. |
| `time to GMT` | Returns the difference between local time and GMT (Universal Time). |
| *Scripting suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_654"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_655"></a> |  |
| `load script` | Returns a `script` object loaded from a file. |
| `run script` | Runs a script or script file |
| `scripting components` | Returns a list of all scripting components. |
| `store script` | Stores a `script` object into a file. |
| *Standard suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_656"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_657"></a> |  |
| `copy` | Copies one or more values into variables. |
| `count` | Counts the number of elements in an object. |
| `get` | Returns the value of a script expression or an application object. |
| `launch` | Launches the specified application without sending it a `run` command. |
| `run` | For an application, launches it. For a script application, launches it and sends it the `run` command. For a script script object, executes its `run` handler. |
| `set` | Assigns one or more values to one or more script variables or application objects. |
| *String Commands suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_658"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_659"></a> |  |
| `ASCII character` | Converts a number to a character.  *Deprecated* starting in AppleScript 2.0. Use the `id` property of the `text` class instead. |
| `ASCII number` | Converts a character to its numeric value.  *Deprecated* starting in AppleScript 2.0. Use the `id` property of the `text` class instead. |
| `localized string` | Returns the localized string for the specified key. |
| `offset` | Finds one piece of text inside another. |
| `summarize` | Summarizes the specified text or text file. |
| *User Interaction suite*<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_660"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_661"></a> |  |
| `beep` | Beeps one or more times. |
| `choose application` | Allows the user to choose an application. |
| `choose color` | Allows the user to choose a color. |
| `choose file` | Allows the user to choose a file. |
| `choose file name` | Allows the user to specify a new file reference. |
| `choose folder` | Allows the user to choose a folder. |
| `choose from list` | Allows the user to choose one or more items from a list. |
| `choose remote application` | Allows the user to choose a running application on a remote machine. |
| `choose URL` | Allows the user to specify a URL. |
| `delay` | Pauses for a fixed amount of time. |
| `display alert` | Displays an alert. |
| `display dialog` | Displays a dialog box, optionally requesting user input. |
| `display notification` | Displays a notification. |
| `say` | Speaks the specified text. |

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW60"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_662"></a>

activate

Brings an application to the front, launching it if necessary.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_63"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW68"></a>`activate` | | *application* | required |

##### Parameters

*application*
:   The application to activate.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_64"></a>

##### Examples

```
activate application "TextEdit"
tell application "TextEdit" to activate
```

##### Discussion

The `activate` command does not launch applications on remote machines. For examples of other ways to specify an application, see the `application` class and [Remote Applications](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW9).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW21"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_663"></a>

ASCII character

Returns the character for a specified number.

> <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_65"></a>
>
> **Important:** This command is deprecated starting in AppleScript 2.0—use the `id` property of the `text` class instead.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_66"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW50"></a>`ASCII character` | | *integer* | required |

##### Parameters

*[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The character code, an integer between 0 and 255.

##### Result

A `text` object containing the character that corresponds to the specified number.

Signals an error if *integer* is out of range.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_67"></a>

##### Examples

```
set theChar to ASCII character 65 --result: "A"
set theChar to ASCII character 194 --result: "¬"
set theChar to ASCII character 2040 --result: invalid range error
```

##### Discussion

The name “ASCII” is something of a misnomer. `ASCII character` uses the primary text encoding, as determined by the user’s language preferences, to map between integers and characters. If the primary language is English, the encoding is Mac OS Roman, if it is Japanese, the encoding is MacJapanese, and so on. For integers below 128, this is generally the same as ASCII, but for integers from 128 to 255, the results vary considerably.

Because of this unpredictability, `ASCII character` and `ASCII number` are deprecated starting in AppleScript 2.0. Use the `id` property of the `text` class instead, since it always uses the same encoding, namely Unicode.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW22"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_664"></a>

ASCII number

Returns the number associated with a specified character.

> <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_68"></a>
>
> **Important:** This command is deprecated starting in AppleScript 2.0—use the `id` property of the `text` class instead.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_69"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW69"></a>`ASCII number` | | *text* | required |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A `text` object containing at least one character. If there is more than one character, only the first one is used.

##### Result

The character code of the specified character as an integer.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_70"></a>

##### Examples

```
set codeValue to ASCII number "¬" --result: 194
```

##### Discussion

The result of `ASCII number` depends on the user’s language preferences; see the Discussion section of `ASCII character` for details.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW1"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_665"></a>

beep

Plays the system alert sound one or more times.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_71"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW70"></a>`beep` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW71"></a> | | *integer* | optional |

##### Parameters

*[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   Number of times to beep.

*Default Value:*
:   `1`

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_72"></a>

##### Examples

Audible alerts can be useful when no one is expected to be looking at the screen:

```
beep 3 --result: three beeps, to get attention
display dialog "Something is amiss here!" -- to show message
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW2"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_666"></a>

choose application

Allows the user to choose an application.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_73"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW72"></a>`choose application` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW73"></a>`with title` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW74"></a>`with prompt` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW75"></a>`multiple selections allowed` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW76"></a>`as` | | *class* | optional |

##### Parameters

`with title` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   Title text for the dialog.

*Default Value:*
:   `"Choose Application"`

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A prompt to be displayed in the dialog.

*Default Value:*
:   `"Select an application:"`

`multiple selections allowed` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow multiple items to be selected? If `true`, the results will be returned in a list, even if there is exactly one item.

*Default Value:*
:   `false`

`as` *class* ( *[application](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW2)* | *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* )
:   Specifies the desired class of the result. If specified, the value must be one of `application` or `alias`.

*Default Value:*
:   `application`

##### Result

The selected application, as either an `application` or `alias` object; for example, `application "TextEdit"`. If multiple selections are allowed, returns a list containing one item for each selected application, if any.

Signals a “user canceled” error if the user cancels the dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_74"></a>

##### Examples

```
choose application with prompt "Choose a web browser:"
choose application with multiple selections allowed
choose application as alias
```

##### Discussion

The `choose application` dialog initially presents a list of all applications registered with the system. To choose an application not in that list, use the Browse button, which allows the user to choose an application anywhere in the file system.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW3"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_671"></a>

choose color

Allows the user to choose a color from a color picker dialog.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_75"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW77"></a>`choose color` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW78"></a>`default color` | | *RGB color* | optional |

##### Parameters

`default color` *[RGB color](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW1)*
:   The color to show when the color picker dialog is first opened.

*Default Value:*
:   `{0, 0, 0}`: black.

##### Result

The selected color, represented as a list of three integers from 0 to 65535 corresponding to the red, green, and blue components of a color; for example, {0, 65535, 0} represents green.

Signals a “user canceled” error if the user cancels the `choose color` dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_76"></a>

##### Examples

This example lets the user choose a color, then uses that color to set the background color in their home folder (when it is in icon view):

```
tell application "Finder"
    tell icon view options of window of home
        choose color default color (get background color)
        set background color to the result
    end tell
end tell
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW4"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_673"></a>

choose file

Allows the user to choose a file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_77"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW58"></a>`choose file` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW79"></a>`with prompt` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW80"></a>`of type` | | *list of text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW81"></a>`default location` | | *alias* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW82"></a>`invisibles` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW83"></a>`multiple selections allowed` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW84"></a>`showing package contents` | | *boolean* | optional |

##### Parameters

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The prompt to be displayed in the dialog.

*Default Value:*
:   None; no prompt is displayed.

`of type` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* of *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A list of Uniform Type Identifiers (UTIs); for example, `{"public.html", "public.rtf"}`. Only files of the specified types will be selectable. For a list of system-defined UTIs, see *[Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/../../FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319)*. To get the UTI for a particular file, use `info for`. <a id="//apple_ref/doc/uid/TP40000983-CH216-SW85"></a> **Note:** Four-character file type codes, such as `"PICT"` or `"MooV"`, are also supported, but are deprecated. To get the file type code for a particular file, use `info for`.

*Default Value:*
:   None; any file can be chosen.

`default location` *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)*
:   The folder to begin browsing in.

*Default Value:*
:   Browsing begins in the last selected location, or, if this is the first invocation, in the user’s `Documents` folder.

`invisibles` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Show invisible files and folders?

*Default Value:*
:   `true`: This is only for historical compatibility reasons. Unless you have a specific need to choose invisible files, you should always use `invisibles false`.

`multiple selections allowed` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow multiple items to be selected? If `true`, the results will be returned in a list, even if there is exactly one item.

*Default Value:*
:   `false`

`showing package contents` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Show the contents of packages? If `true`, packages are treated as folders, so that the user can choose a file inside a package (such as an application).

*Default Value:*
:   `false`. Manipulating the contents of packages is discouraged unless you control the package format or the package itself.

##### Result

The selected file, as an `alias`. If multiple selections are allowed, returns a list containing one `alias` for each selected file, if any.

Signals a “user canceled” error if the user cancels the dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_78"></a>

##### Examples

```
set aFile to choose file with prompt "HTML or RTF:" ¬
    of type {"public.html", "public.rtf"} invisibles false
```

A UTI can specify a general class of files, not just a specific format. The following script allows the user to choose any image file, whether its format is `JPEG`, `PNG`, `GIF`, or whatever. It also uses the `default location` parameter combined with `path to (folder)` to begin browsing in the user’s `Pictures` folder:

```
set picturesFolder to path to pictures folder
choose file of type "public.image" with prompt "Choose an image:" ¬
    default location picturesFolder invisibles false
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW5"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_680"></a>

choose file name

Allows the user to specify a new filename and location. This does not create a file—rather, it returns a file specifier that can be used to create a file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_79"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW86"></a>`choose file name` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW87"></a>`with prompt` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW88"></a>`default name` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW89"></a>`default location` | | *alias* | optional |

##### Parameters

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The prompt to be displayed near the top of the dialog.

*Default Value:*
:   `"Specify new file name and location"`

`default name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The default file name.

*Default Value:*
:   `"untitled"`

`default location` *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)*
:   The default file location. See `choose file` for examples.

*Default Value:*
:   Browsing starts in the last location in which a search was made or, if this is the first invocation, in the user’s `Documents` folder.

##### Result

The selected location, as a `file`. For example:

` file "HD:Users:currentUser:Documents:untitled"`

Signals a “user canceled” error if the user cancels the dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_80"></a>

##### Examples

The following example supplies a non-default prompt and search location:

```
set fileName to choose file name with prompt "Save report as:" ¬
default name "Quarterly Report" ¬
default location (path to desktop folder)
```

##### Discussion

If you choose the name of a file or folder that exists in the selected location, `choose file name` offers the choice of replacing the chosen item. However, choosing to replace does not actually replace the item.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW6"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_684"></a>

choose folder

Allows the user to choose a directory, such as a folder or a disk.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_81"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW90"></a>`choose folder` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW91"></a>`with prompt` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW92"></a>`default location` | | *alias* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW93"></a>`invisibles` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW94"></a>`multiple selections allowed` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW95"></a>`showing package contents` | | *boolean* | optional |

##### Parameters

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The prompt to be displayed in the dialog.

*Default Value:*
:   None; no prompt is displayed.

`default location` *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)*
:   The folder to begin browsing in.

*Default Value:*
:   Browsing begins in the last selected location, or, if this is the first invocation, in the user’s `Documents` folder.

`invisibles` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Show invisible folders?

*Default Value:*
:   `false`

`multiple selections allowed` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow multiple items to be selected? If `true`, the results will be returned in a list, even if there is exactly one item.

*Default Value:*
:   `false`

`showing package contents` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Show the contents of packages? If `true`, packages are treated as folders, so that the user can choose a package folder, such as an application, or a folder inside a package.

*Default Value:*
:   `false`. Manipulating the contents of packages is discouraged unless you control the package format or the package itself.

##### Result

The selected directory, as an `alias`. If multiple selections are allowed, returns a list containing one `alias` for each selected directory, if any.

Signals a “user canceled” error if the user cancels the `choose folder` dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_82"></a>

##### Examples

The following example specifies a prompt and allows multiple selections:

```
set foldersList to choose folder ¬
    with prompt "Select as many folders as you like:" ¬
    with multiple selections allowed
```

The following example gets a POSIX path to a chosen folder and uses the `quoted form` property (of the `text` class) to ensure correct quoting of the resulting string for use with shell commands:

```
set folderName to quoted form of POSIX path of (choose folder)
```

Suppose that you choose the folder named `iWork '08` in your `Applications` folder. The previous statement would return the following result, which properly handles the embedded single quote and space characters in the folder name:

```
"'/Applications/iWork '\\\\''08/'"
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW7"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_690"></a>

choose from list

Allows the user to choose items from a list.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_83"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW96"></a>`choose from list` | | *list* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW97"></a>`with title` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW98"></a>`with prompt` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW99"></a>`default items` | | *list* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW100"></a>`OK button name` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW101"></a>`cancel button name` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW102"></a>`multiple selections allowed` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW103"></a>`empty selection allowed` | | *boolean* | optional |

##### Parameters

*[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* (of *[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)* or *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   A list of numbers and/or `text` objects for the user to choose from.

`with title` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   Title text for the dialog.

*Default Value:*
:   None; no title is displayed.

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The prompt to be displayed in the dialog.

*Default Value:*
:   `"Please make your selection:"`

`default items` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* (of *[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)* or *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   A list of numbers and/or `text` objects to be initially selected. The list cannot include multiple items unless you also specify `multiple selections allowed true`. If an item in the default items list is not in the list to choose from, it is ignored.

*Default Value:*
:   None; no items are selected.

`OK button name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of the OK button.

*Default Value:*
:   `"OK"`

`cancel button name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of the Cancel button.

*Default Value:*
:   `"Cancel"`

`multiple selections allowed` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow multiple items to be selected?

*Default Value:*
:   `false`

`empty selection allowed` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow the user to choose OK with no items selected? If `false`, the OK button will not be enabled unless at least one item is selected.

*Default Value:*
:   `false`

##### Result

If the user clicks the OK button, returns a `list` of the chosen `number` and/or `text` items; if empty selection is allowed and nothing is selected, returns an empty list (`{}`). If the user clicks the Cancel button, returns `false`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_84"></a>

##### Examples

This script selects from a list of all the people in Address Book who have defined birthdays, and gets the birthday of the selected one. Notice the `if the result is not false` test (`choose from list` returns `false` if the user clicks Cancel) and the `set aName to item 1 of the result` (`choose from list` returns a list, even if it contains only one item).

```
tell application "Address Book"
    set bDayList to name of every person whose birth date is not missing value
    choose from list bDayList with prompt "Whose birthday would you like?"
    if the result is not false then
        set aName to item 1 of the result
        set theBirthday to birth date of person named aName
        display dialog aName & "'s birthday is " & date string of theBirthday
    end if
end tell
```

##### Discussion

For historical reasons, `choose from list` is the only dialog command that returns a result (`false`) instead of signaling an error when the user presses the “Cancel” button.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW8"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_698"></a>

choose remote application

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_699"></a>Allows the user to choose a running application on a remote machine.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_85"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW104"></a>`choose remote application` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW105"></a>`with title` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW106"></a>`with prompt` | | *text* | optional |

##### Parameters

`with title` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   Title text for the `choose remote application` dialog.

*Default Value:*
:   None; no title is displayed.

`with prompt` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The prompt to be displayed in the dialog.

*Default Value:*
:   `"Select an application:"`

##### Result

The selected application, as an `application` object.

Signals a “user canceled” error if the user cancels the dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_86"></a>

##### Examples

```
set myApp to choose remote application with prompt "Choose a remote web browser:"
```

##### Discussion

The user may choose a remote machine using <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_702"></a>Bonjour or by entering a specific IP address. There is no way to limit the precise kind of application returned, so either limit your script to generic operations or validate the user’s choice. If you want your script to send application-specific commands to the resulting application, you will need a using terms from statement.

For information on targeting other machines, see [Remote Applications](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW9).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW9"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_703"></a>

choose URL

Allows the user to specify a URL.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_87"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW107"></a>`choose URL` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW108"></a>`showing` | | *listOfServiceTypesOrTextStrings* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW109"></a>`editable URL` | | *boolean* | optional |

##### Parameters

`showing` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* (of service types or *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   A list that specifies the types of services to show, if available. The list can contain one or more of the following service types, or one or more `text` objects representing Bonjour service types (described below), or both: * `Web servers`: shows `http` and `https` services * `FTP Servers`: shows `ftp` services * `Telnet hosts`: shows `telnet` services * `File servers`: shows `afp`, `nfs`, and `smb` services * `News servers`: shows `nntp` services * `Directory services`: shows `ldap` services * `Media servers`: shows `rtsp` services * `Remote applications`: shows `eppc` services A `text` object is interpreted as a Bonjour service type—for example, `"_ftp._tcp"` represents the file transfer protocol. These types are listed in [Technical Q&A 1312: Bonjour service types used in OS X](http://developer.apple.com/qa/qa2001/qa1312.html).<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_705"></a>

*Default Value:*
:   `File servers`

`editable URL` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Allow user to type in a URL? If you specify `editable URL false`, the text field in the dialog is inactive. `choose URL` does not attempt to verify that the user-entered text is a valid URL. Your script should be prepared to verify the returned value.

*Default Value:*
:   `true`: the user can enter a text string. If `false`, the user is restricted to choosing an item from the Bonjour-supplied list of services.

##### Result

The URL for the service, as a `text` object. This result may be passed to `open location` or to any application that can handle the URL, such as a browser for `http` URLs.

Signals a “user canceled” error if the user cancels the dialog. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_88"></a>

##### Examples

The following script asks the user to choose an URL, either by typing in the text input field or choosing one of the Bonjour-located servers:

```
set myURL to choose URL
tell application Finder to open location myURL
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW26"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_707"></a>

clipboard info

Returns information about the current clipboard contents.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_89"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW110"></a>`clipboard info` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW111"></a>`for` | | *class* | optional |

##### Parameters

`for` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   Restricts returned information to only this data type.

*Default Value:*
:   None; returns information for all types of data as a list of lists, where each list represents a scrap flavor.

##### Result

A `list` containing one entry `{class, size}` for each type of data on the clipboard. To retrieve the actual data, use the `the clipboard` command.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_90"></a>

##### Examples

```
clipboard info
clipboard info for Unicode text
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW29"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_709"></a>

close access

Closes a file opened with the `open for access` command.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_91"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW112"></a>`close access` | | *fileSpecifier* | required |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* | *file descriptor* )
:   The alias or file specifier or integer file descriptor of the file to close. A file descriptor must be obtained as the result of an earlier `open for access` call.

##### Result

None.

Signals an error if the specified file is not open.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_92"></a>

##### Examples

You should always close files that you open, being sure to account for possible errors while using the open file:

```
set aFile to choose file
set fp to open for access aFile
try
    --file reading and writing here
on error e number n
    --deal with errors here and don't resignal
end
close access fp
```

##### Discussion

Any files left open will be automatically closed when the application exits.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW53"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_710"></a>

copy

Copies one or more values, storing the result in one or more variables. This command only copies AppleScript values, not application-defined objects.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_93"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW113"></a>`copy` | | *expression* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW114"></a>`to` | | *variablePattern* | required |

##### Parameters

*expression*
:   The expression whose value is to be copied.

`to` *variablePattern*
:   The name of the variable or pattern of variables in which to store the value or pattern of values. Patterns may be lists or records.

##### Result

The new copy of the value.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_94"></a>

##### Examples

As mentioned in the Discussion, `copy` creates an independent copy of the original value, and it creates a deep copy. For example:

```
set alpha to {1, 2, {"a", "b"}}
copy alpha to beta
set item 2 of item 3 of alpha to "change" --change the original list
set item 1 of beta to 42 --change a different item in the copy
{alpha, beta}
--result: {{1, 2, {"a", "change"}}, {42, 2, {"a", "b"}}}
```

Each variable reflects only the changes that were made directly to that variable. Compare this with the similar example in `set`.

See the `set` command for examples of using variable patterns. The behavior is the same except that the values are copied.

##### Discussion

The `copy` command may be used to assign new values to existing variables, or to define new variables. See [Declaring Variables with the copy Command](../conceptual/ASLR_variables.md#//apple_ref/doc/uid/TP40000983-CH223-SW8) for additional details.

Using the `copy` command creates a new value that is independent of the original—a subsequent change to that value does not change the original value. The copy is a “deep” copy, so sub-objects, such as lists within lists, are also copied. Contrast this with the behavior of the `set` command.

When using `copy` with an object specifier, the specifier itself is the value copied, not the object in the target application that it refers to. `copy` therefore copies the object specifier, but does not affect the application data at all. To copy the object in the target application, use the application’s `duplicate` command, if it has one.

##### Special Considerations

The syntax `put` *expression* `into` *variablePattern* is also supported, but is deprecated. It will be transformed into the `copy` form when you compile the script.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW55"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_712"></a>

count

Counts the number of elements in another object.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_95"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW115"></a>`(count \| number of)` | | *expression* | required |

##### Parameters

*expression*
:   An expression that evaluates to an object with elements, such as a `list`, `record`, or application-defined container object. `count` will count the contained elements.

##### Result

The number of elements, as an `integer`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_96"></a>

##### Examples

In its simplest form, `count`, or the equivalent pseudo-property `number`, counts the `item` elements of a value. This may be an AppleScript value, such as a list:

```
set aList to {"Yes", "No", 4, 5, 6}
count aList  --result: 5
number of aList  --result: 5
```

…or an application-defined object that has `item` elements:

```
tell application "Finder" to count disk 1  --result: 4
```

If the value is an object specifier that evaluates to a list, `count` counts the items of that list. This may be an [Every](ASLR_reference_forms.md#//apple_ref/doc/uid/TP40000983-CH4g-BBCJFIIH) specifier:

```
count every integer of aList  --result: 3
count words of "hello world"  --result: 2
tell application "Finder" to count folders of disk 1  --result: 4
```

…or a [Filter](ASLR_reference_forms.md#//apple_ref/doc/uid/TP40000983-CH4g-BAJJHEFE) specifier:

```
tell application "Finder"
    count folders of disk 1 whose name starts with "A"  --result: 1
end tell
```

…or similar. For more on object specifiers, see [Object Specifiers](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW7).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW39"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_713"></a>

current date

Returns the current date and time.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_97"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW116"></a>`current date` | |  | required |

##### Result

The current date and time, as a `date` object.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_98"></a>

##### Examples

```
current date  --result: date "Tuesday, November 13, 2007 11:13:29 AM"
```

See the `date` class for information on how to access the properties of a date, such as the day of the week or month.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW10"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_714"></a>

delay

Waits for a specified number of seconds.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_99"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW117"></a>`delay` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW118"></a> | | *number* | optional |

##### Parameters

*[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)*
:   The number of seconds to delay. The number may be fractional, such as `0.5` to delay half a second.

*Default Value:*
:   `0`

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_100"></a>

##### Examples

```
set startTime to current date
delay 3  --delay for three seconds
set elapsedTime to ((current date) - startTime)
display dialog ("Elapsed time: " & elapsedTime & " seconds")
```

##### Discussion

`delay` does not make any guarantees about the actual length of the delay, and it cannot be more precise than 1/60th of a second. `delay` is not suitable for real-time tasks such as audio-video synchronization.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW11"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_715"></a>

display alert

Displays a standardized alert containing a message, explanation, and from one to three buttons.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_101"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW119"></a>`display alert` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW120"></a>`message` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW121"></a>`as` | | *alertType* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW122"></a>`buttons` | | *list* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW123"></a>`default button` | | *buttonSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW124"></a>`cancel button` | | *buttonSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW125"></a>`giving up after` | | *integer* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The alert text, which is displayed in emphasized system font.

`message` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   An explanatory message, which is displayed in small system font, below the alert text.

`as` *alertType*
:   The type of alert to show. You can specify one of the following alert types: * `informational`: the standard alert dialog * `warning`: the alert dialog dialog is badged with a warning icon * `critical`: currently the same as the standard alert dialog

*Default Value:*
:   `informational`

`buttons` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* (of *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   A list of up to three button names. If you supply one name, a button with that name serves as the default and is displayed on the right side of the alert dialog. If you supply two names, two buttons are displayed on the right, with the second serving as the default button. If you supply three names, the first is displayed on the left, and the next two on the right, as in the case with two buttons.

*Default Value:*
:   `{"OK"}`: One button labeled “OK”, which is the default button.

`default button` ( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* or *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* )
:   The name or number of the default button. This may be the same as the cancel button.

*Default Value:*
:   The rightmost button.

`cancel button` ( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* or *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* )
:   The name or number of the cancel button. See “Result” below. This may be the same as the default button.

*Default Value:*
:   None; there is no cancel button.

`giving up after` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The number of seconds to wait before automatically dismissing the alert.

*Default Value:*
:   None; the dialog will wait until the user clicks a button.

##### Result

If the user clicks a button that was not specified as the cancel button, `display alert` returns a record that identifies the button that was clicked—for example, `{button returned: "OK"}`. If the command specifies a `giving up after` value, the record will also contain a `gave up:false` item.

If the `display alert` command specifies a `giving up after` value, and the dialog is dismissed due to timing out before the user clicks a button, the command returns a record indicating that no button was returned and the command gave up: `{button returned:"", gave up:true}`

If the user clicks the specified cancel button, the command signals a “user canceled” error. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_102"></a>

##### Examples

```
set alertResult to display alert "Insert generic warning here." ¬
    buttons {"Cancel", "OK"} as warning ¬
    default button "Cancel" cancel button "Cancel" giving up after 5
```

For an additional example, see the Examples section for the `try` statement.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW12"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_722"></a>

display dialog

Displays a dialog containing a message, one to three buttons, and optionally an icon and a ﬁeld in which the user can enter text.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_103"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW126"></a>`display dialog` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW127"></a>`default answer` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW128"></a>`hidden answer` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW129"></a>`buttons` | | *list* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW130"></a>`default button` | | *labelSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW131"></a>`cancel button` | | *labelSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW132"></a>`with title` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW133"></a>`with icon` | | *resourceSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW134"></a>`with icon` | | *iconTypeSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW135"></a>`with icon` | | *fileSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW136"></a>`giving up after` | | *integer* | optional |

##### Parameters

*text*
:   The dialog text, which is displayed in emphasized system font.

`default answer` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The initial contents of an editable text field. This edit field is not present unless this parameter is present; to have the field present but blank, specify an empty string: `default answer ""`

*Default Value:*
:   None; there is no edit field.

`hidden answer` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   If true, any text in the edit field is obscured as in a password dialog: each character is displayed as a bullet.

*Default Value:*
:   `false`: text in the edit field is shown in cleartext.

`buttons` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* (of *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   A list of up to three button names.

*Default Value:*
:   If you don’t specify any buttons, by default, Cancel and OK buttons are shown, with the OK button set as the default button. If you specify any buttons, there is no default or cancel button unless you use the following parameters to specify them.

`default button` ( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* | *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* )
:   The name or number of the default button. This button is highlighted, and will be pressed if the user presses the Return or Enter key.

*Default Value:*
:   If there are no buttons specified using `buttons`, the OK button. Otherwise, there is no default button.

`cancel button` ( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* | *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* )
:   The name or number of the cancel button. This button will be pressed if the user presses the Escape key or Command-period.

*Default Value:*
:   If there are no buttons specified using `buttons`, the Cancel button. Otherwise, there is no cancel button.

`with title` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The dialog window title.

*Default Value:*
:   None; no title is displayed.

`with icon` ( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* | *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* )
:   The resource name or ID of the icon to display.

`with icon` ( *stop | note | caution* )
:   The type of icon to show. You may specify one of the following constants: * `stop` (or `0`): Shows a stop icon * `note` (or `1`): Shows the application icon * `caution` (or `2`): Shows a warning icon, badged with the application icon

`with icon` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies a `.icns` file.

`giving up after` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The number of seconds to wait before automatically dismissing the dialog.

*Default Value:*
:   None; the dialog will wait until the user presses a button.

##### Result

A record containing the button clicked and text entered, if any. For example:

`{text returned:"Cupertino", button returned:"OK"}`

If the dialog does not allow text input, there is no `text returned` item in the returned record.

If the user clicks the specified cancel button, the command signals a “user canceled” error. For an example of how to handle such errors, see [try Statements](ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973).

If the `display dialog` command specifies a `giving up after` value, and the dialog is dismissed due to timing out before the user clicks a button, it returns a record indicating that no button was returned and the command gave up: `{button returned:"", gave up:true}`

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_104"></a>

##### Examples

The following example shows how to use many of the parameters to a `display dialog` command, how to process possible returned values, and one way to handle a user cancelled error. The dialog displays two buttons and prompts a user to enter a name, giving up if they do not make a response within fifteen seconds. It shows one way to handle the case where the user cancels the dialog, which results in AppleScript signaling an “error” with the error number -128. The script uses additional `display dialog` commands to show the flow of logic and indicate where you could add statements to handle particular outcomes.

```
set userCanceled to false
try
    set dialogResult to display dialog ¬
        "What is your name?" buttons {"Cancel", "OK"} ¬
        default button "OK" cancel button "Cancel" ¬
        giving up after 15 ¬
        default answer (long user name of (system info))
on error number -128
    set userCanceled to true
end try
 
if userCanceled then
    -- statements to execute when user cancels
    display dialog "User cancelled."
else if gave up of dialogResult then
    -- statements to execute if dialog timed out without an answer
    display dialog "User timed out."
else if button returned of dialogResult is "OK" then
    set userName to text returned of dialogResult
    -- statements to process user name
    display dialog "User name: " & userName
end if
end
```

The following example displays a dialog that asks for a password. It supplies a default answer of `"wrong"`, and specifies that the default answer, as well as any text entered by the user, is hidden (displayed as a series of bullets). It gives the user up to three chances to enter a correct password.

```
set prompt to "Please enter password:"
repeat 3 times
    set dialogResult to display dialog prompt ¬
        buttons {"Cancel", "OK"} default button 2 ¬
        default answer "wrong" with icon 1 with hidden answer
    set thePassword to text returned of dialogResult
    if thePassword = "magic" then
        exit repeat
    end if
end repeat
if thePassword = "magic" or thePassword = "admin" then
    display dialog "User entered valid password."
end if
```

The password text is copied from the return value `dialogResult`. The script doesn’t check for a user cancelled error, so if the user cancels AppleScript stops execution of the script.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW224"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_733"></a>

display notification

Posts a notification using the Notification Center, containing a title, subtitle, and explanation, and optionally playing a sound.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_105"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW225"></a>`display notification` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW226"></a>`with title` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW227"></a>`subtitle` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW228"></a>`sound name` | | *text* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The body text of the notification. At least one of this and the title must be specified.

`with title` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The title of the notification. At least one of this and the body text must be specified.

`subtitle` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The subtitle of the notification.

`sound name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of a sound to play when the notification appears. This may be the base name of any sound installed in `Library/Sounds`.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_106"></a>

##### Examples

```
display notification "Encoding complete" subtitle "The encoded files are in the folder " & folderName
```

##### Discussion

Exactly how the notification is presented is controlled by the “Notifications” preferences in System Preferences. Users may opt to display a reduced form of notification, turn off the sound, or even not display them at all.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW40"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_737"></a>

do shell script

Executes a shell script using the `sh` shell.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_107"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW137"></a>`do shell script` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW138"></a>`as` | | *class* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW139"></a>`administrator privileges` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW140"></a>`user name` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW141"></a>`password` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW142"></a>`altering line endings` | | *boolean* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The shell script to execute.

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   Specifies the desired type of the result. The raw bytes returned by the command will be interpreted as the specified class.

*Default Value:*
:   `«class utf8»`: UTF-8 text. If there is no *as* parameter and the output is not valid UTF-8, the output will be interpreted as text in the primary encoding.

`administrator privileges` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Execute the command as the administrator? Once a script is correctly authenticated, it will not ask for authentication again for five minutes. The elevated privileges and the grace period do not extend to any other scripts or to the rest of the system. For security reasons, you may not tell another application to `do shell script with administrator privileges`. Put the command outside of any `tell` block, or put it inside a `tell me` block.

*Default Value:*
:   `false`

`user name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of an administrator account. You can avoid a password dialog by specifying a name in this parameter and a password in the `password` parameter. If you specify a user name, you must also specify a password.

`password` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   An administrator password, typically used in conjunction with the administrator specified by the `user name` parameter. If `user name` is omitted, it is assumed to be the current user.

`altering line endings` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Should the `do shell script` command change all line endings in the command output to Mac-style and trim a trailing one? For example, the result of `do shell script "echo foo; echo bar"` is `"foo\\rbar"`, not the `"foo\\nbar\\n"` that the shell script actually returned.

*Default Value:*
:   `true`

##### Result

The output of the shell script.

Signals an error if the shell script exits with a non-zero status. The error number will be the status, the error message will be the contents of stderr.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_108"></a>

##### Examples

```
do shell script "uptime"
```

##### Discussion

For additional documentation and examples of the `do shell script` command, see Technical Note TN2065, [do shell script in AppleScript](http://developer.apple.com/technotes/tn2002/tn2065.html).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW56"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_743"></a>

get

Evaluates an object specifier and returns the result.

The command name `get` is typically optional—expressions that appear as statements or operands are automatically evaluated as if they were preceded by `get`. However, `get` can be used to force early evaluation of part of an object specifier.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_109"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW143"></a>`get` | | *specifier* | required |
|  | `as` | *class* | optional |

##### Parameters

*specifier*
:   An object specifier to be evaluated. If the specifier refers to an application-defined object, the `get` command is sent to that application. Technically, all values respond to `get`, but for all values other than object specifiers, `get` is an identity operation: the result is the exact same value.

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   The desired class for the returned data. If the data is not of the desired type, AppleScript attempts to coerce it to that type.

*Default Value:*
:   None; no coercion is performed.

##### Result

The value of the evaluated expression. See [Reference Forms](ASLR_reference_forms.md#//apple_ref/doc/uid/TP40000983-CH4g-120522) for details on what the results of evaluating various object specifiers are.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_110"></a>

##### Examples

`get` can get properties or elements of AppleScript-defined objects, such as lists:

```
get item 1 of {"How", "are", "you?"}  --result: "How"
```

…or of application-defined objects:

```
tell application "Finder" to get name of home  --result: "myname"
```

As noted above, the `get` is generally optional. For example, these statements are equivalent to the above two:

```
item 1 of {"How", "are", "you?"}  --result: "How"
tell application "Finder" to name of home  --result: "myname"
```

However, an explicit `get` can be useful for forcing early evaluation of part of an object specifier. Consider:

```
tell application "Finder" to get word 1 of name of home
--Finder got an error: Can’t get word 1 of name of folder "myname" of folder "Users" of startup disk.
```

This fails because Finder does not know about elements of `text`, such as `words`. AppleScript does, however, so the script has to make Finder get only the `name of ...` part:

```
tell application "Finder" to get word 1 of (get name of home)
--result: "myname"
```

The explicit `get` forces that part of the specifier to be evaluated; Finder returns a `text` result, from which AppleScript can then get `word 1`.

For more information on specifiers, see [Object Specifiers](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW7).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW30"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_745"></a>

get eof

Returns the length of a file, in bytes.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_111"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW63"></a>`get eof` | | *fileSpecifier* | required |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* | *file descriptor* )
:   The file to obtain the length for, as an alias, a file specifier, or an `integer` file descriptor. A file descriptor must be obtained as the result of an earlier `open for access` call.

##### Result

The logical size of the file, that is, the length of its contents in bytes.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_112"></a>

##### Examples

This example obtains an alias to a desktop picture folder and uses `get eof` to obtain its length:

```
set desktopPicturesFolderPath to ¬
     (path to desktop pictures folder as text) & "Flow 1.jpg" as alias
--result: alias "Leopard:Library:Desktop Pictures:Flow 1.jpg"
get eof desktopPicturesFolderPath --result: 531486
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW41"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_746"></a>

get volume settings

Returns the sound output and input volume settings.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_113"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW144"></a>`get volume settings` | |  | required |

##### Result

A record containing the sound output and input volume settings. All the integer settings are between 0 (silent) and 100 (full volume):

`output volume` (an `integer` )
:   The base output volume.

`input volume` (an `integer` )
:   The input volume.

`alert volume` (an `integer` )
:   The alert volume. 100 for this setting means “as loud as the output volume.”

`output muted` (a `boolean` )
:   Is the output muted? If true, this overrides the output and alert volumes.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_114"></a>

##### Examples

```
set volSettings to get volume settings
--result: {output volume:43, input volume:35, alert volume:78, output muted:false}
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW14"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_747"></a>

info for

Return information for a file or folder.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_115"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW65"></a>`info for` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW145"></a>`size` | | *boolean* | optional |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An alias or file specifier for the file or folder.

`size` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Return the size of the file or folder? For a file, its “size” is its length in bytes; for a folder, it is the sum of the sizes of all the files the folder contains.

*Default Value:*
:   `true`: Because getting the size of a folder requires getting the sizes of all the files inside it, `size true` may take a long time for large folders such as `/System`. If you do not need the size, ask to not get it using `size false`. Alternatively, target the Finder or System Events applications to ask for the specific properties you want.

##### Result

A record containing information about the specified file or folder, with the following fields. Some fields are only present for certain kinds of items:

`name` (a `text` object)
:   The item’s full name, as it appears in the file system. This always includes the extension, if any. For example, `"OmniOutliner Professional.app"`.

`displayed name` (a `text` object)
:   The item’s name as it appears in Finder. This may be different than the `name` if the extension is hidden or if the item has a localized name. For example, `"OmniOutliner Professional"`.

`short name` ( a `text` object, applications only)
:   The application’s `CFBundleName`, which is the name displayed in the menu bar when the application is active. This is often, but not always, the same as the displayed name. For example, `"OmniOutliner Pro"`.

`name extension` (a `text` object)
:   The extension part of the item name. For example, the name extension of the file “`foo.txt`” is `"txt"`.

`bundle identifier` (a `text` object)
:   The package’s bundle identifier. If the package is an application, this is the application’s `id`.

`type identifier` (a `text` object)
:   The item’s type, as a Uniform Type Identifier (UTI). This is the preferred form for identifying item types, and may be used with `choose file`.

`kind` (a `text` object)
:   The item’s type, as displayed in Finder. This may be localized, and should only be used for display purposes.

`default application` (an `alias` object)
:   The application that will open this item.

`creation date` (a `date` object)
:   The date the item was created.

`modification date` (a `date` object)
:   The date the item was last modified. Folder modification dates do not change when an item inside them changes, though they do change when an item is added or removed.

`file type` (a `text` object)
:   The item’s type, as a four-character code. This is the classic equivalent of the type identifier, but less accurate and harder to interpret; use `type identifier` if possible.

`file creator` (a `text` object)
:   The item’s four-character creator code. For applications, this is the classic equivalent of the bundle identifier, and will work for referencing an application by id. For files, this can be used to infer the default application, but not reliably; use `default application` if possible.

`short version` (a `text` object)
:   The item’s short version string, as it appears in a Finder “Get Info” window. Any item may have this attribute, but typically only applications do.

`long version` (a `text` object)
:   The item’s long version string, as it appears in a Finder “Get Info” window. Any item may have this attribute, but typically only applications do.

`size` (an `integer` )
:   The item’s size, in bytes. For more details, see the `size` parameter.

`alias` (a `boolean` )
:   Is the item an alias file?

`folder` (a `boolean` )
:   Is the item a folder? This is true for packages, such as application packages, as well as normal folders.

`package folder` (a `boolean` )
:   Is the item a package folder, such as an application? A package folder appears in Finder as if it is a file.

`extension hidden` (a `boolean` )
:   Is the item’s name extension hidden?

`visible` (a `boolean` )
:   Is the item visible? Typically, only special system files are invisible.

`locked` (a `boolean` )
:   Is the item locked?

`busy status` (a `boolean` )
:   Is the item currently in use? If `true`, the item is reliably busy. If `false`, the item may still be busy, because this status may not be supported by some applications or file systems.

`folder window` (rectangle, folders only)
:   The folder’s window’s bounding rectangle, as list of four integers: {top, left, bottom, right}.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_116"></a>

##### Examples

```
set downloadsFolder to path to downloads folder
    --result: alias "HD:Users:me:Downloads:"
info for downloadsFolder
    --result: {name:"Downloads", folder:true, alias:false, ...}
```

##### Special Considerations

Because `info for` returns so much information, it can be slow, and because it only works on one file at a time, it can be difficult to use. The recommended technique is to use System Events or Finder to ask for the particular properties you want.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW51"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_749"></a>

launch

Launches an application, if it is not already running, but does not send it a `run` command.

If an application is already running, sending it a `launch` command has no effect. That allows you to open an application without performing its usual startup procedures, such as opening a new window or, in the case of a script application, running its script. For example, you can use the `launch` command when you don’t want an application to open and close visibly. This is less useful in AppleScript 2.0, which launches applications as hidden by default (even with the `run` command).

See the `application` class reference for information on how to use an `application` object’s `is running` property to determine if it is running without having to launch it.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_117"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW146"></a>`launch` | | *application* | required |

##### Parameters

*application*
:   The application to launch.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_118"></a>

##### Examples

```
launch application "TextEdit"
tell application "TextEdit" to launch
```

##### Discussion

The `launch` command does not launch applications on remote machines. For examples of other ways to specify an application, see the `application` class.

Many applications also support the `reopen` <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_750"></a>command, which reactivates a running application or launches it if it isn’t running. If the application is already running, this command has the same effect as double-clicking the application icon in the Finder. Each application determines how it will implement the `reopen` command—some may perform their usual startup procedures, such as opening a new window, while others perform no additional operations.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW15"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_751"></a>

list disks

Returns the names of the currently mounted volumes.

> <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_119"></a>
>
> **Important:** This command is deprecated; use `tell application "System Events" to get the name of every disk`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_120"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW147"></a>`list disks` | |  | required |

##### Result

A `list` of text objects, one for each currently mounted volume.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW16"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_752"></a>

list folder

Returns the names of the items in a specified folder.

> <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_121"></a>
>
> **Important:** This command is deprecated; use `tell application "System Events" to get the name of every disk item of ...`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_122"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW148"></a>`list folder` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW149"></a>`invisibles` | | *boolean* | optional |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   Specifies the folder to list.

`invisibles` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Show invisible files and folders?

*Default Value:*
:   `true`

##### Result

A `list` of `text` objects, one for each item in the specified folder.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW35"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_754"></a>

load script

Returns a `script` object loaded from a specified file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_123"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW150"></a>`load script` | | *fileSpecifier* | required |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies a `script` object. The file must be a compiled script (with extension `scpt`) or script bundle (with extension `scptd`).

##### Result

The `script` object. You can get this object’s properties or call its handlers as if it were a local `script` object.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_124"></a>

##### Examples

For examples, see [Parameter Specifications](../conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-SW12) in [About Handlers](../conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-CJBIDBJH).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW23"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_755"></a>

localized string

Returns the localized text for the specified key.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_125"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW151"></a>`localized string` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW152"></a>`from table` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW219"></a>`in bundle` | | *fileSpecifier* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The key for which to obtain the localized text.

`from table` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of the strings file excluding the `.strings` suffix.

*Default Value:*
:   `"Localizable"`

`in bundle` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies the strings file.

*Default Value:*
:   The current script bundle for a document-based script (a `scptd` bundle); otherwise, the current application.

##### Result

A `text` object containing the localized text, or the original key if there is no localized text for that key.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_126"></a>

##### Examples

In order for `localized string` to be useful, you must create localized string data for it to use:

1. Save your script as an application bundle or script bundle.
2. Create `lproj` folders in the `Resources` directory of the bundle for each localization: for example, `English.lproj`, `French.lproj`. Create files named `Localized.strings` in each one. When you are done, the folder structure should look like this:

   <a id="//apple_ref/doc/uid/TP40000983-CH216-SW48"></a>

   **Figure 7-1**  Bundle structure with localized string data

   ![Bundle structure with localized string data](https://developer.apple.com/library/archive/applescript-language-guide/Art/localizedStringLayout_2x.png)
3. Add key/value pairs to each Localized.strings file. Each pair is a line of text `"`*key*`" = "`*value*`";`, for example:

   <a id="//apple_ref/doc/uid/TP40000983-CH216-SW218"></a>

   **Figure 7-2**  Key/value pair for localized string data

   ![Key/value pair for localized string data](https://developer.apple.com/library/archive/applescript-language-guide/Art/localizableStringData_2x.png)

Now `localized string` will return the appropriate values, as defined in your files. For example, when running in French:

```
localized string "hello"  --result: "bonjour"
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW49"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_758"></a>

log

In Script Editor, displays a value in the Event Log History window or in the Event Log pane of a script window.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_127"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW220"></a>`log` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW221"></a> | | *value* | optional |

##### Parameters

*value*
:   The value to display. Expressions are evaluated but object specifiers are not resolved. The displayed value is enclosed in block comment characters—for example, `(*window 1*)`. If you do not specify a value, `log` will display just the comment characters: `(**)`.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_128"></a>

##### Examples

The following shows a simple use of logging:

```
set area to 7 * 43 as square feet
log area -- result (in Event Log pane): (*square feet 301.0*)
```

Log statements can be useful for tracking a script’s progress. For an example that shows how to log statements in a repeat loop, see [Logging](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW17).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW17"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_759"></a>

mount volume

Mounts the specified network volume.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_129"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW153"></a>`mount volume` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW154"></a>`on server` | | *text* | (see parameter description) |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW155"></a>`in AppleTalk zone` | | *text* | (see parameter description) |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW156"></a>`as user name` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW157"></a>`with password` | | *text* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name or URL (for example, `afp://server/volume/`) of the volume to mount.

`on server` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The server on which the volume resides; omit if URL path provided in direct parameter.

`in AppleTalk zone` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The AppleTalk zone in which the server resides; omit if URL path provided.

`as user name` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The user name with which to log in to the server; omit for guest access.

`with password` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The password for the user name; omit for guest access.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_130"></a>

##### Examples

```
mount volume "afp://myserver.com/" -- guest access
mount volume "http://idisk.mac.com/myname/Public"
mount volume "http://idisk.mac.com/somebody" ¬
    as user name "myname" with password "mypassword"
```

##### Discussion

The `mount volume` command can connect to any file server that is supported by the Finder Connect To... command, including Windows (smb), Samba, and FTP servers. On some kinds of servers, the `as user name` and `with password` parameters may not bypass the login dialog, but encoding the name and password in the URL (for example, `smb://myname:passwd@server.domain.com/sharename`) will mount it silently.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW24"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_764"></a>

offset

Finds one piece of text inside another.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_131"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW158"></a>`offset` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW159"></a>`of` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW160"></a>`in` | | *text* | required |

##### Parameters

`of` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The source text to find the position of.

`in` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The target text to search in.

##### Result

An `integer` value indicating the position, in characters, of the source text in the target, or 0 if not found.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_132"></a>

##### Examples

```
set myString to "Yours, mine, and ours"
offset of "yours" in myString  --result: 1, because case is ignored by default
offset of "mine" in myString  --result: 8
offset of "theirs" in myString  --result: 0, because "theirs" doesn't appear
considering case
    offset of "yours" in myString -- result: 0, because case is now considered
end considering
```

##### Discussion

`offset` compares text as the `equals` operator does, including `considering` and `ignoring` conditions. The values returned are counted the same way `character` elements of `text` are counted—for example, `offset of "c" in "école"` is always `2`, regardless of whether `"école"` is in Normalization Form C or D. The result of matching part of a character cluster is undefined.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW31"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_767"></a>

open for access

Opens a file for reading and writing.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_133"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW62"></a>`open for access` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW161"></a>`write permission` | | *boolean* | optional |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies the file to open. You can only use an alias if the file exists.

`write permission` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Should writing to the file be allowed?

*Default Value:*
:   `false`: `write` and `set eof` commands on this file will fail with an error.

##### Result

A file descriptor, as an `integer`. This file descriptor may be used with any of the other file commands: `read`, `write`, `get eof`, `set eof`, and `close access`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_134"></a>

##### Examples

The following example opens a file named "NewFile" in the specified location `path to desktop`, but does not ask for write access:

```
set theFile to (path to desktop as text) & "NewFile"
set referenceNumber to open for access theFile
```

To open the file with write access, you would substitute the following line:

```
set referenceNumber to open for access theFile with write permission
```

##### Discussion

Opening a file using `open for access` is not the same as opening a file using Finder. It is “open” only in the sense that AppleScript has access to read (and optionally write) its contents; it does not appear in one of the target application’s windows, and it does not even have to be one of the target application’s files. `open for access` and the associated file commands (`read`, `write`, `get eof`, `set eof`) are typically used with text files. They can also read and write arbitrary binary data, but this is not recommended unless you create the file yourself or have detailed knowledge of the file format.

Calling `open for access` on a file returns an integer, termed a *file descriptor*, which represents an open communication channel to the file’s data. This file descriptor remains open until the script calls `close access` on it (or on the same file). Each file descriptor maintains a *file pointer*, which marks the current position within the file and is initially set to the beginning of the file. `read` and `write` commands begin reading or writing at the file pointer, unless instructed otherwise using a `from` or `starting at` parameter, and advance the file pointer by the number of bytes read or written, so the next operation will begin where the previous one left off.

A single file may be opened more than once, and therefore have several different file descriptors. Each file descriptor maintains its own file pointer, and each must be closed separately. If you open more than one channel at once with write permission, behavior is unspecified.

It is not strictly necessary to use `open for access`—all the other file commands can accept an alias; if the file is not open, they will open it, do the operation, and then close it. Explicitly opening and closing the file does have two potential advantages, however.

One is performance: if you are performing a number of operations on the same file, opening and closing it repeatedly could become expensive. It is cheaper to explicitly open the file, do the work, and then explicitly close it.

Two is ease of sequential read and write operations: because the file pointer tracks the progress through the file, reading or writing several pieces of data from the same file is a simple matter. Doing the same thing without using the file pointer requires calculating the data size yourself, which is not even possible in some cases.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW54"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_769"></a>

open location

Opens a URL with the appropriate program.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_135"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW61"></a>`open location` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW162"></a>`error reporting` | | *boolean* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The URL to open.

`error reporting` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   This parameter exists only for historical reasons; it is no longer supported.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_136"></a>

##### Examples

This example opens an Apple web page:

```
open location "http://www.apple.com"
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW18"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_771"></a>

path to (application)

Returns the location of the specified application.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_137"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW66"></a>`path to` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW163"></a> | | *application* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW164"></a>`as` | | *class* | optional |

##### Parameters

*application*
:   The application to locate. See the `application` class reference for possible ways to specify an application. You may also use one of the following identifiers: `current application` : The application executing the script, such as Script Editor. `frontmost application` : The frontmost application. `me` : The script itself. For script applications, this is the same as `current application`, but for script documents, it is the location of the document. <a id="//apple_ref/doc/uid/TP40000983-CH216-SW165"></a> **Note:** Some older applications may treat `me` identically to `current application`. `it` : The application of the current target.

*Default Value:*
:   `it`

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)* ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   The class of the returned location. If specified, must be one of `alias` or `text`.

*Default Value:*
:   `alias`

##### Result

The location of the specified application, as either an `alias` or a `text` object containing the path.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_138"></a>

##### Examples

```
path to application "TextEdit"
    --result: alias "Leopard:Applications:TextEdit.app:"
path to  --result: alias "Leopard:Applications:AppleScript:Script Editor.app:"
path to me  --result: same as above
path to it  --result: same as above
path to frontmost application  --result: same as above
path to current application
    --result: same, but could be different for a script application
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW19"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_773"></a>

path to (folder)

Returns the location of the specified special folder.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_139"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW166"></a>`path to` | | *folder constant* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW167"></a>`from` | | *domain constant* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW168"></a>`as` | | *class* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW169"></a>`folder creation` | | *boolean* | optional |

##### Parameters

*folder constant*
:   The special folder for which to return the path. You may specify one of the following folders: ``` application support applications folder desktop desktop pictures folder documents folder downloads folder favorites folder Folder Action scripts fonts help home folder internet plugins keychain folder library folder modem scripts movies folder music folder pictures folder preferences printer descriptions public folder scripting additions scripts folder services folder shared documents shared libraries sites folder startup disk startup items system folder system preferences temporary items trash users folder utilities folder workflows folder ``` The following folders are also defined, but are only meaningful when used with `from Classic domain`: ``` apple menu control panels control strip modules extensions launcher items folder printer drivers printmonitor shutdown folder speakable items stationery voices ```

`from` *domain constant*
:   The domain in which to look for the specified folder. You may specify one of the following domains: `system domain` : A folder in `/System`. `local domain` : A folder in `/Library`. `network domain` : A folder in `/Network`. `user domain` : A folder in `~`, the user’s home folder. `Classic domain` : A folder in the Classic Mac OS system folder. Only meaningful on systems that support Classic.

*Default Value:*
:   The default domain for the specified folder. This varies depending on the folder.

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)* ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* )
:   The class of the returned location.

*Default Value:*
:   `alias`

`folder creation` *boolean*
:   Create the folder if it doesn’t exist? Your script may not have permission to create the folder (for example, asking to create something in the system domain), so your script should be prepared for that error.

*Default Value:*
:   `true`

##### Result

The location of the specified folder, as either an `alias` or a `text` object containing the path.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_140"></a>

##### Examples

```
path to desktop --result: alias "Leopard:Users:johndoe:Desktop:"
path to desktop as string --result: "Leopard:Users:johndoe:Desktop:"
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW20"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_777"></a>

path to resource

Returns the location of the specified resource.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_141"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW170"></a>`path to resource` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW171"></a>`in bundle` | | *fileSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW172"></a>`in directory` | | *text* | optional |

##### Parameters

*text*
:   The name of the requested resource.

`in bundle` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies the bundle containing the resource.

*Default Value:*
:   The current script bundle for a document-based script (a `scptd` bundle); otherwise, the current application.

`in directory` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The name of a subdirectory in the bundle’s `Resources` directory.

##### Result

The location of the specified resource, as an `alias`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_142"></a>

##### Examples

The following example shows how you can get the path to a `.icns` file—in this case, in the Finder application.

```
tell application "Finder"
set gearIconPath to path to resource "Gear.icns"
end
--result: alias "HD:System:Library:CoreServices:Finder.app:Contents:Resources:Gear.icns"
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW42"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_780"></a>

random number

Returns a random number.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_143"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW173"></a>`random number` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW174"></a>`from` | | *number* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW175"></a>`to` | | *number* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW176"></a>`with seed` | | *number* | optional |

##### Parameters

`from` *[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)*
:   The lowest number to return. Can be negative.

*Default Value:*
:   0.0

`to` *[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)*
:   The highest number to return. Can be negative.

*Default Value:*
:   1.0

`with seed` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   An initial seed for the random number generator. Once called with any particular seed value, `random number` will always generate the same sequence of numbers. This can be useful when testing randomized algorithms: you can force it to behave the same way every time.

##### Result

A number between the `from` and `to` limits, including the limit values. Depending on the limit values, the result may be an integer or a real. If at least one limit is specified, and all specified limits are integers, the result is an integer. Otherwise, the result is a real, and may have a fractional part.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_144"></a>

##### Examples

```
random number  --result: 0.639215561057
random number from 1 to 10  --result: 8
```

##### Discussion

Random numbers are, by definition, random, which means that you may get the same number twice (or even more) in a row, especially if the range of possible numbers is small.

The numbers generated are only pseudo-random, and are not considered cryptographically secure.

If you need to select one of a set of objects in a relationship, use `some` *object* rather than *object* `(random number from 1 to count` *objects*`)`. See the [Arbitrary](ASLR_reference_forms.md#//apple_ref/doc/uid/TP40000983-CH4g-BCIJEEHE) reference form for more details.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW32"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_784"></a>

read

Reads data from a file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_145"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW177"></a>`read` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW178"></a>`from` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW179"></a>`for` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW180"></a>`to` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW181"></a>`before` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW182"></a>`until` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW183"></a>`using delimiters` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW184"></a>`as` | | *class* | optional |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* | *file descriptor* )
:   The file to read from, as an alias, a file specifier, or an `integer` file descriptor. A file descriptor must be obtained as the result of an earlier `open for access` call.

`from` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The byte position in the file to start reading from. The position is 1-based, so `1` is the first byte of the file, `2` the second, and so on. Negative integers count from the end of the file, so `-1` is the last byte, `-2` the second-to-last, and so on.

*Default Value:*
:   The current file pointer (see `open for access`) if the file is open, or the beginning of the file if not.

`for` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The number of bytes to read.

*Default Value:*
:   Read until the end of the file.

`to` ( *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* | *eof* )
:   Stop reading at this byte position in the file; use `eof` to indicate the last byte. The position is 1-based, like the `from` parameter.

`before` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A single character; read up to the next occurrence of that character. The *before* character is also read, but is not part of the result, so the next `read` will start just after it.

`until` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A single character; read up to and including the next occurrence of that character.

`using delimiter` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   A delimiter, such as a tab or return character, used to separate the data read into a list of text objects. The resulting items consist of the text between occurrences of the delimiter text. The delimiter is considered a separator, so a leading or trailing delimiter will produce an empty string on the other side. For example, the result of reading `"axbxcx"` using a delimiter of `"x"` would be `{"a", "b", "c", ""}`.

*Default Value:*
:   None; `read` returns a single item.

`using delimiters` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* of *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   As `using delimiter` above, but all of the strings in the list count as delimiters.

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   Interpret the raw bytes read as this class. The most common ones control the use of three different text encodings: `text` or `string` : The primary text encoding, as determined by the user’s language preferences set in the International preference panel. (For example, Mac OS Roman for English, MacJapanese for Japanese, and so on.) `Unicode text` : UTF-16. `«class utf8»` : UTF-8. (See [Double Angle Brackets](../conceptual/ASLR_raw_data.md#//apple_ref/doc/uid/TP40000983-CH225-SW1) for information on chevron or “raw” syntax.) Any other class is possible, for example `date` or `list`, but is typically only useful if the data was written using a `write` statement specifying the same value for the `as` parameter.

*Default Value:*
:   `text`

##### Result

The data read from the file. If the file is open, the file pointer is advanced by the number of bytes read, so the next `read` command will start where the previous one left off.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_146"></a>

##### Examples

The following example opens a file for read access, reads up to (and including) the first occurrence of `"."`, closes the file, and displays the text it read. (See the Examples section for the `write` command for how to create a similar file for reading.)

```
set fp to open for access file "Leopard:Users:myUser:NewFile"
set myText to read fp until "."
close access fp
display dialog myText
```

To read all the text in the file, replace `set myText to read fp until "."` with `set myText to read fp`.

##### Discussion

At most one of `to`, `for`, `before`, and `until` is allowed. Use of `before`, `until`, or `using delimiter(s)` will interpret the file first as text and then coerce the text to whatever is specified in the `as` parameter. Otherwise, it is treated as binary data (which may be interpreted as text if so specified.)

`read` cannot automatically detect the encoding used for a text file. If a file is not in the primary encoding, you must supply an appropriate `as` parameter.

When reading binary data, `read` always uses big-endian byte order. This is only a concern if you are reading binary files produced by other applications.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW43"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_793"></a>

round

Rounds a number to an integer.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_147"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW185"></a>`round` | | *real* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW186"></a>`rounding` | | *roundingDirection* | optional |

##### Parameters

*[real](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCJECEC)*
:   The number to round.

`rounding` *roundingDirection*
:   The direction to round. You may specify one of the following rounding directions: `up` : Rounds to the next largest integer. This is the same as the math “ceiling” function. `down` : Rounds down to the next smallest integer. This is the same as the math “floor” function. `toward zero` : Rounds toward zero, discarding any fractional part. Also known as truncation. `to nearest` : Rounds to the nearest integer; .5 cases are rounded to the nearest even integer. For example, 1.5 rounds to 2, 0.5 rounds to 0. Also known as “unbiased rounding” or “bankers’ rounding.” See Discussion for details. `as taught in school` : Rounds to the nearest integer; .5 cases are rounded away from zero. This matches the rules commonly taught in elementary mathematics classes.

*Default Value:*
:   `to nearest`

##### Result

The rounded value, as an `integer` if it is within the allowable range (±2^29), or as a `real` if not.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_148"></a>

##### Examples

Rounding up or down is not the same as rounding away from or toward zero, though it may appear so for positive numbers. For example:

```
round 1.1 rounding down --result: 1
round -1.1 rounding down --result: -2
```

To round to the nearest multiple of something other than 1, divide by that number first, round, and then multiply. For example, to round a number to the nearest 0.01:

```
set x to 5.1234
set quantum to 0.01
(round x/quantum) * quantum --result: 5.12
```

##### Discussion

The definition of `to nearest` is more accurate than `as taught in school`, but may be surprising if you have not seen it before. For example:

```
round 1.5 --result: 2
round 0.5 --result: 0
```

Rounding 1.5 to 2 should come as no surprise, but `as taught in school` would have rounded 0.5 up to 1. The problem is that when dealing with large data sets or with many subsequent rounding operations, always rounding up introduces a slight upward skew in the results. The round-to-even rule used by `to nearest` tends to reduce the total rounding error, because on average an equal portion of numbers will round down as will round up.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW57"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_795"></a>

run

Executes the `run` handler of the specified target.

To run an application, it must be on a local or mounted volume. If the application is already running, the effect of the `run` command depends on the application. Some applications are not affected; others repeat their startup procedures each time they receive a `run` command.

The `run` command launches an application as hidden; use `activate` to bring the application to the front.

For a `script` object, the `run` command causes either the explicit or the implicit `run` handler, if any, to be executed. For related information, see [run Handlers](../conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-SW15).

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_149"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
|  | `run` | *runTarget* | optional |

##### Parameters

`runTarget` *script*
:   A `script` or `application` object.

*Default Value:*
:   `it` (the current target)

##### Result

The result, if any, returned by the specified object’s `run` handler.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_150"></a>

##### Examples

```
run application "TextEdit"
tell application "TextEdit" to run
run myScript --where myScript is a script object
```

For information about using the `run` command with `script` objects, see [Sending Commands to Script Objects](../conceptual/ASLR_script_objects.md#//apple_ref/doc/uid/TP40000983-CH207-SW3).

##### Discussion

To specify an application to run, you can supply a string with only the application name, as shown in the Examples section. Or you can specify a location more precisely, using one of the forms described in [Aliases and Files](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW28). For examples of other ways to specify an application, see the `application` class.

It is not necessary to explicitly tell an application to `run` before sending it other commands; AppleScript will do that automatically. To launch an application without invoking its usual startup behavior, use the `launch` command. For further details, see [Calling a Script Application From a Script](../conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-SW17).

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW36"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_797"></a>

run script

Runs a specified script or script file.

See also `store script`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_151"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW187"></a>`run script` | | *scriptTextOrFileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW188"></a>`with parameters` | | *listOfParameters* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW189"></a>`in` | | *text* | optional |

##### Parameters

( *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)* | *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   The script text, or an `alias` or `file` specifier that specifies the script file to run.

`with parameters` *[list](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCDBHIE)* of *anything*
:   A list of parameter values to be passed to the script.

`in` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The scripting component to use.

*Default Value:*
:   `"AppleScript"`

##### Result

The result of the script’s `run` handler.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_152"></a>

##### Examples

The following script targets the application Finder, escaping the double quotes around the application name with the backslash character (for more information on using the backslash, see the Special String Characters section in the `text` class description):

```
run script "get name of front window of app \\"Finder\\"" --result: a window name
```

This example executes a script stored on disk:

```
set scriptAlias to "Leopard:Users:myUser:Documents:savedScript.scptd:" as alias
run script scriptAlias --result: script is executed
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW13"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_800"></a>

say

Speaks the specified text.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_153"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW190"></a>`say` | | *text* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW191"></a>`displaying` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW192"></a>`using` | | *text* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW193"></a>`waiting until completion` | | *boolean* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW194"></a>`saving to` | | *fileSpecifier* | optional |

##### Parameters

*[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The text to speak.

`displaying` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The text to display in the feedback window, if different from the spoken text. This parameter is ignored unless Speech Recognition is turned on (in System Preferences).

`using` *[text](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIAHJF)*
:   The voice to speak with—for example: `"Zarvox"`. You can use any of the voices from the System Voice pop-up on the Text to Speech tab in the Speech preferences pane.

*Default Value:*
:   The current System Voice (set in the Speech panel in System Preferences.

`waiting until completion` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Should the command wait for speech to complete before returning? This parameter is ignored unless Speech Recognition is turned on (in System Preferences).

*Default Value:*
:   `true`

`saving to` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier to an `AIFF` file (existing or not) to contain the sound output. You can only use an `alias` specifier if the file exists. If this parameter is specified, the sound is not played audibly, only saved to the file.

*Default Value:*
:   None; the text is spoken out loud, and no file is saved.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_154"></a>

##### Examples

```
say "You are not listening to me!" using "Bubbles" -- result: spoken in Bubbles
```

The following example saves the spoken text into a sound file:

```
set soundFile to choose file name -- specify name ending in ".aiff"
    --result: a file URL
say "I love oatmeal." using "Victoria" saving to soundFile
    --result: saved to specified sound file
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW37"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_805"></a>

scripting components

Returns a list of the names of all currently available scripting components, such as the AppleScript component.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_155"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW195"></a>`scripting components` | |  | required |

##### Result

A `list` of `text` items, one for each installed scripting component.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_156"></a>

##### Examples

```
scripting components --result: {"AppleScript"}
```

##### Discussion

A scripting component is a software component, such as AppleScript, that conforms to the Open Scripting Architecture (OSA) interface. The OSA provides an abstract interface for applications to compile, execute, and manipulate scripts without needing to know the details of the particular scripting language. Each scripting language corresponds to a single scripting component.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW52"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_806"></a>

set

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_807"></a>

Assigns one or more values to one or more variables.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_157"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
|  | `set` | *variablePattern* | required |
|  | `to` | *expression* | optional |

##### Parameters

*variablePattern*
:   The name of the variable or pattern of variables in which to store the value or pattern of values. Patterns can be lists or records.

`to` *expression*
:   The expression whose value is to be set. It can evaluate to any type of object or value.

##### Result

The value assigned.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_158"></a>

##### Examples

`set` may be used to create new variables:

```
set myWeight to 125
```

...assign new values to existing variables:

```
set myWeight to myWeight + 23
```

...change properties or elements of objects, such as lists:

```
set intList to {1, 2, 3}
set item 3 of intList to 42
```

...or application-defined objects:

```
tell application "Finder" to set name of startup disk to "Happy Fun Ball"
```

As mentioned in the Discussion, setting one variable to another makes both variables refer to the exact same object. If the object is mutable, that is, it has writable properties or elements, changes to the object will appear in both variables:

```
set alpha to {1, 2, {"a", "b"}}
set beta to alpha
set item 2 of item 3 of alpha to "change" --change the original variable
set item 1 of beta to 42 --change a different item in the new variable
{alpha, beta}
--result: {{42, 2, {"a", "change"}}, {42, 2, {"a", "change"}}}
```

Both variables show the same changes, because they both refer to the same object. Compare this with the similar example in `copy`. Assigning a new object to a variable is not the same thing as changing the object itself, and does not affect any other variables that refer to the same object. For example:

```
set alpha to {1, 2, 3}
set beta to alpha --result: beta refers to the same object as alpha
set alpha to {4, 5, 6}
    --result: assigns a new object to alpha; this does not affect beta.
{alpha, beta}
--result: {{4, 5, 6}, {1, 2, 3}}
```

`set` can assign several variables at once using a pattern, which may be a list or a record. For example:

```
tell application "Finder" to set {x, y} to position of front window
```

Since `position of front window` evaluates to a list of two integers, this sets `x` to the first item in the list and `y` to the second item.

You can think of pattern assignment as shorthand for a series of simple assignments, but that is not quite accurate, because the assignments are effectively simultaneous. That means that you can use pattern assignment to exchange two variables:

```
set {x, y} to {1, 2} --now x is 1, and y is 2.
set {x, y} to {y, x} --now x is 2, and y is 1.
```

To accomplish the second statement using only simple assignments, you would need a temporary third variable.

For more information on using the set command, including a more complex pattern example, see [Declaring Variables with the set Command](../conceptual/ASLR_variables.md#//apple_ref/doc/uid/TP40000983-CH223-SW9).

##### Discussion

Using the `set` command to assign a value to a variable causes the variable to refer to the original value. In a sense, it creates a new name for the same object. If multiple variables refer to a mutable object (that is, one with writable properties or elements, such as a list or `script` object), changes to the object are observable through any of the variables. If you want a separate copy, use the `copy` command. This sharing only applies to values in AppleScript itself; it does not apply to values in other applications. Changing the object a variable refers to is not the same as altering the object itself, and does not affect other variables that refer to the same object.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW33"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_809"></a>

set eof

Sets the length of a file, in bytes.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_159"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW64"></a>`set eof` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW196"></a>`to` | | *integer* | required |

##### Parameters

( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* | *file descriptor* )
:   The file to set the length of, as an alias, a file specifier, or as an integer file descriptor, which must be obtained as the result of an earlier `open for access` call.

`to` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The new length of the file, in bytes. If the new length is shorter than the existing length of the file, any data beyond that position is lost. If the new length is longer, the contents of the new bytes are unspecified.

##### Result

None.

Signals a “write permission” error if the file was opened using `open for access` without write permission.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_160"></a>

##### Examples

If you want to completely replace the contents of an existing file, the first step must be to change its length to zero:

```
set theFile to choose file with prompt "Choose a file to clobber:"
set eof theFile to 0
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW27"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_811"></a>

set the clipboard to

Places data on the clipboard.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_161"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW197"></a>`set the clipboard to` | | *anything* | required |

##### Parameters

*anything*
:   The data (of any type) to place on the clipboard.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_162"></a>

##### Examples

The following script places text on the clipboard, then retrieves the text in TextEdit with a `the clipboard` command:

```
set the clipboard to "Important new text."
tell application "TextEdit"
    activate  --make sure TextEdit is running
    set clipText to the clipboard  --result: "Important new text."
    --perform operations with retrieved text
end tell
```

##### Discussion

It is not necessary to use the clipboard to move data between scriptable applications. You can simply `get` the data from the first application into a variable and `set` the appropriate data in the second application.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW44"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_812"></a>

set volume

Sets the sound output, input, and alert volumes.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_163"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW198"></a>`set volume` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW199"></a> | | *number* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW200"></a>`output volume` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW201"></a>`input volume` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW202"></a>`alert volume` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW203"></a>`output muted` | | *boolean* | optional |

##### Parameters

*[number](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCBJDGC)*
:   The sound output volume, a real number from 0 to 7. <a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_164"></a> **Important:** This parameter is deprecated; if specified, all other parameters will be ignored.

`output volume` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The sound output volume, an integer from 0 to 100.

*Default Value:*
:   None; the output volume is not changed.

`input volume` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The sound input volume, an integer from 0 to 100.

*Default Value:*
:   None; the input volume is not changed.

`alert volume` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The alert input volume, an integer from 0 to 100.

*Default Value:*
:   None; the alert volume is not changed.

`output muted` *[boolean](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCIBBGG)*
:   Should the sound output be muted?

*Default Value:*
:   None; the output muting is not changed.

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_165"></a>

##### Examples

The following example saves the current volume settings, before increasing the output volume, saying some text, and restoring the original value:

```
set savedSettings to get volume settings
-- {output volume:32, input volume:70, alert volume:78, output muted:false}
set volume output volume 90
say "This is pretty loud."
set volume output volume (output volume of savedSettings)
delay 1
say "That's better."
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW38"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_817"></a>

store script

Stores a `script` object into a file.

See also `run script`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_166"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW204"></a>`store script` | | *script* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW205"></a>`in` | | *fileSpecifier* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW206"></a>`replacing` | | *replacingConstant* | optional |

##### Parameters

*script*
:   The `script` object to store.

`in` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* )
:   An `alias` or `file` specifier that specifies the file to store the `script` object in.

*Default Value:*
:   None; a standard Save As dialog will be presented to allow the user to choose where to save the `script` object.

`replacing` *replacingConstant*
:   Allow overwriting an existing file? You may specify one of the following constants: `yes` : Overwrite without asking. `no` : Never overwrite; signal an error if the file exists. `ask` : Present a dialog asking the user what to do; the options are Replace (overwrite the file), Cancel (signal a “user canceled” error), or Save As (save to a different location).

*Default Value:*
:   `ask`

##### Result

None.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_167"></a>

##### Examples

This example stores a script on disk, using the Save As dialog to specify a location on the desktop and the name `storedScript`. It then creates an alias to the stored script and runs it with `run script`:

```
script test
    display dialog "Test"
end script
 
store script test --specify "Leopard:Users:myUser:Desktop:storedScript"
 
set localScript to alias "Leopard:Users:myUser:Desktop:storedScript" run script localScript --result: displays dialog "Test"
```

The `store script` command stores only the contents of the script—in this case, the one statement, `display dialog "Test"`. It does not store the beginning and ending statements of the script definition.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW25"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_820"></a>

summarize

Summarizes the specified text or text file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_168"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW207"></a>`summarize` | | *textSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW222"></a>`in` | | *integer* | optional |

##### Parameters

*textSpecifier*
:   The `text`, or an `alias` to a text file, to summarize.

`in` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The number of sentences desired in the summary.

*Default Value:*
:   `1`

##### Result

A `text` object containing a summarized version of the text or file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_169"></a>

##### Examples

This example summarizes Lincoln’s famous Gettysburg Address down to one sentence—a tough job even for AppleScript:

```
set niceSpeech to "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."
set greatSummary to summarize niceSpeech in 1
display dialog greatSummary --result: displays one inspiring sentence
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW45"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_822"></a>

system attribute

Get environment variables or attributes of this computer.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_170"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW208"></a>`system attribute` | | *attribute* | optional |

##### Parameters

*attribute*
:   The attribute to test: either a Gestalt value or a shell environment variable name. Gestalt values are described in *[Gestalt Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/gestalt_manager)*.

*Default Value:*
:   If the attribute is omitted, `system attribute` will return a list of the names of all currently defined environment variables.

`has` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   For Gestalt values, an integer mask that is bitwise-ANDed with the Gestalt response. If the result is non-zero, `system attribute` returns `true`, otherwise `false`. For environment variables, this parameter is ignored.

*Default Value:*
:   None; `system attribute` returns the original Gestalt response code.

##### Result

If the attribute specified is a Gestalt selector, either the Gestalt response code or `true` or `false` depending on the `has` parameter.

If the attribute specified is an environment variable, the value of that variable, or an empty string (`""`) if it is not defined.

If no attribute is supplied, a list of all defined environment variables.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_171"></a>

##### Examples

To get the current shell:

```
system attribute "SHELL" --result: "/bin/bash" (for example)
```

To get a list of all defined environment variables:

```
system attribute
(* result: (for example)
{"PATH", "TMPDIR", "SHELL", "HOME", "USER", "LOGNAME", "DISPLAY", "SSH_AUTH_SOCK", "Apple_PubSub_Socket_Render", "__CF_USER_TEXT_ENCODING", "SECURITYSESSIONID", "COMMAND_MODE"}
*)
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW46"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_824"></a>

system info

Gets information about the system.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_172"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW209"></a>`system info` | |  | required |

##### Result

A record containing various information about the system and the current user. This record contains the following fields:

`AppleScript version` (a `text` object)
:   The version number of AppleScript, for example, `"2.0"`. This can be useful for testing for the existence of AppleScript features. When comparing version numbers, use `considering numeric strings` to make them compare in numeric order, since standard lexicographic ordering would consider `"1.9"` to come after `"1.10"`.

`AppleScript Studio version` (a `text` object)
:   The version number of AppleScript Studio, for example, `"1.5"`. <a id="//apple_ref/doc/uid/TP40000983-CH216-SW223"></a> **Note:** AppleScript Studio is deprecated in OS X v10.6.

`system version` (a `text` object)
:   The version number of OS X, for example, `"10.5.1"`.

`short user name` (a `text` object)
:   The current user’s short name, for example, `"hoser"`. This is set in the Advanced Options panel in the Accounts preference pane, or in the “Short Name” field when creating the account. This is also available from System Events using `name of current user`.

`long user name` (a `text` object)
:   The current user’s long name, for example, `"Random J. Hoser"`. This is the “User Name” field in the Accounts preference pane, or in the “Name” field when creating the account. This is also available from System Events using `full name of current user`.

`user ID` (an `integer` )
:   The current user’s user ID. This is set in the Advanced Options panel in the Accounts preference pane.

`user locale` (a `text` object)
:   The current user’s locale code, for example `"en_US"`.

`home directory` (an `alias` object)
:   The location of the current user’s home folder. This is also available from Finder’s `home` property, or System Events’ `home folder` property.

`boot volume` (a `text` object)
:   The name of the boot volume, for example, `"Macintosh HD"`. This is also available from Finder or System Events using `name of startup disk`.

`computer name` (a `text` object)
:   The computer’s name, for example `"mymac"`. This is the “Computer Name” field in the Sharing preference pane.

`host name` (a `text` object)
:   The computer’s DNS name, for example `"mymac.local"`.

`IPv4 address` (a `text` object)
:   The computer’s IPv4 address, for example `"192.201.168.13"`.

`primary Ethernet address` (a `text` object)
:   The MAC address of the primary Ethernet interface, for example `"00:1c:63:91:4e:db"`.

`CPU type` (a `text` object)
:   The CPU type, for example `"Intel 80486"`.

`CPU speed` (an `integer` )
:   The clock speed of the CPU in MHz, for example `2400`.

`physical memory` (an `integer` )
:   The amount of physical RAM installed in the computer, in megabytes (MB), for example `2048`.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_173"></a>

##### Examples

```
system info --result: long record of information
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW28"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_825"></a>

the clipboard

Returns the contents of the clipboard.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_174"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW210"></a>`the clipboard` | |  | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW211"></a>`as` | | *class* | optional |

##### Parameters

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   The type of data desired. `the clipboard` will attempt to find that “flavor” of data on the clipboard; if it is not found, it will attempt to coerce whatever flavor is there.

##### Result

The data from the clipboard, which can be of any type.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_175"></a>

##### Examples

The following script places text on the clipboard, and then appends the clipboard contents to the frontmost TextEdit document:

```
 
set the clipboard to "Add this sentence at the end."
tell application "TextEdit"
    activate  --make sure TextEdit is running
    make new paragraph at end of document 1 with data (return & the clipboard)
end tell
```

##### Discussion

It is not necessary to use the clipboard to move data between scriptable applications. You can simply `get` the data from the first application into a variable and `set` the appropriate data in the second application.

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW47"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_827"></a>

time to GMT

Returns the difference between local time and GMT (Greenwich Mean Time) or Universal Time, in seconds.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_176"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW212"></a>`time to GMT` | |  | required |

##### Result

The `integer` number of seconds difference between the current time zone and Universal Time.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_177"></a>

##### Examples

The following example computes the time difference between the current location and Cupertino:

```
set localOffset to time to GMT  --local difference, in seconds
set cupertinoOffset to -8.0 * hours
    --doesn't account for Daylight Savings; may actually be -7.0.
set difference to (localOffset - cupertinoOffset) / hours
display dialog ("Hours to Cupertino: " & difference)
```

<a id="//apple_ref/doc/uid/TP40000983-CH216-SW34"></a><a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_828"></a>

write

Writes data to a specified file.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_178"></a>

##### Syntax

|  |  |  |  |
| --- | --- | --- | --- |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW213"></a>`write` | | *anything* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW214"></a>`to` | | *fileSpecifier* | required |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW215"></a>`starting at` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW216"></a>`for` | | *integer* | optional |
| <a id="//apple_ref/doc/uid/TP40000983-CH216-SW217"></a>`as` | | *class* | optional |

##### Parameters

*anything*
:   The data to write to the file. This is typically `text`, but may be of any type. When reading the data back, the `read` command must specify the same type, or the results are undefined.

`to` ( *[alias](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW3)* | *[file](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-SW17)* | *file descriptor* )
:   The file to write to, as an alias, a file specifier, or an `integer` file descriptor. A file descriptor must be obtained as the result of an earlier `open for access` call.

`starting at` ( *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)* | *eof* )
:   The byte position in the file to start reading from. The position is 1-based, so `1` is the first byte of the file, `2` the second, and so on. Negative integers count from the end of the file, so `-1` is the last byte, `-2` the second-to-last, and so on. The constant `eof` is the position just after the last byte; use this to append data to the file.

*Default Value:*
:   The current file pointer (see `open for access`) if the file is open, or the beginning of the file if not.

`for` *[integer](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCHBDCJ)*
:   The number of bytes to write.

*Default Value:*
:   Write all the data provided.

`as` *[class](ASLR_classes.md#//apple_ref/doc/uid/TP40000983-CH1g-BBCFEDGB)*
:   Write the data as this class. The most common ones control the use of three different text encodings: `text` or `string` : The primary text encoding, as determined by the user’s language preferences set in the International preference panel. (For example, Mac OS Roman for English, MacJapanese for Japanese, and so on.) `Unicode text` : UTF-16. `«class utf8»` : UTF-8. Any other class is possible, for example `date` or `list`, but is typically only useful if the data will be read using a `read` statement specifying the same value for the `as` parameter.

*Default Value:*
:   The class of the supplied data. See Special Considerations.

##### Result

None. If the file is open, `write` will advance the file pointer by the number of bytes written, so the next `write` command will start writing where the last one ended.

Signals an error if the file is open without write permission, or if there is any other problem that prevents writing to the file, such as a lack of disk space.

<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_179"></a>

##### Examples

The following example opens a file with write permission, creating it if it doesn’t already exist, writes text to it, and closes it.

```
set fp to open for access file "HD:Users:myUser:NewFile" with write permission
write "Some text. And some more text." to fp
close access fp
```

##### Special Considerations

As specified above, `write` with no `as` parameter writes as the class of the supplied data, which means that in AppleScript 2.0 `write` always writes `text` data using the primary encoding. Prior to 2.0, `string` and `Unicode text` were distinct types, which meant that it would use primary encoding for `string` and UTF-16 for `Unicode text`. For reliable results when creating scripts that will run on both 2.0 and pre-2.0, always specify the encoding explicitly using `as text` or `as Unicode text`, as appropriate.<a id="//apple_ref/doc/uid/TP40000983-CH216-DontLinkElementID_833"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
