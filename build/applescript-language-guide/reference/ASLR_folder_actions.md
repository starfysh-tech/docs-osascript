<a id="//apple_ref/doc/uid/TP40000983-CH219-SW2"></a>

# Folder Actions Reference

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_919"></a>Folder Actions is a feature of macOS that lets you associate AppleScript scripts with folders. A Folder Action script is executed when the folder to which it is attached has items added or removed, or when its window is opened, closed, moved, or resized. The script provides a handler that matches the appropriate format for the action, as described in this chapter.

Folder Actions make it easy to create hot folders that respond to external actions to trigger a workflow. For example, you can use a Folder Action script to initiate automated processing of any photo dropped in a targeted folder. A well written Folder Action script leaves the hot folder empty. This avoids repeated application of the action to the same files, and allows Folder Actions to perform more efficiently.

You can Control-click a folder to access some Folder Action features with the contextual menu in the Finder. Or you can use the Folder Actions Setup application, located in `/System/Library/CoreServices`. This application lets you perform tasks such as the following:

* Enable or disable Folder Actions.
* View the folders that currently have associated scripts
* View and edit the script associated with a folder.
* Add folders to or remove folders from the list of folders.
* Associate one or more scripts with a folder.
* Enable or disable all scripts associated with a folder.
* Enable or disable individual scripts associated with a folder.
* Remove scripts associated with a folder.

Folder Actions Setup looks for scripts located in `/Library/Scripts/Folder Action Scripts` and `~/Library/Scripts/Folder Action Scripts`. You can use the sample scripts located in `/Library/Scripts/Folder Action Scripts` or any scripts you have added to these locations, or you can navigate to other scripts.

A Folder Action script provides a handler (see [Handler Reference](ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-163762)) that is invoked when the specified action takes place. When working with Folder Action handlers, keep in mind that:

* You do not invoke Folder Actions directly. Instead, when a triggering action takes place on a folder, the associated handler is invoked automatically.
* When a Folder Action handler is invoked, none of the parameters is optional.
* A Folder Action handler does not return a value.

Here’s how you can use a Folder Action script to perform a specific action whenever an image file is dropped on a specific image folder:

1. Create a script with Script Editor or another script application.
2. In that script, write a handler that conforms to the syntax documented here for the `adding folder items to` folder action. Your handler can use the aliases that are passed to it to access the image files dropped on the folder.
3. Save the script as a compiled script or script bundle.
4. Put a copy of the script in `/Library/Scripts/Folder Action Scripts` or `~/Library/Scripts/Folder Action Scripts`.
5. Use the Folder Actions Setup application, located in `/Applications/AppleScript`, to:

   1. Enable folder actions for your image folder.
   2. Add a script to that folder, choosing the script you created.

<a id="//apple_ref/doc/uid/TP40000983-CH219-SW48"></a>

adding folder items to

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_920"></a>A script handler that is invoked after items are added to its associated folder.

##### Syntax

|  |
| --- |
| ``` on adding folder items to alias after receiving listOfAlias  [ statement ]... end [ adding folder items to ]  ``` |

##### Placeholders

*alias*
:   An `alias` that identifies the folder that received the items.

*listOfAlias*
:   List of aliases that identify the items added to the folder.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_203"></a>

##### Examples

The following Folder Action handler is triggered when items are added to the folder to which it is attached. It makes an archived copy, in ZIP format, of the individual items added to the attached folder. Archived files are placed in a folder named `Done` within the attached folder.

```
 
on adding folder items to this_folder after receiving these_items
    tell application "Finder"
        if not (exists folder "Done" of this_folder) then
            make new folder at this_folder with properties {name:"Done"}
        end if
        set the destination_folder to folder "Done" of this_folder as alias
        set the destination_directory to POSIX path of the destination_folder
    end tell
    repeat with i from 1 to number of items in these_items
        set this_item to item i of these_items
        set the item_info to info for this_item
        if this_item is not the destination_folder and ¬
            the name extension of the item_info is not in {"zip", "sit"} then
            set the item_path to the quoted form of the POSIX path of this_item
            set the destination_path to the quoted form of ¬
                (destination_directory & (name of the item_info) & ".zip")
            do shell script ("/usr/bin/ditto -c -k -rsrc --keepParent " ¬
                & item_path & " " & destination_path)
        end if
    end repeat
end adding folder items to
```

<a id="//apple_ref/doc/uid/TP40000983-CH219-SW1"></a>

closing folder window for

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_921"></a>A script handler that is invoked after a folder’s associated window is closed.

##### Syntax

|  |
| --- |
| ``` on closing folder window for alias  [ statement ]... end [ closing folder window for ]  ``` |

##### Placeholders

*alias*
:   An `alias` that identifies the folder that was closed.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_204"></a>

##### Examples

The following Folder Action handler is triggered when the folder to which it is attached is closed. It closes any open windows of folders within the targeted folder.

```
-- This script is designed for use with OS X v10.2 and later.
on closing folder window for this_folder
    tell application "Finder"
        repeat with EachFolder in (get every folder of folder this_folder)
            try
                close window of EachFolder
            end try
        end repeat
    end tell
end closing folder window for
```

<a id="//apple_ref/doc/uid/TP40000983-CH219-SW50"></a>

moving folder window for

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_922"></a>A script handler that is invoked after a folder’s associated window is moved or resized. Not currently available.

##### Syntax

|  |
| --- |
| ``` on moving folder window for alias from bounding rectangle  [ statement ]... end [ moving folder window for ]  ``` |

##### Placeholders

*alias*
:   An `alias` that identifies the folder that was moved or resized. You can use this alias to obtain the folder window’s new coordinates from the Finder.

*bounding rectangle*
:   The previous coordinates of the window of the folder that was moved or resized. The coordinates are provided as a list of four numbers, {left, top, right, bottom}; for example, {10, 50, 500, 300} for a window whose origin is near the top left of the screen (but below the menu bar, if present).

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_205"></a>

##### Examples

```
on moving folder window for this_folder from original_coordinates
    tell application "Finder"
        set this_name to the name of this_folder
        set the bounds of the container window of this_folder ¬
            to the original_coordinates
    end tell
    display dialog "Window \\"" & this_name & "\\" has been returned to its original size and position." buttons {"OK"} default button 1
end moving folder window for
```

##### Special Considerations

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_206"></a>

**Warning:** In OS X v10.5, and possibly in previous OS versions, Folder Actions does not activate attached `moving folder window for` scripts when the folder is moved.

<a id="//apple_ref/doc/uid/TP40000983-CH219-SW51"></a>

opening folder

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_923"></a>A script handler that is invoked when its associated folder is opened in a window.

##### Syntax

|  |
| --- |
| ``` on opening folder alias  [ statement ]... end [ opening folder ]  ``` |

##### Placeholders

*alias*
:   An `alias` that identifies the folder that was opened.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_207"></a>

##### Examples

The following Folder Action handler is triggered when the folder it is attached to is opened. It displays any text from the Spotlight Comments field of the targeted folder. (Prior to OS X v10.4, this script displays text from the Comments field of the specified folder.)

```
-- This script is designed for use with OS X v10.2 and later.
property dialog_timeout : 30 -- set the amount of time before dialogs auto-answer.
 
on opening folder this_folder
    tell application "Finder"
        activate
        set the alert_message to the comment of this_folder
        if the alert_message is not "" then
            display dialog alert_message buttons {"Open Comments", "Clear Comments", "OK"} default button 3 giving up after dialog_timeout
            set the user_choice to the button returned of the result
            if the user_choice is "Clear Comments" then
                set comment of this_folder to ""
            else if the user_choice is "Open Comments" then
                open information window of this_folder
            end if
        end if
    end tell
end opening folder
```

##### Special Considerations

Spotlight was introduced in OS X v10.4. In prior versions of the Mac OS, the example script shown above works with the Comments field of the specified folder, rather than the Spotlight Comments field.

<a id="//apple_ref/doc/uid/TP40000983-CH219-SW52"></a>

removing folder items from

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_924"></a>A script handler that is invoked after items have been removed from its associated folder.

##### Syntax

|  |
| --- |
| ``` on removing folder items from alias after losing listOfAliasOrText  [ statement ]... end [ removing folder items from ]  ``` |

##### Placeholders

*alias*
:   An `alias` that identifies the folder from which the items were removed.

*listOfAliasOrText*
:   List of aliases that identify the items lost (removed) from the folder. For permanently deleted items, only the names are provided (as `text` strings).

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_208"></a>

##### Examples

The following Folder Action handler is triggered when items are removed from the folder to which it is attached. It displays an alert containing the number of items removed.<a id="//apple_ref/doc/uid/TP40000983-CH219-DontLinkElementID_925"></a>

```
on removing folder items from this_folder after losing these_items
    tell application "Finder"
        set this_name to the name of this_folder
    end tell
    set the item_count to the count of these_items
    display dialog (item_count as text) & " items have been removed " & "from folder \\"" & this_name & "\\"." buttons {"OK"} default button 1
end removing folder items from
```

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
