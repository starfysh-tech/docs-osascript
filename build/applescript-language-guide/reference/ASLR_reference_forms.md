<a id="//apple_ref/doc/uid/TP40000983-CH4g-120522"></a>

# Reference Forms

This chapter describes AppleScript reference forms. <a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1065"></a>A *reference form* specifies the syntax for identifying an object or group of objects in an application or other container—that is, the syntax for constructing an object specifier (described in [Object Specifiers](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW7)).

For example, the following object specifier (from a script targeting the Finder) uses several index reference forms, which identify an object by its number within a container:<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1066"></a>

```
item 1 of second folder of disk 1
```

> <a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_218"></a>
>
> **Important:** When you use a reference form, you specify the container in which the referenced object or objects reside. This takes the form *referenceForm* `of` *containerObject*. You can also enclose a reference form in a `tell` statement, which then serves to specify the outer container. For more information, see [Absolute and Relative Object Specifiers](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW25).
>
> Some of the examples of reference forms shown in this chapter will not compile as shown. To compile them, you may need to add an enclosing `tell` statement, targeting the Finder or the word processing application TextEdit.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BCIJEEHE"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-120700"></a>Arbitrary

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1067"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1068"></a>Specifies an arbitrary object in a container. This form is useful whenever randomness is desired.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1069"></a>

Because an arbitrary item is, by its nature, random, this form is not useful for operations such as processing each item in a group of files, words, or other objects.

##### Syntax

|  |
| --- |
| ``` some  class  ``` |

##### Placeholders

*class*
:   The class for an arbitrary object.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_219"></a>

##### Examples

The following creates a new Mail message with a random signature (and depends on the user having at least one signature):

```
tell application "Mail"
    activate
    set randomSignature to some signature
    set newMessage to make new outgoing message ¬
        at end of outgoing messages with properties ¬
        {subject:"Guess who?", content:"Welcome aboard.", visible:true}
    set message signature of newMessage to randomSignature
end tell
```

The following simply gets a random word from a TextEdit document:

```
tell application "TextEdit"
    some word of document 1 -- any word from the first document
end tell
```

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCJFIIH"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-120825"></a>Every

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1070"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1071"></a>Specifies every object of a particular class in a container.

##### Syntax

|  |
| --- |
| ```  every  class   pluralClass  ``` |

##### Placeholders

*class*
:   A singular class (such as `word` or `paragraph`).

*pluralClass*
:   The plural form for a class (such as `words` or `paragraphs`).<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1073"></a>

##### Value

The value of an `every` object specifier is a list of the objects from the container. If the container does not contain any objects of the specified class, the list is an empty list: {}. For example, the value of the expression `every word of {1, 2, 3}` is the empty list `{}`.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_220"></a>

##### Examples

The following example uses an `every` object specifier to specify every word contained in a text string:

```
set myText to "That's all, folks"
every word of myText --result: {"That's", "all", "folks"} (a list of three words)
```

The following object specifier specifies the same list:

```
words of myText
```

The following example specifies a list of all the items in the Users folder of the startup disk (boot partition):

```
tell application "Finder"
    every item of folder "Users" of startup disk
end tell
```

The following specifies the same list as the previous example:

```
tell application "Finder"
    items of folder "Users" of startup disk
end tell
```

##### Discussion

Use of the `every` reference form implies the existence of an `index` property for the specified objects.

If you specify an `every` object specifier as the container from which to obtain a property or object, the result is a list containing the specified property or object for each object of the container. The number of items in the list is the same as the number of objects in the container.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BAJJHEFE"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-121170"></a>Filter

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1074"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1075"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1076"></a>Specifies all objects in a container that match a condition, or test, specified by a Boolean expression.

The filter form specifies application objects only. It cannot be used to filter the AppleScript objects `list`, `record`, or `text`. A term that uses the filter form is also known as a `whose` clause.

> <a id="//apple_ref/doc/uid/TP40000983-CH4g-SW3"></a>
>
> **Note:** You can use the words `where`<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1077"></a> or `that`<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1078"></a> as <a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1079"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1080"></a>synonyms for `whose`.

A filter reference form can often be replaced by a `repeat` statement, or vice versa. For example, the following script closes every TextEdit window that isn’t named `"Old Report.rtf"`:

```
tell application "TextEdit"
    close every window whose name is not "Old Report.rtf"
end tell
```

You could instead obtain a list of open windows and set up a `repeat` statement that checks the name of each window and closes the window if it isn’t named `"Old Report.rtf"`. However, a `whose` clause is often the fastest way to obtain the desired information.

The following is an abbreviated form of the previous script:

```
windows of application "TextEdit" whose name is not "Old Report.rtf"
```

For related information, see [repeat Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-127362).

##### Syntax

|  |
| --- |
| ```  objectSpecifier  ( whose \| where )  booleanTest    ``` |

##### Placeholders

*objectSpecifier*
:   Specifies the container in which to look for objects that match the Boolean test.

`whose` | `where`
:   These words have the same meaning, and refer to all of the objects in the specified container that match the conditions in the specified Boolean expression.

*booleanTest*
:   Any Boolean expression (see the `boolean` class definition).

##### Value

The value of a filter reference form is a list of the objects that pass the test. If no objects pass the test, the list is an empty list: {}.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_221"></a>

##### Examples

The following example shows an object specifier for all open Finder windows that do not have the name `"AppleScript Language Guide"`.

```
tell application "Finder"
    every window whose name is not "AppleScript Language Guide"
end tell
```

##### Discussion

In effect, a filter reduces the number of objects in a container. Instead of specifying `every` Finder window, the following object specifier specifies just the windows that are currently zoomed:

```
every window whose zoomed is true
```

To specify a container after a filter, you must enclose the filter and the object specifier it applies to in parentheses, as in this example:

```
tell application "Finder"
    (files whose file type is not "APPL") in folder "HD:SomeFolder:"
end tell
```

Within a test in a filter reference, the direct object is the object being tested. Though it isn’t generally needed, this implicit target can be specified explicitly using the keyword `it`, which is described in [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4).

The following example shows several equivalent ways of constructing a filter reference to find all the files in a folder that whose name contains the word “AppleScript”. While the term `it` refers to the Finder application outside of the filter statements, within them `of it` refers to the current file being tested. The result of each filter test is the same and is not changed by including or omitting the term `of it`:

```
tell application "Finder"
    it --result: application "Finder" (target of tell statement)
    set myFolder to path to home folder
        --result: alias "Leopard:Users:myUser:"
    files in myFolder --result: a list of Finder document files
    files in myFolder where name of it contains "AppleScript"
    (* result: document file "AppleScriptLG.pdf" of folder "myUser"
        of folder "Users" of startup disk of application "Finder"}*)
    files in myFolder where name contains "AppleScript" -- same result
    every file in myFolder whose name contains "AppleScript" -- same result
    every file in myFolder where name of it contains "AppleScript"
        -- same result
end tell
```

A filter reference form includes one or more tests. Each test is a Boolean expression that compares a property or element of each object being tested, or the objects themselves, with another object or value. [Table 8-1](#//apple_ref/doc/uid/TP40000983-CH4g-SW1) shows some filter references, the Boolean expressions they contain, and what is being tested in each reference.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-SW1"></a>

**Table 8-1**  Boolean expressions and tests in filter references

| Filter reference form | Boolean expression | What is being tested |
| `windows whose zoomed is true` | `zoomed is true` | The `zoomed` property of each window |
| `windows whose name isn’t "Hard Disk"` | `name isn’t "Hard Disk"` | The `name` property of each window |
| `files whose creator type is "OMGR"` | `creator type is "OMGR"` | The `creator type` property of each file |

A test can be any Boolean expression. You can link multiple tests, as in the following statement:

```
windows whose zoomed is true and floating is false
```

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCJDFIE"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-121447"></a>ID

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1083"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1084"></a>Specifies an object by the value of its `id` property.

You can use the ID reference form only with application objects that have an ID property.

##### Syntax

|  |
| --- |
| ``` class id  expression   ``` |

##### Placeholders

*expression*
:   The id value.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_222"></a>

##### Examples

The following examples use the ID reference form to specify an `application` by ID and a `disk` object by ID.

```
tell application id "com.apple.finder"
-- specifies an application (Finder) by its ID
disk id -100 -- specifies a Finder disk object by ID
name of disk id -100 --result: "Leopard_GM" (gets name from ID specifier)
end tell
```

##### Discussion

Use of the `id` reference form implies the existence of a `id` property for the specified objects.

Although `id` properties are most often integers, an `id` property can belong to any class. An application that supports `id` properties for its scriptable objects must guarantee that the IDs are unique within a container. Some applications may also provide additional guarantees, such as ensuring the uniqueness of an ID among all objects.

The value of an `id` property is not typically modifiable. It does not change even if the object is moved within the container. This allows you to save an object’s ID and use it to refer to the object for as long as the object exists. In some scripts you may wish to refer to an object by its ID, rather than by a property such as its name, which may change. Similarly, you could keep track of an item by its index, but indexes can change when items in a container are added, deleted, or even renamed.

> <a id="//apple_ref/doc/uid/TP40000983-CH4g-SW2"></a>
>
> **Note:** A good way to keep track of files and folders is to use an `alias`.

Starting in AppleScript 2.0, objects of class `application` have an `id` property, which represents the application’s bundle identifier (the default) or its four-character signature code.

Also starting in AppleScript 2.0, objects of class `text` have an `id` property, representing the Unicode code point or points for the character or characters in the object. Because a `text` object’s ID is based on the characters it contains, these IDs are not guaranteed to be unique, and in fact will be identical for two `text` objects that store the same characters. And in fact, there is no way to tell two such objects apart by inspection.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-121798"></a>Index

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1086"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1087"></a>Specifies an object by describing its position with respect to the beginning or end of a container.

For related information, see [Relative](#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI).

##### Syntax

|  |
| --- |
| ```  class [ index ] integer   integer ( st \| nd \| rd \| th ) class  ( first \| second \| third \| fourth \| fifth \| sixth \| seventh \| eighth \| ninth \| tenth ) class            ( last \| front \| back ) class     ``` |

##### Placeholders

*class*
:   The class of the indexed object to obtain.

*integer*
:   An integer that describes the position of the object in relation to the beginning of the container (if integer is a positive integer) or the end of the container (if integer is a negative integer).

`st` | `nd` | `rd` | `th`
:   Appended to the appropriate integer to form an index. For example, `1st`, `2nd`, `3rd`.

`first` | `second` | `third` | `fourth` | `fifth` | `sixth` | `seventh` | `eighth` | `ninth` | `tenth`
:   Specify one of the ordinal indexes. The forms `first`, `second`, and so on are equivalent to the corresponding integer forms (for example, `second word` is equivalent to `2nd word`). For objects whose index is greater than 10, you can use the forms `12th`, `23rd`, `101st`, and so on. (Note that any integer followed by any of the suffixes listed is valid; for example, you can use `11rd` to refer to the eleventh object.)

`last` | `front` | `back`
:   The `front` form (for example, `front window`) is equivalent to *class 1* (`window 1`) or *first class* (`first window`). The `last` and `back` forms (for example, `last word` and `back window`) refer to the last object in a container. They are equivalent to *class -1* (for example, `window -1`).

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_223"></a>

##### Examples

Each of the following object specifiers specifies the first item on the startup disk:

```
item 1 of the startup disk
item index 1 of the startup disk -- "index" is usually omitted
the first item of the startup disk
```

The following object specifiers specify the second word from the beginning of the third paragraph:

```
word 2 of paragraph 3
2nd word of paragraph 3
second word of paragraph 3
```

The following object specifiers specify the last word in the third paragraph:

```
word –1 of paragraph 3
last word of paragraph 3
```

The following object specifiers specify the next-to-last word in the third paragraph.

```
word –2 of paragraph 3
-2th word of paragraph 3
```

##### Discussion

Indexes are volatile. Changing some other property of the object may change its index, as well as the index of other like objects. For example, after deleting `word 4` from a paragraph, the word no longer exists. But there may still be a `word 4`—the word that was formerly `word 5`. After `word 4` is deleted, any words with an index higher than 4 will also have a new index. So the object an index specifies can change.

For a unique, persistent object specifier, you can use the `id` reference form (see [ID](#//apple_ref/doc/uid/TP40000983-CH4g-BBCJDFIE)), if the application supports it for the class of object you are working with. And for keeping track of a file, you can use an `alias` object.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCJFDBA"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-122258"></a>Middle

Specifies the middle object of a particular class in a container. This form is rarely used.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1102"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1103"></a>

##### Syntax

|  |
| --- |
| ```  middle  class   ``` |

##### Placeholders

*class*
:   The class of the middle object to obtain.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_224"></a>

##### Examples

```
tell application "TextEdit"
    middle paragraph of front document
end tell
middle item of {1, "doughnut", 33} --result: "doughnut"
middle item of {1, "doughnut", 22, 33} --result: "doughnut"
middle item of {1, "doughnut", 11, 22, 33} --result: 11
```

##### Discussion

The `middle` reference form generally works only when the `index` form also works.

AppleScript calculates the middle object by taking half the count, then rounding up. For example, the middle word of a paragraph containing ten words is the fifth word; the middle of eleven words is the sixth.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCIBAAJ"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-122409"></a>Name

Specifies an object by name.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1105"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1106"></a>

##### Syntax

|  |
| --- |
| ```  class  [ named ]  nameText   ``` |

##### Placeholders

*class*
:   The class for the specified object.

*nameText*
:   The value of the object’s name property.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_225"></a>

##### Examples

The following statements identify objects by name:

```
document "Report.rtf"
window named "logs"
```

##### Discussion

Use of the `name` reference form implies the existence of a `name` property for the specified objects.

In some applications, it is possible to have multiple objects of the same class in the same container with the same name. For example, if there are two drives named “Hard Disk”, the following statement is ambiguous (at least to the reader):

```
tell application "Finder"
    item 1 of disk "Hard Disk"
end tell
```

In such cases, it is up to the application to determine which object is specified by a `name` reference.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCJCGDB"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-122724"></a>Property

Specifies a property of an object.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1108"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1109"></a>

##### Syntax

|  |
| --- |
| ```  propertyLabel  ``` |

##### Placeholders

*propertyLabel*
:   The label for the property.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_226"></a>

##### Examples

The following example is an object specifier to a property of a Finder window. It lists the label for the window’s property (`zoomed`) and its container (`front window`). `zoomed` is a Boolean property.

```
zoomed of front window -- e.g., false, if the window isn't zoomed
```

For many objects, you can obtain a list of properties:

```
tell app "Finder"
     properties of window 1 --result: a list of properties and their values
end tell
```

The following example is an object specifier to the `UnitPrice` property of a `record` object. The label of the property is `UnitPrice` and the container is the `record` object.

```
UnitPrice of {Product:"Super Snack", UnitPrice:0.85, Quantity:10} --result: 0.85
```

##### Discussion

Property labels are listed in class definitions in application dictionaries. Because a property’s label is unique among the properties of an object, the label is all you need to specify the property—there is no need to specify the class of the property.

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-122867"></a>Range

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1110"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1111"></a>Specifies a series of objects of the same class in the same container. You can specify the objects with a pair of indexes (such as `words 12 thru 24`) or with a pair of boundary objects (`integers from integer 1 to integer 3`).

##### Syntax

|  |
| --- |
| ```  every  class  from  boundarySpecifier1  to  boundarySpecifier2   pluralClass  from  boundarySpecifier1  to  boundarySpecifier2  class  startIndex  ( thru \| through )  stopIndex    pluralClass  startIndex  ( thru \| through )  stopIndex  ``` |

##### Placeholders

*class*
:   A singular class (such as `window` or `word`).

*pluralClass*
:   A plural class (such as `windows` or `words`).

*boundarySpecifier1* and *boundarySpecifier2*
:   Specifiers to objects that bound the range. The range includes the boundary objects. You can use the reserved word `beginning` in place of *boundarySpecifier1* to indicate the position before the first object of the container. Similarly, you can use the reserved word `end` in place of *boundarySpecifier2* to indicate the position after the last object in the container.

*startIndex* and *stopIndex*
:   The indexes of the first and last object of the range (such as `1` and `10` in `words 1 thru 10`). Though integer indexes are the most common class, the start and stop indexes can be of any class. An application determines which index classes are meaningful to it.

##### Value

The value of a range reference form is a list of the objects in the range. If the specified container does not contain objects of the specified class, or if the range is out of bounds, an error is returned. For example, the following range specifier results in an error because there are no words in the list:

```
words 1 thru 3 of {1, 2, 3} --result: an error
```

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_227"></a>

##### Examples

The following example shows the boundary object form of a range specifier. When you compile this statement, Script Editor converts `from integer 1 to integer 2` to the form `integers 1 thru 2`.

```
set intList to integers from integer 1 to integer 2 of {17, 33, 24}
     --result: {17, 33}
```

In the next example, the phrase `folders 3 thru 4` is a range specifier that specifies a list of two folders in the container `startup disk`:

```
tell application "Finder"
    folders 3 thru 4 of startup disk
end tell
--result: a list of folders (depends on contents of startup disk)
```

##### Discussion

If you specify a range specifier as the container for a property or object, as in

```
name of folders 2 thru 3 of startup disk
```

the result is a list containing the specified property or object for each object of the container. The number of items in the list is the same as the number of objects in the container.

To obtain a contiguous series of characters—instead of a list—from a `text` object, use the `text` class:

```
text from word 1 to word 4 of "We're all in this together"
--result: "We're all in this"
words 1 thru 4 of "We're all in this together"
--result: {"We're", "all", "in", "this"}
```

<a id="//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH4g-123374"></a>Relative

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1115"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1116"></a>

Specifies an object or an insertion point in a container by describing a position in relation to another object, known as the base, in the same container.

##### Syntax

|  |
| --- |
| ```  [ class ] ( before \| [in] front of ) baseSpecifier  [ class ] ( after \| [in] back of \| behind ) baseSpecifier         ``` |

##### Placeholders

*class*
:   The class identifier of the specified object. If you omit this parameter, the specifier refers to an insertion point.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1124"></a>

*baseSpecifier*
:   A specifier for the object.

`before` | `[in] front of`
:   These forms are equivalent, and refer to the object immediately preceding the base object.

`after` | `[in] back of` | `behind`
:   These forms are equivalent, and refer to the object immediately after the base.

`beginning | front`
:   These forms are equivalent, and refer to the first insertion point of the container (`insertion point 1`). <a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1125"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1126"></a>

`end | back`
:   These forms are equivalent, and refer to the last insertion point of the container (`insertion point -1`). <a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1127"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1128"></a><a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1129"></a> Although terms such as `beginning` and `end` sound like absolute positions, they are relative to the existing contents of a container (that is, before or after the existing contents).

<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_228"></a>

##### Examples

The two relative specifiers in the following `tell` block specify the same file by identifying its position relative to another file on a disk:

```
tell application "Finder"
    item before item 3 of startup disk --result: e.g., a specifier
    item after item 1 of startup disk --result: e.g., a specifier
end tell
```

The following example shows how to use various relative specifiers in a word processing document:

```
tell first document of application "TextEdit"
    copy word 1 to before paragraph 3
    copy word 3 to in back of paragraph 4
    copy word 1 of the last paragraph to behind the third paragraph
end tell
```

##### Discussion

The `relative` reference form generally works only when the `index` form also works.

You can specify only a single object with a relative specifier—an object that is either before or after the base object.<a id="//apple_ref/doc/uid/TP40000983-CH4g-DontLinkElementID_1130"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
