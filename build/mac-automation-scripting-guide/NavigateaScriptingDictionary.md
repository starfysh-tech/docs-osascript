<a id="//apple_ref/doc/uid/TP40016239-CH77"></a><a id="//apple_ref/doc/uid/TP40016239-CH77-SW1"></a>

## Navigating a Scripting Dictionary

A scripting dictionary window in Script Editor contains three primary areas. See Figure 12-1.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW2"></a>
**Figure 12-1**Primary elements of a scripting dictionary window in Script Editor
![image: ../Art/script-editor_dictionary-callouts_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/script-editor_dictionary-callouts_2x.png)

* **Toolbar.** Options for toggling between terminology views, setting the scripting language, entering search terms, and more.
* **Navigation pane.** Columns of scripting terminology.
* **Detail pane.** Definitions for any terminology selected in the navigation pane.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW13"></a>

### Types of Terminology

The navigation pane of a dictionary includes the types of terms described in Table 12-1.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW3"></a>

**Table 12-1**Types of scripting terminology

| Type | Icon | Description |
| --- | --- | --- |
| Suite | image: ../Art/osa_suite_2x.png | A *suite* is a grouping of related commands and classes. Apps often have a Standard Suite, which includes terminology supported by most scriptable apps, such as an `open` command, a `quit` command, and an `application` class. |
| Command | image: ../Art/osa_command_2x.png | A *command* is an instruction that can be sent to an app or object in order to initiate some action. For example, `delete`, `make`, `print` are commands that are found in many scriptable apps. Many commands have *parameters* that specify the target object and control the behavior of the command. |
| Class | image: ../Art/osa_class_2x.png    image: ../Art/osa_element_2x.png | A *class* is an object within an app, or an app itself. Mail, for example, has an `application` class, a `message` class, and a `signature` class, among others. Objects within an app sometimes contain other objects as *elements*. For example, in Mail, a `mailbox` objects can contain `message` objects as elements. |
| Property | image: ../Art/osa_property_2x.png | A *property* is an attribute of a class. For example, the `message` class in Mail has many properties, including `date received`, `read status`, and `subject`. Some properties are read-only, while others are readable and writable. |

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW14"></a>

### Key Concepts

It’s important to understand the concepts of *inheritance* and *containment* when navigating a scripting dictionary.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW15"></a>

### Inheritance

In a scriptable app, different classes often implement the same properties. For example, in Finder, the `file` and `folder` classes both have `creation date`, `modification date`, and `name` properties. Rather than defining these same properties multiple times throughout the scripting dictionary, Finder implements a generic `item` class. Since files and folders are considered types of Finder items, these classes inherit the properties of the `item` class. In other words, any properties of the `item` class also apply to the `file` and `folder` classes. There are many other items in Finder that also inherit these same properties, including the `disk`, `package`, and `alias file` classes.

A class that inherits the properties of other classes can also implement its own properties. In Finder, the `file` class implements a number of file-specific properties, including `file type` and `version`. The `alias file` class implements an `original item` property.

In some cases, a class inherits properties from multiple classes. In Finder, an alias is a type of file, which is a type of item. Therefore, the `alias file` class inherits the properties of both the `file` and `item` classes, as shown in Figure 12-2.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW4"></a>
**Figure 12-2**In scripting, classes can inherit the properties of other classes
![image: ../Art/Inheritance_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/Inheritance_2x.png)

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW16"></a>

### Containment

Classes of a scriptable app reside within a certain containment hierarchy. The application is at the top level, with other classes nested beneath. Finder, for example, contains disks, folders, files, and other objects. While files don’t contain elements, folders and disks can contain other folders and files. See Figure 12-3. Mail is another example—the application contains accounts, which can contain mailboxes, which can contain other mailboxes and messages.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW5"></a>
**Figure 12-3**In scripting, classes can contain other classes as elements
![image: ../Art/Containment_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/Containment_2x.png)

When referencing a class, you must do so very specifically according to its containment hierarchy in order to provide the scripting system with context. To reference a file in Finder, you would specify where the file resides in the folder hierarchy. See Listing 12-1 and Listing 12-2. To reference a message in Mail, you would specify where the message resides in the mailbox and account hierarchy.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&name=Reference%20a%20File%20by%20Containment%20Hierarchy%20in%20Finder&script=tell%20application%20%22Finder%22%0D%20%20%20%20modification%20date%20of%20file%20%22My%20File.txt%22%20of%20folder%20%22Documents%22%20of%20folder%20%22YourUserName%22%20of%20folder%20%22Users%22%20of%20startup%20disk%0Dend%20tell%0D--%3E%20Result%3A%20date%20%22Monday%2C%20September%2028%2C%202015%20at%2010%3A10%3A17%20AM%22%0D)

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW6"></a>
**Listing 12-1**AppleScript: Referencing a file by containment hierarchy in Finder

1. `tell application "Finder"`
2. ` modification date of file "My File.txt" of folder "Documents" of folder "YourUserName" of folder "Users" of startup disk`
3. `end tell`
4. `--&gt; Result: date "Monday, September 28, 2015 at 10:10:17 AM"`

**JAVASCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&name=Reference%20a%20File%20by%20Containment%20Hierarchy%20in%20Finder&script=var%20Finder%20%3D%20Application%28%22Finder%22%29%0DFinder.startupDisk.folders%5B%22Users%22%5D.folders%5B%22YourUserName%22%5D.folders%5B%22Documents%22%5D.files%5B%22My%20File.txt%22%5D.modificationDate%28%29%0D%2F%2F%20Result%3A%20Mon%20Sep%2028%202015%2017%3A10%3A17%20GMT-0700%20%28PDT%29%0D)

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW7"></a>
**Listing 12-2**JavaScript: Referencing a file by containment hierarchy in Finder

1. `var Finder = Application("Finder")`
2. `Finder.startupDisk.folders["Users"].folders["YourUserName"].folders["Documents"].files["My File.txt"].modificationDate()`
3. `// Result: Mon Sep 28 2015 17:10:17 GMT-0700 (PDT)`

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW17"></a>

### Anatomy of a Command Definition

The definition of a command in a scripting dictionary is a recipe for using the command, as shown in Figure 12-4, Listing 12-3, and Listing 12-4.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW8"></a>
**Figure 12-4**Definition for the move command in the Finder scripting dictionary
![image: ../Art/dictionary_move_command_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/dictionary_move_command_2x.png)

A command definition includes the following elements:

* **Command name.** The name of the command.
* **Direct parameter.** An object to be targeted by the command. For the `move` command in Finder, this is the object to be moved. If a command definition doesn’t specify a direct parameter, then the target object is the application. A direct parameter immediately follows the command.
* **Labeled parameters.** Control some aspect of the command’s behavior and are required or optional. Optional parameters are surrounded by brackets. Since these parameters are identified by label, they can be placed in any order when you write your script. The command definition denotes the value type for each labeled parameter. For example, the optional `replacing` parameter for the `move` command in Finder takes a boolean value.
* **Result.** The result of the command, if any. Often, this is a reference to a newly created or modified object. For the `move` command in Finder, it’s a reference to the moved object.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&name=Example%20Usage%20of%20the%20Move%20Command%20in%20Finder&script=tell%20application%20%22Finder%22%0D%20%20%20%20move%20folder%20someFolder%20to%20someOtherFolder%20replacing%20true%0Dend%20tell%0D)

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW9"></a>
**Listing 12-3**AppleScript: Example usage of the move command in Finder

1. `tell application "Finder"`
2. ` move folder someFolder to someOtherFolder replacing true`
3. `end tell`

**JAVASCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&name=Example%20Usage%20of%20the%20Move%20Command%20in%20Finder&script=var%20Finder%20%3D%20Application%28%22Finder%22%29%0DFinder.move%28someFolder%2C%20%7B%0D%20%20to%3A%20someOtherFolder%2C%0D%20%20replacing%3A%20true%0D%7D%29%0D)

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW10"></a>
**Listing 12-4**JavaScript: Example usage of the move command in Finder

1. `var Finder = Application("Finder")`
2. `Finder.move(someFolder, {`
3. ` to: someOtherFolder,`
4. ` replacing: true`
5. `})`

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW18"></a>

### Anatomy of a Class Definition

A class definition describes a class, as shown in Figure 12-5.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW12"></a>
**Figure 12-5**Definition for the mailbox class in the Mail scripting dictionary
![image: ../Art/dictionary_mailbox_class_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/dictionary_mailbox_class_2x.png)

A class definition includes the following elements:

* **Class name.** The name of the class.
* **Inheritance details.** A list of other classes from which properties are inherited, if any. Each class is a hyperlink—clicking it takes you to the definition for the corresponding class.
* **Containment details.** A list of contained classes, if any. May also list other classes containing the class, if any.
* **Properties.** Any properties for the class, along with their data types. Read-only properties include an `r/o` indicator.

To view inherited properties, as well as containing classes in the Script Editor dictionary viewer, select Show inherited items in Preferences &gt; General. See Figure 12-6.

<a id="//apple_ref/doc/uid/TP40016239-CH77-SW11"></a>
**Figure 12-6**Enabling inherited item dictionary details in Script Editor
![image: ../Art/script-editor_preferences_window_showinheriteditems_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/script-editor_preferences_window_showinheriteditems_2x.png)
