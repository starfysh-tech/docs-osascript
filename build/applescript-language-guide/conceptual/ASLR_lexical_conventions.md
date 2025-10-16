<a id="//apple_ref/doc/uid/TP40000983-CH214-SW1"></a>

# AppleScript Lexical Conventions

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_396"></a>This chapter provides an overview of the vocabulary and conventions of the AppleScript Language. It starts with the character set and introduces elements of increasing complexity.

After reading this chapter, you should have an understanding of the basic language components used to construct AppleScript expressions and statements.

AppleScript Lexical Conventions contains the following sections:

* [Character Set](#//apple_ref/doc/uid/TP40000983-CH214-SW3)
* [Identifiers](#//apple_ref/doc/uid/TP40000983-CH214-SW4)
* [Keywords](#//apple_ref/doc/uid/TP40000983-CH214-SW7)
* [Comments](#//apple_ref/doc/uid/TP40000983-CH214-SW8)
* [The Continuation Character](#//apple_ref/doc/uid/TP40000983-CH214-SW9)
* [Literals and Constants](#//apple_ref/doc/uid/TP40000983-CH214-SW10)
* [Operators](#//apple_ref/doc/uid/TP40000983-CH214-SW18)
* [Variables](#//apple_ref/doc/uid/TP40000983-CH214-SW23)
* [Expressions](#//apple_ref/doc/uid/TP40000983-CH214-SW20)
* [Statements](#//apple_ref/doc/uid/TP40000983-CH214-SW17)
* [Commands](#//apple_ref/doc/uid/TP40000983-CH214-SW6)
* [Results](#//apple_ref/doc/uid/TP40000983-CH214-SW19)
* [Raw Codes](#//apple_ref/doc/uid/TP40000983-CH214-SW5)

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW3"></a>

## Character Set

Starting in OS X v10.5 (AppleScript 2.0), <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_397"></a>the character set for AppleScript is Unicode. AppleScript preserves all characters correctly worldwide, and comments and text constants in scripts may contain any Unicode characters.

AppleScript syntax uses several non-ASCII characters, which can be typed using special key combinations. For information on characters that AppleScript treats specially, see the sections [Identifiers](#//apple_ref/doc/uid/TP40000983-CH214-SW4), [Comments](#//apple_ref/doc/uid/TP40000983-CH214-SW8), [Text](#//apple_ref/doc/uid/TP40000983-CH214-SW26), [The Continuation Character](#//apple_ref/doc/uid/TP40000983-CH214-SW9), and [Raw Codes](#//apple_ref/doc/uid/TP40000983-CH214-SW5) in this chapter, as well as [Table 9-1](../reference/ASLR_operators.md#//apple_ref/doc/uid/TP40000983-CH5g-SW2) in [Operators Reference](../reference/ASLR_operators.md#//apple_ref/doc/uid/TP40000983-CH5g-124070).

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW4"></a>

## Identifiers

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_398"></a>An AppleScript *identifier* is a series of characters that identifies a class name, variable, or other language element, such as labels for properties and handlers.

An identifier must begin with a letter and can contain any of these characters:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_
```

Identifiers are not case sensitive. For example, the identifiers `myvariable` and `MyVariable` are equivalent.

AppleScript remembers and enforces the first capitalization it comes across for an identifier. So if it first encounters an identifier as `myAccount`, it will later, during compilation, change versions such as `MyAccount` and `myaccount` to `myAccount`.

The following are examples of valid identifiers: `areaOfCircle`, `Agent007`, `axis_of_rotation`.

The following are not valid identifiers: `C-`, `back&forth`, `999`, `Why^Not`.

AppleScript provides a loophole to the preceding rules: identifiers whose first and last characters are vertical bars (|) can contain any characters. The leading and trailing vertical bars are not considered part of the identifier.<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_399"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_400"></a>

> <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_11"></a>
>
> **Important:** This use of vertical bars can make scripts difficult to read, and is not recommended.

The following are legal identifiers: `|back&forth|`, `|Right*Now!|`.<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_401"></a>

An identifier can contain additional vertical bars preceded by a backslash (\) character, as in the identifier `|This\|Or\|That|`. Use of the backslash character is described further in the Special String Characters section of the `text` class.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW7"></a>

## Keywords

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_402"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_403"></a>A *keyword* is a reserved word in the AppleScript language. Keywords consist of lower-case, alphabetic characters: `abcdefghijklmnopqrstuvwxyz`. In a few cases, such as `aside from`, they come in pairs.

> <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_12"></a>
>
> **Important:** You should not attempt to reuse keywords in your scripts for variable names or other purposes. Developers should not re-define keywords in the terminology for their scriptable applications.

Table 1-1 lists the keywords reserved in AppleScript 2.0 (which are the same as those used in AppleScript 1.x). For additional information, see [Table A-1](../reference/ASLR_keywords.md#//apple_ref/doc/uid/TP40000983-CH222-SW1), which provides a brief description for each keyword and points to related information, where available.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW2"></a>

**Table 1-1**  AppleScript reserved words, listed alphabetically

| `about` | `above` | `after` | `against` | `and` | `apart from` |
| `around` | `as` | `aside from` | `at` | `back` | `before` |
| `beginning` | `behind` | `below` | `beneath` | `beside` | `between` |
| `but` | `by` | `considering` | `contain` | `contains` | `contains` |
| `continue` | `copy` | `div` | `does` | `eighth` | `else` |
| `end` | `equal` | `equals` | `error` | `every` | `exit` |
| `false` | `fifth` | `first` | `for` | `fourth` | `from` |
| `front` | `get` | `given` | `global` | `if` | `ignoring` |
| `in` | `instead of` | `into` | `is` | `it` | `its` |
| `last` | `local` | `me` | `middle` | `mod` | `my` |
| `ninth` | `not` | `of` | `on` | `onto` | `or` |
| `out of` | `over` | `prop` | `property` | `put` | `ref` |
| `reference` | `repeat` | `return` | `returning` | `script` | `second` |
| `set` | `seventh` | `since` | `sixth` | `some` | `tell` |
| `tenth` | `that` | `the` | `then` | `third` | `through` |
| `thru` | `timeout` | `times` | `to` | `transaction` | `true` |
| `try` | `until` | `where` | `while` | `whose` | `with` |
| `without` | `` | `` | `` | `` | `` |

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW8"></a>

## Comments

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_404"></a>A *comment* is text that is ignored by AppleScript when a script is executed. You can use comments to describe what is happening in the script or make other kinds of notes. There are three kinds of comments:

* <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_405"></a>A block comment begins with the characters `(*` and ends with the characters `*)`. Block comments must be placed between other statements. That means they can be placed on the same line at the beginning or end of a statement, but cannot be embedded within a simple (one-line) statement.
* <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_406"></a>An end-of-line comment begins with the characters `--` (two hyphens) and ends with the end of the line:

  ```
  --end-of-line comments extend to the end of the line
  ```
* Starting in version 2.0, AppleScript also supports use of the # symbol as an end-of-line comment. This allows you to make a plain AppleScript script into a <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_407"></a>Unix executable by beginning it with the following line and giving it execute permission:

  ```
  #!/usr/bin/osascript
  ```

  Compiled scripts that use `#` will run normally on pre-2.0 systems, and if edited will display using `--`. Executable text scripts using `#!/usr/bin/osascript` will not run on pre-2.0 systems, since the `#` will be considered a syntax error.

You can nest comments—that is, comments can contain other comments, as in this example:

```
(*  Here are some
    --nested comments
    (* another comment within a comment *)
*)
```

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW9"></a>

## The Continuation Character

A simple AppleScript statement must normally be entered on a single line. You can extend a statement to the next line by ending it with the *<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_408"></a>continuation character*, ¬. With a U.S. keyboard, you can enter this character by typing Option-l (lower-case L). In Script Editor, you can type Option-Return, which inserts the continuation character and moves the insertion point to the next line.

Here is a single statement displayed on two lines:

```
display dialog "This is just a test." buttons {"Great", "OK"} ¬
default button "OK" giving up after 3
```

A continuation character within a quoted text string is treated like any other character.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW10"></a>

## Literals and Constants

A <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_409"></a>*literal* is a value that evaluates to itself—that is, it is interpreted just as it is written. In AppleScript, for example, `"Hello"` is a text literal. A <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_410"></a>*constant* is a word with a predefined value. For example, AppleScript defines a number of enumerated constants for use with the `path to (folder)` command, each of which specifies a location for which to obtain the path.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW14"></a>

### Boolean

AppleScript defines the <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_411"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_412"></a>Boolean values `true` and `false` and supplies the `boolean` class.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW13"></a>

### Constant

[Global Constants in AppleScript](ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-BAJBDEJI) describes constants that can be used throughout your scripts. For related information, see the `constant` class.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW15"></a>

### List

A list defines an ordered collection of values, known as items, of any class. As depicted in a script, a list consists of a series of expressions contained within braces and separated by commas, such as the following:

```
{1, 7, "Beethoven", 4.5}
```

A list can contain other lists. An empty list (containing no items) is represented by a pair of empty braces: `{}`.

AppleScript provides the `list` class for working with lists.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW12"></a>

### Number

A <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_413"></a>numeric literal is a sequence of digits, possibly including other characters, such as a unary minus sign, period (in reals), or `"E+"` (in exponential notation). The following are some numeric literals:

```
-94596
3.1415
9.9999999999E+10
```

AppleScript defines classes for working with `real` and `integer` values, as well as the `number` class, which serves as a synonym for either `real` or `integer`.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW16"></a>

### Record

A record is an unordered collection of labeled properties. A record appears in a script as a series of property definitions contained within braces and separated by commas. Each property definition consists of a unique label, a colon, and a value for the property. For example, the following is a record with two properties:

```
{product:"pen", price:2.34}
```

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW26"></a>

### Text

A <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_414"></a>`text` literal consists of a series of Unicode characters enclosed in a pair of double quote marks, as in the following example:

```
"A basic string."
```

AppleScript `text` objects are instances of the `text` class, which provides mechanisms for working with text. The Special String Characters section of that class describes how to use white space, backslash characters, and double quotes in text.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW18"></a>

## Operators

An *operator* is a symbol, word, or phrase that derives a value from another value or pair of values. For example, the multiplication operator (`*`) multiplies two numeric operands, while the concatenation operator (`&`) joins two objects (such as text strings). The `is equal` operator performs a test on two Boolean values.

For detailed information on AppleScript’s operators, see [Operators Reference](../reference/ASLR_operators.md#//apple_ref/doc/uid/TP40000983-CH5g-124070).

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW23"></a>

## Variables

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_415"></a>A *variable* is a named container in which to store a value. Its name, which you specify when you create the variable, follows the rules described in [Identifiers](#//apple_ref/doc/uid/TP40000983-CH214-SW4). You can declare and initialize a variable at the same time with a `copy` or `set` command. For example:

```
set myName to "John"
copy 33 to myAge
```

Statements that assign values to variables are known as <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_416"></a>*assignment statements*.

When AppleScript encounters a variable, it evaluates the variable by getting its value. A variable is contained in a script and its value is normally lost when you close the script that contains it.

AppleScript variables can hold values of any class. For example, you can assign the integer value `17` to a variable, then later assign the Boolean value `true` to the same variable.<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_417"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_418"></a>

For more information, see [Variables and Properties](ASLR_variables.md#//apple_ref/doc/uid/TP40000983-CH223-SW10).

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW20"></a>

## Expressions

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_419"></a>An *expression* is any series of lexical elements that has a value. Expressions are used in scripts to represent or derive values. The simplest kinds of expressions, called literal expressions, are representations of values in scripts. More complex expressions typically combine literals, variables, operators, and object specifiers.

When you run a script, AppleScript converts its expressions into values. This process is known as *evaluation*. For example, when the following simple expression is evaluated, the result is 21:<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_420"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_421"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_422"></a>

```
3 * 7 --result: 21
```

An object specifier<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_423"></a> specifies some or all of the information needed to find another object. For example, the following object specifier specifies a named document:

```
document named "FavoritesList"
```

For more information, see [Object Specifiers](ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW7).

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW17"></a>

## Statements

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_424"></a>A *statement* is a series of lexical elements that follows a particular AppleScript syntax. Statements can include keywords, variables, operators, constants, expressions, and so on.

Every script consists of statements. When AppleScript executes a script, it reads the statements in order and carries out their instructions.

A *control statement* is a statement that determines when and how other statements are executed. AppleScript defines standard control statements such as `if`, `repeat`, and `while` statements, which are described in detail in [Control Statements Reference](../reference/ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-157332).

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_425"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_426"></a> A *simple statement* is one that can be written on a single line:

```
set averageTemp to 63 as degrees Fahrenheit
```

> <a id="//apple_ref/doc/uid/TP40000983-CH214-SW11"></a>
>
> **Note:** You can use a continuation character (¬) to extend a simple statement onto a second line.

<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_427"></a><a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_428"></a> A *compound statement* is written on more than one line, can contain other statements, and has the word `end` (followed, optionally, by the first word of the statement) in its last line. For example the following is a compound `tell` statement:

```
tell application "Finder"
    set savedName to name of front window
    close window savedName
end tell
```

A compound statement can contain other compound statements.

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW6"></a>

## Commands

A *command* is a word or series of words used in an AppleScript statement to request an action. Every command is directed at a *target*, which is the object that responds to the command. The target is usually an application object or an object in macOS, but it can also be a `script` object or a value in the current script.

The following statement uses AppleScript’s `get` command to obtain the name of a window; the target is the front window of the Finder application:

```
get name of front window of application "Finder"
```

For more information on command types, parameters, and targets, see [Commands Overview](ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW8).

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW19"></a>

## Results

The <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_429"></a>*result* of a statement is the value generated, if any, when the statement is executed. For example, executing the statement `3 + 4` results in the value `7`. The result of the statement `set myText to "keyboard"` is the text object `"keyboard"`. A result can be of any class. AppleScript stores the result in the globally available property <a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_430"></a>`result`, described in [AppleScript Constant](ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW38).<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_431"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH214-SW5"></a>

## Raw Codes

When you open, compile, edit, or run scripts with a script editor, you may occasionally see terms enclosed in double angle brackets, or chevrons<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_432"></a> («»), in a script window or in another window. These terms are called *raw format* or *raw codes*, because they represent the underlying Apple event codes<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_433"></a> that AppleScript uses to represent scripting terms.

For compatibility with Asian national encodings, “《” and “》” are allowed as synonyms for “«” and “»” ( (Option- \ and Option-Shift- \, respectively, on a U.S. keyboard), since the latter do not exist in some Asian encodings.

For more information on raw codes, see [Double Angle Brackets](ASLR_raw_data.md#//apple_ref/doc/uid/TP40000983-CH225-SW1).<a id="//apple_ref/doc/uid/TP40000983-CH214-DontLinkElementID_434"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
