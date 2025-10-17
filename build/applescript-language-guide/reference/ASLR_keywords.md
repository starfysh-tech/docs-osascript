<a id="//apple_ref/doc/uid/TP40000983-CH222-SW2"></a>

# AppleScript Keywords

<a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_967"></a><a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_968"></a><a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_969"></a>This appendix lists AppleScript keywords (or *reserved words*), provides a brief description for each, and points to related information, where available. (See also [Keywords](../conceptual/ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW7) in [AppleScript Lexical Conventions](../conceptual/ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW1).)

The keywords in [Table A-1](#//apple_ref/doc/uid/TP40000983-CH222-SW1) are part of the AppleScript language. You should not attempt to reuse them in your scripts for variable names or other purposes. Developers should not re-define keywords in the terminology for their scriptable applications. You can view many additional scripting terms defined by Apple, but not part of the AppleScript language, in [AppleScript Terminology and Apple Event Codes](http://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html).

<a id="//apple_ref/doc/uid/TP40000983-CH222-SW1"></a>

**Table A-1**  AppleScript reserved words, with descriptions

| `about` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `above` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `after` | used to describe position in the [Relative](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI) reference form; used as part of operator (`comes after`, `does not come after`) with classes such as `date`, `integer`, and `text` |
| `against` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `and` | logical *and* operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `apart from` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `around` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `as` | coercion operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `aside from` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `at` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `back` | used with [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) and [Relative](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI) reference forms; `in back of` is synonymous with `after` and `behind` |
| `before` | used to describe position in the [Relative](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI) reference form; used as an operator (`comes before`, `does not come before`) with classes such as `date`, `integer`, and `text`; synonymous with `in front of` |
| `beginning` | specifies an insertion location at the beginning of a container—see the boundary specifier descriptions for the [Range](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ) reference form |
| `behind` | synonymous with `after` and `in back of` |
| `below` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `beneath` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `beside` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `between` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `but` | used in [considering and ignoring Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-130224) |
| `by` | used with binary containment operator `contains, is contained by`; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `considering` | a control statement—see [considering and ignoring Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-130224) |
| `contain, contains` | binary containment operator—see `contains, is contained by` |
| `continue` | changes the flow of execution—see `continue` |
| `copy` | an AppleScript command—see `copy` |
| `div` | division operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `does` | used with operators such as `does not equal`, `does not come before`, and `does not contain`—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `eighth` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `else` | used with `if` control statement—see [if Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-158244) |
| `end` | marks the end of a script or handler definition, or of a compound statement, such as a `tell` or `repeat` statement; also specifies an insertion location at the end of a container—see the boundary specifier descriptions for the [Range](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ) reference form |
| `equal, equals` | binary comparison operator—see `equal, is not equal to` |
| `error` | `error` control statement; also used with`try` statement |
| `every` | specifies every object in a container—see [Every](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCJFIIH) reference form |
| `exit` | terminates a `repeat` loop—see `exit` |
| `false` | a Boolean literal—see [Boolean](../conceptual/ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW14) |
| `fifth` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `first` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `for` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `fourth` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `from` | used in specifying a range of objects in a container—see [Range](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ) reference form; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `front` | `in front of` is used to describe position in the [Relative](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI) reference form; synonymous with `before` |
| `get` | an AppleScript command—see `get` |
| `given` | a special handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `global` | specifies the scope for a variable (see also `local`)—see [Global Variables](../conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW13) |
| `if` | a control statement—see [if Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-158244) |
| `ignoring` | a control statement—see [considering and ignoring Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-130224) |
| `in` | used in construction object specifiers—see [Containers](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW24); also used with the [Relative](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHGEDI) reference form—for example `in front of` and `in back of` |
| `instead of` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `into` | `put into` is a deprecated synonym for the `copy` command; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `is` | used with various comparison operators—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `it` | refers to the current target (`of it`)—see [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4) |
| `its` | synonym for `of it`—see [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4) |
| `last` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `local` | specifies the scope for a variable (see also `global`)—see [Local Variables](../conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW12) |
| `me` | refers to the current script (`of me`)—see [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4) |
| `middle` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `mod` | remainder operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `my` | synonym for `of me`—see [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4) |
| `ninth` | specifies a position in a container—see [Middle](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCJFDBA) reference form |
| `not` | logical negation operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `of` | used in construction object specifiers—see [Containers](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW24); used with or as part of many other terms, including `of me` , `in front of` , and so on |
| `on` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `onto` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `or` | logical *or* operator—see [Table 9-1](ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-SW2) |
| `out of` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `over` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `prop, property` | `prop` is an abbreviation for `property`—see [The it and me Keywords](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4) |
| `put`<a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_970"></a> | `put into` is a deprecated synonym for the `copy` command |
| `ref/reference` | `ref` is an abbreviation for `reference`—see `reference` |
| `repeat` | a control statement—see [repeat Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-127362) |
| `return` | exits from a handler—see `return` |
| `returning`<a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_971"></a> | deprecated |
| `script` | used to declare a script object; also the class of a script object—see the `script` class and [Script Objects](../conceptual/ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-BAJJCIAA) |
| `second` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `set` | an AppleScript command—see `set` |
| `seventh` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `since` | handler parameter label—see [Handler Syntax (Labeled Parameters)](ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-SW2) |
| `sixth` | specifies an index position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `some` | specifies an object in a container—see [Arbitrary](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BCIJEEHE) reference form |
| `tell` | a control statement—see [tell Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-158637) |
| `tenth` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `that` | synonym for `whose` |
| `the`<a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_972"></a> | syntactic no-op, used to make script statements look more like natural language |
| `then` | used with `if` control statement—see [if Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-158244) |
| `third` | specifies a position in a container—see [Index](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCGHGAF) reference form |
| `through, thru` | used in specifying a range of objects in a container—see [Range](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ) reference form |
| `timeout` | used with `with timeout` control statement—see `with timeout` |
| `times` | used with `repeat` control statement—see `repeat (number) times` |
| `to` | used in many places, including `copy` and `set` commands; in the [Range](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BBCHDJJJ) reference form; by operators such as `is equal to` and `a reference to`; with the control statement `repeat with loopVariable (from startValue to stopValue)`; with the partial result parameter in [try Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-128973) |
| `transaction` | used with `with transaction` control statement—see `with transaction` |
| `true` | a Boolean literal—see [Boolean](../conceptual/ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW14) |
| `try` | an error-handling statement—see [try Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-128973) |
| `until` | used with `repeat` control statement—see `repeat until` |
| `use` | a requirement statement—see [use Statements](ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-SW4) |
| `where` | used with the [Filter](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BAJJHEFE) reference form to specify a Boolean test expression (synonymous with `whose`) |
| `while` | used with `repeat` control statement—see `repeat while` |
| `whose` | used with the [Filter](ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BAJJHEFE) reference form to specify a Boolean test expression (synonymous with `where`) |
| `with` | used in commands to specify various kinds of parameters, including `true` for some Boolean for parameters—see, for example, the `with prompt` and `multiple selections allowed` parameters to the `choose from list` command; also used with application `make` commands to specify properties (`with properties`) |
| `without` | used in commands to specify `false` for a Boolean for a parameter—see, for example, the `multiple selections allowed` parameter to the `choose from list` command<a id="//apple_ref/doc/uid/TP40000983-CH222-DontLinkElementID_973"></a> |

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
