<a id="//apple_ref/doc/uid/TP40000983-CH5g-124070"></a>

# Operators Reference

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_977"></a>This chapter describes AppleScript operators. An *operator* is a symbol, word, or phrase that derives a value from another value or pair of values. An *operation* is the evaluation of an expression that contains an operator. An *operand* is an expression from which an operator derives a value.

AppleScript provides logical and mathematical operators, as well as operators for containment, concatenation, and obtaining a reference to an object. Operators that operate on two values are called *<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_978"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_979"></a>binary operators*, while operators that operate on a single value are known as *<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_980"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_981"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_982"></a>unary operators*.

The first part of this chapter contains two tables: Table 9-1 summarizes all of the operators that AppleScript uses, and [Table 9-2](#//apple_ref/doc/uid/TP40000983-CH5g-SW3) shows the order in which AppleScript evaluates operators within expressions. The rest of the chapter shows how AppleScript evaluates representative operators in script expressions.<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_983"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW2"></a>

**Table 9-1**  AppleScript operators

| AppleScript operator | Description |
| `and`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_984"></a> | Logical conjunction.  A binary logical operator that combines two Boolean values. The result is `true` only if both operands evaluate to `true`.  AppleScript checks the left-hand operand first and, if its is `false`, ignores the right-hand operand. (This behavior is called <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_985"></a>short-circuiting.)  Class of operands: `boolean`  Class of result: `boolean` |
| `or`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_986"></a> | Logical disjunction.  A binary logical operator that combines two Boolean values. The result is `true` if either operand evaluates to `true`.  AppleScript checks the left-hand operand first and, if its is `true`, ignores the right-hand operand. (This behavior is called short-circuiting.)  Class of operands: `boolean`  Class of result: `boolean` |
| `&`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_987"></a> | <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_988"></a>Concatenation.  A binary operator that joins two values. If the left-hand operand is a `text` object, the result is a `text` object (and only in this case does AppleScript try to coerce the value of the right-hand operand to match that of the left).  If the operand to the left is a record, the result is a record. If the operand to the left belongs to any other class, the result is a list.  For more information, see `& (concatenation)`.  Class of operands: any  Class of result: `list`, `record`, `text` |
| `=`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_989"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_990"></a>  `is<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_991"></a> equal`  `equals`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_992"></a>  `[is] equal to` | Equality.  A binary comparison operator that results in `true` if both operands have the same value. The operands can be of any class.  For more information, see `equal, is not equal to`.  Class of operands: `boolean`  Class of result: `boolean` |
| `≠` (Option-equal sign on U.S. keyboard)  `is not`  `isn't`  `isn't equal [to]`  `is not equal [to]`  `doesn't equal`  `does not equal`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_993"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_994"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_995"></a> | Inequality.  A binary comparison operator that results in `true` if its two operands have different values. The operands can be of any class.  For more information, see `equal, is not equal to`.  Class of operands: `boolean`  Class of result: `boolean` |
| `>`  `[is] greater than`  `comes after`  `is not less than or equal [to]`  `isn't less than or equal [to]`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_996"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_997"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_998"></a> | Greater than.  A binary comparison operator that results in `true` if the value of the left-hand operand is greater than the value of the right-hand operand.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the left-hand operand.  For more information, see `greater than, less than`.  Class of operands: `date`, `integer`, `real`, `text`  Class of result: `boolean` |
| `<`  `[is] less than`  `comes before`  `is not greater than or equal [to]`  `isn't greater than or equal [to]`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_999"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1000"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1001"></a> | Less than.  A binary comparison operator that results in `true` if the value of the left-hand operand is less than the value of the right-hand operand.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  For more information, see `greater than, less than`.  Class of operands: `date`, `integer`, `real`, `text`  Class of result: `boolean` |
| `≥` (Option-period on U.S. keyboard)  `>=`  `[is] greater than or equal [to]`  `is not less than`  `isn't less than`  `does not come before`  `doesn't come before`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1002"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1003"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1004"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1005"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1006"></a> | Greater than or equal to.  A binary comparison operator that results in `true` if the value of the left-hand operand is greater than or equal to the value of the right-hand operand.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  The method AppleScript uses to determine which value is greater depends on the class of the operands.  Class of operands: `date`, `integer`, `real`, `text`  Class of result: `boolean` |
| `≤` (Option-comma on U.S. keyboard)  `<=`  `[is] less than or equal [to]`  `is not greater than`  `isn't greater than`  `does not come after`  `doesn't come after`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1007"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1008"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1009"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1010"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1011"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1012"></a> | Less than or equal to.  A binary comparison operator that results in `true` if the value of the left-hand operand is less than or equal to the value of the right-hand operand.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  The method AppleScript uses to determine which value is greater depends on the class of the operands.  Class of operands: `date`, `integer`, `real`, `text`  Class of result: `boolean` |
| `start[s] with`  `begin[s] with`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1013"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1014"></a> | Starts with.  A binary containment operator that results in `true` if the list or `text` object to its right matches the beginning of the list or `text` object to its left.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  For more information, see `starts with, ends with`.  Class of operands: `list`, `text`  Class of result: `boolean` |
| `end[s] with`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1015"></a> | Ends with.  A binary containment operator that results in `true` if the list or `text` object to its right matches the end of the list or `text` object to its left.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  For more information, see `starts with, ends with`.  Class of operands: `list`, `text`  Class of result: `boolean` |
| `contain[s]`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1016"></a> | Containment.  A binary containment operator that results in `true` if the list, record, or `text` object to its right matches any part of the list, record, or `text` object to its left.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.  For more information, see `contains, is contained by`.  Class of operands: `list`, `record`, `text`  Class of result: `boolean` |
| <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1017"></a>`does not contain`  `doesn't contain` | Non-containment.  A binary containment operator that results in `true` if the list, record, or `text` object to its right does not match any part of the list, record, or `text` object to its left.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the right-hand operand to the class of the left-hand operand.  For more information, see `contains, is contained by`.  Class of operands: `list`, `record`, `text`  Class of result: `boolean` |
| <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1018"></a>`is in`  `is contained by` | Containment.  A binary containment operator that results in `true` if the list, record, or `text` object to its left matches any part of the list, record, or `text` object to its right.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the left-hand operand to the class of the right-hand operand.  For more information, see `contains, is contained by`.  Class of operands: `list`, `record`, `text`  Class of result: `boolean` |
| <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1019"></a>`is not in`  `is not contained by`  `isn't contained by` | Non-containment.  A binary containment operator that results in `true` if the list, record, or `text` object to its left does not match any part of the list, record, or `text` object to its right.  Both operands must evaluate to values of the same class. If they don’t, AppleScript attempts to coerce the left-hand operand to the class of the right-hand operand.  For more information, see `contains, is contained by`.  Class of operands: `list`, `record`, `text`  Class of result: `boolean` |
| `*`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1020"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1021"></a> | Multiplication.  A binary arithmetic operator that multiplies the number to its left and the number to its right.  Class of operands: `integer`, `real`  Class of result: `integer`, `real` |
| `+`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1022"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1023"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1024"></a> | Addition.  A binary arithmetic operator that adds the number or date to its left and the number or date to its right. Only integers can be added to dates. AppleScript interprets such an integer as a number of seconds.  As a unary operator, `+` has no effect and is removed on compile.  Class of operands: `date`, `integer`, `real`  Class of result: `date`, `integer`, `real` |
| `–` | Subtraction.  A binary or unary arithmetic operator.  The binary operator subtracts the number to its right from the number or date to its left.  The unary operator makes the number to its right negative.  Only integers can be subtracted from dates. AppleScript interprets such an integer as a number of seconds.  Class of operands: `date`, `integer`, `real`  Class of result: `date`, `integer`, `real`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1025"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1026"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1027"></a> |
| `/`  `÷` (Option-slash on U.S. keyboard) | Division.  A binary arithmetic operator that divides the number to its left by the number to its right.  Class of operands: `integer`, `real`  Class of result: `real`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1028"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1029"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1030"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1031"></a> |
| `div` | Integral division.  A binary arithmetic operator that divides the number to its left by the number to its right and returns the integral part of the answer as its result.  Class of operands: `integer`, `real`  Class of result: `integer`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1032"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1033"></a> |
| `mod` | Remainder.  A binary arithmetic operator that divides the number to its left by the number to its right and returns the remainder as its result.  Class of operands: `integer`, `real`  Class of result: `integer`, `real`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1034"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1035"></a> |
| `^` | Exponentiation.  A binary arithmetic operator that raises the number to its left to the power of the number to its right.  Class of operands: `integer`, `real`  Class of result: `real`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1036"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1037"></a> |
| `as` | Coercion (or *object conversion*).  A binary operator that converts the left-hand operand to the class listed to its right.  Not all values can be coerced to all classes. The coercions that AppleScript can perform are listed in [Coercion (Object Conversion)](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW21). The additional coercions, if any, that an application can perform is listed in its dictionary.  Class of operands: The right-hand operand must be a class identifier or list of class identifiers; the left-hand operand must be a value that can be converted to that class or one of the listed classes.  Class of result: The class specified by the class identifier to the right of the operator <a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1038"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1039"></a> |
| `not` | Negation.  A unary logical operator that results in `true` if the operand to its right is `false`, and `false` if the operand is `true`.  Class of operand: `boolean`  Class of result: `boolean`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1040"></a> |
| `[a] (ref [to] | reference to)` | A reference to.  A unary operator that causes AppleScript to return a `reference` object that specifies the location of the operand to its right. A reference is evaluated at run time, not at compile time.  See `a reference to` for more information.  Class of operand: any class type  Class of result: `reference`<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1041"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1042"></a> |

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1043"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1044"></a>When evaluating expressions, AppleScript uses operator precedence to determine which operations are evaluated first. In the following expression, for example, AppleScript does not simply perform operations from left to right—it performs the multiplication operation `2 * 5` first, because multiplication has higher precedence than addition.

```
12 + 2 * 5 --result: 22
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1045"></a>[Table 9-2](#//apple_ref/doc/uid/TP40000983-CH5g-SW3) shows the order in which AppleScript performs operations. The column labeled “Associativity” indicates the order in the case where there are two or more operands of the same precedence in an expression. The word “None” in the Associativity column indicates that you cannot have multiple consecutive occurrences of the operation in an expression. For example, the expression `3 = 3 = 3` is not legal because the associativity for the equal operator is “none.”

To evaluate expressions with multiple unary operators of the same order, AppleScript applies the operator closest to the operand first, then applies the next closest operator, and so on. For example, the expression `not not not true` is evaluated as `not (not (not true))`.

You can enforce the order in which AppleScript performs operations by grouping expressions in parentheses, which are evaluated first, starting with the innermost pair of parentheses.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW3"></a>

**Table 9-2**  Operator precedence

| Order | Operators | Associativity | Type of operator |
| 1 | `( )` | Innermost to outermost | Grouping |
| 2 | `+`  `–` | Unary | Plus or minus sign for numbers |
| 3 | `^` | Right to left | Exponentiation  (note that this is different from standard math, in which exponentiation takes precedence over unary plus or minus) |
| 4 | `*`  `/`  `div`  `mod` | Left to right | Multiplication and division |
| 5 | `+`  `–` | Left to right | Addition and subtraction |
| 6 | `&` | Left to right | Concatenation |
| 7 | `as` | Left to right | Coercion |
| 8 | `<`  `≤`  `>`  `≥` | None | Comparison |
| 9 | `=`  `≠` | None | Equality and inequality |
| 10 | `not` | Unary | Logical negation |
| 11 | `and` | Left to right | Logical and |
| 12 | `or` | Left to right | Logical or |

The following sections provide additional detail about how AppleScript evaluates operators in expressions:

* `& (concatenation)`
* `a reference to`
* Para
* `contains, is contained by`
* `equal, is not equal to`
* `greater than, less than`
* `starts with, ends with`

<a id="//apple_ref/doc/uid/TP40000983-CH5g-BAJEGEEC"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1046"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125281"></a>& (concatenation)

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1047"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1048"></a>The concatenation operator (`&`) concatenates `text` objects, joins `record` objects into a record, and joins other objects into a list.

[Table 9-1](#//apple_ref/doc/uid/TP40000983-CH5g-SW2) summarizes the use of use of this operator.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125314"></a>

##### text

The concatenation of two `text` objects joins the characters from the left-hand `text` object to the characters from the right-hand `text` object, without intervening spaces. For example, `"dump" & "truck"` evaluates to the `text` object `"dumptruck"`.

If the left-hand operand is a `text` object, but the right-hand operand is not, AppleScript attempts to coerce the right-hand operand to a `text` object. For example, when AppleScript evaluates the expression `"Route " & 66` it coerces the integer `66` to the `text` object `"66"`, and the result is the `text` object `"Route 66"`.

However, you get a different result if you reverse the order of the operands:

```
66 & "Route " --result: {66, "Route "} (a list)
```

In the following example, the left-hand operand is a `text` object and the right-hand operand is a list, so concatenation results in a `text` object:

```
item 1 of {"This"} & {"and", "that"} -- "Thisandthat"
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125417"></a>

##### record

The concatenation of two records joins the properties of the left-hand record to the properties of the right-hand record. If both records contain properties with the same name, the value of the property from the left-hand record appears in the result. For example, the result of the expression

```
{ name:"Matt", mileage:"8000" } & { name:"Steve", framesize:58 }
```

is

```
{ name:"Matt", mileage:"8000", frameSize:58 }
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125467"></a>

##### All Other Classes

Except for the cases described above for `text` objects and `record` objects, the concatenation operator (`&`) joins lists. A non-list operand is considered to be a list containing that operand. The following example shows concatenation of two integers, a list and a text string, and a list and a record, respectively:

```
1 & 2 --result: {1, 2}
{"this"} & "hello" --result: {"this", "hello"}
{"this"} & {a:1, b:2} --result: {"this", 1, 2}
```

If both the operands to be concatenated are lists, then the result is a list containing all the items in the left-hand list, followed by all the items in the right-hand list. For example:

```
{"This"} & {"and", "that"} --result: {"This", "and", "that"}
{"This"} & item 1 of {"and", "that"} --result: {"This", "and"}
```

To join two lists and create a list of lists, rather than a single list, you can enclose each list in two sets of brackets:

```
{{1, 2}} & {{3, 4}} --result: {{1, 2}, {3, 4}}
```

For information on working efficiently with large lists, see `list`.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW1"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1049"></a>

a reference to

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1050"></a>The `a reference to` operator is a unary operator that returns a `reference` object. You can abbreviate this operator to `a ref to`, or `ref to`, or even just `ref`.

For related information, see the `reference` class and [Object Specifiers](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW7).

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW4"></a>

##### Examples

The following statement creates a `reference` object that contains an object specifier to the Finder startup disk:

```
tell app "Finder" to set diskRef to a ref to startup disk
--result: startup disk of application "Finder"
```

The following shows how to obtain a reference object that refers to an item in a list:

```
set itemRef to a reference to item 3 of {1, "hello", 755, 99}
    --result: item 3 of {1, "hello", 755, 99}
set newTotal to itemRef + 45 --result: 800
```

In the final line, AppleScript automatically resolves the object specifier contained in the reference `itemRef` and obtains its value to use in the addition operation. To cause AppleScript to explicitly resolve a `reference` object, you can use its `contents` property:

```
contents of itemRef --result: 755
```

The next examples demonstrate how using a reference object can result in a different outcome than accessing an object directly. The first example obtains a current track object from iTunes, gets the name, changes the track, then gets the name again:

```
tell application "iTunes"
    set curTrack to current track
    --result: file track id 2703 of user playlist id 2425
    --        of source id 46 of application "iTunes"
    display dialog (name of curTrack as string)  -- "Shattered"
    next track -- play next song
    display dialog (name of curTrack as string) -- "Shattered"
end tell
```

Because `curTrack` is a specific `track` object, its name doesn’t change when the current track changes. But observe the result when using a reference to the current track:

```
tell application "iTunes"
    set trackRef to a reference to current track
    --result: current track of application "iTunes"
    display dialog (name of trackRef as string) -- "Shattered"
    next track -- play next song
    display dialog (name of trackRef as string) -- "Strange Days"
end tell
```

Because `trackRef` is a `reference` object containing an object specifier, the specifier identifies the new track when the current track changes.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW5"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1051"></a>

as (coercion)

The `as` operator converts, or *coerces*, a value of one class to a value of another class. Not all values are coercible to all classes; see [Coercion (Object Conversion)](../conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW21) for a list of allowed coercions.

The right-hand operand of `as` may be a single class, such as `text`, or a list of classes, such as `{integer, text}.` When given a list, the `as` operator processes the list from the first type to the last, checking if the value is an instance of that type; if one matches, the result is the original value. If none match, then it again processes the list from the first type to the last, attempting to coerce the value to that type; the result is the result of the first successful coercion. If none succeed, it throws an error.

> <a id="//apple_ref/doc/uid/TP40000983-CH5g-SW6"></a>
>
> **Note:** Coercing to a list of classes is supported in OS X Yosemite v10.10 and later.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-SW7"></a>

##### Examples

This expression returns `x` as a number, suitable for use with a math operator. For example, if `x` was the text `"1.5"`, it would return the `real` value `1.5`.

```
x as number
```

This expression returns `x` as either an integer or text, whichever succeeds first. For example, consider if `x` was `date "Wednesday, May 27, 2015 at 12:03:15 PM"`: `date` objects cannot be coerced to integers, but they can be coerced to text, so the result is the date as text: `"Wednesday, May 27, 2015 at 12:03:15 PM"`.

```
x as {integer, text}
```

The way lists of classes are processed means that the result of `as` can depend on the order of the classes. For example, the result of `1.5 as {integer, text}` is `2`, but `1.5 as {text, integer}` is `"1.5"`. It is also possible to have types that will never be reached. For example, in the expression `x as {number, integer}`, the `integer` coercion will never trigger, because `number` will always succeed first.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125019"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1052"></a>

contains, is contained by

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1053"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1054"></a>The `contains` and `is contained by` operators work with lists, records, and `text` objects.

[Table 9-1](#//apple_ref/doc/uid/TP40000983-CH5g-SW2) summarizes the use of these operators and their synonyms.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125052"></a>

##### list

A list `contains` another list if the right-hand list is a sublist of the left-hand list. A sublist is a list whose items appear in the same order and have the same values as any series of items in the other list. For example, the following statement is `true` because `1 + 1` evaluates to `2`, so that all the items in the right-hand list appear, in the same order, in the left-hand list:

```
{ "this", "is", 1 + 1, "cool" } contains { "is", 2 }
```

The following statement is `false` because the items in the right-hand list are not in the same order as the matching items in the left-hand list:

```
{ "this", "is", 2, "cool" } contains { 2, "is" }
```

A list `is contained by` another list if the left-hand list is a sublist of the right-hand list. For example, the following expression is `true`:

```
{ "is", 2} is contained by { "this", "is", 2, "cool" }
```

Both `contains` and `is contained by` work if the sublist is a single value—as with the concatenation operator (`&`), single values are coerced to one-item lists. For example, both of the following expressions evaluate to `true`:

```
{ "this", "is", 2, "cool" } contains 2
2 is contained by { "this", "is", 2, "cool" }
```

However, the following expressions, containing nested lists, both evaluate to false:

```
{"this", "is", {2}, "cool"} contains 2 -- false
{"this", "is", {2}, "cool"} contains {2} -- false
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125159"></a>

##### record

A record contains another record if all the properties in the right-hand record are included in the left-hand record, and the values of properties in the right-hand record are equal to the values of the corresponding properties in the left-hand record. A record is contained by another record if all the properties in the left-hand record are included in the right-hand record, and the values of the properties in the left-hand record are equal to the values of the corresponding properties in the right-hand record. The order in which the properties appear does not matter. For example, the following is `true`:

```
{ name:"Matt", mileage:"8000", description:"fast"} ¬
    contains { description:"fast", name:"Matt" }
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-125200"></a>

##### text

A `text` object contains another `text` object if the characters in the right-hand `text` object are equal to any contiguous series of characters in the left-hand `text` object. For example,

```
"operand" contains "era"
```

is `true`, but

```
"operand" contains "dna"
```

is `false`.

A `text` object is contained by another `text` object if the characters in the left-hand `text` object are equal to any series of characters in the right-hand `text` object. For example, this statement is `true`:

```
"era" is contained by "operand"
```

Text comparisons can be affected by `considering` and `ignoring` statements, as described in the Text section of `equal, is not equal to`.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124095"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1055"></a>

equal, is not equal to

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1056"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1057"></a>The `equal` and `is not equal to` operators can handle operands of any class. Two expressions of different classes are generally not equal, although for scalar operands, such as booleans, integers, and reals, two operands are the same if they have the same value.

[Table 9-1](#//apple_ref/doc/uid/TP40000983-CH5g-SW2) summarizes the use of these operators and their synonyms.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124286"></a>

##### list

Two lists are equal if they both contain the same number of items and if the value of an item in one list is identical to the value of the item at the corresponding position in the other list:

```
{ 7, 23, "Hello" } = {7, 23, "Goodbye"} --result: false
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124374"></a>

##### record

Two records are equal if they both contain the same collection of properties and if the values of properties with the same label are equal. They are not equal if the records contain different collections of properties, or if the values of properties with the same label are not equal. The order in which properties are listed does not affect equality. For example, the following expression is `true`:

```
{ name:"Matt", mileage:"8000" } = { mileage:"8000", name:"Matt"}
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124567"></a>

##### text

Two `text` objects are equal if they are both the same series of characters. They are not equal if they are different series of characters. For related information, see the `text` class.

Text comparisons can be affected by `considering` and `ignoring` statements, which instruct AppleScript to selectively consider or ignore attributes of characters or types of characters. For example, unless you use an `ignoring` statement, AppleScript compares `text` objects by considering all characters and punctuation.

AppleScript does not distinguish uppercase from lowercase letters unless you use a `considering` statement to consider the `case` attribute. For example:

```
"DUMPtruck" is equal to "dumptruck" --result: true
considering case
    "DUMPtruck" is equal to "dumptruck" --result: false
end considering
```

When comparing two `text` objects, if the test is not enclosed in a `considering` or `ignoring` statement, then the comparison uses default values for considering and ignoring attributes (described in `considering / ignoring (text comparison)`).

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124619"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1058"></a>

greater than, less than

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1059"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1060"></a>The `greater than` and `less than` operators work with dates, integers, real numbers, and `text` objects.

[Table 9-1](#//apple_ref/doc/uid/TP40000983-CH5g-SW2) summarizes the use of these operators and their synonyms.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124652"></a>

##### date

A date is greater than another date if it represents a later time. A date is less than another date if it represents an earlier time.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124666"></a>

##### integer, real

An integer or a real number is greater than another integer or real number if it represents a larger number. It is less than another integer or real number if it represents a smaller number.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124694"></a>

##### text

To determine the ordering of two `text` objects, AppleScript uses the collation order set in the Language pane of International preferences. A `text` object is greater than (comes after) another `text` object based on the lexicographic ordering of the user’s language preference. With the preference set to English, the following two statements both evaluate to `true`:

```
"zebra" comes after "aardvark"
"zebra" > "aardvark"
```

The following two statements also evaluate to `true`:

```
"aardvark" comes before "zebra"
"aardvark" < "zebra"
```

Text comparisons can be affected by `considering` and `ignoring` statements, as described in the Text section of `equal, is not equal to`.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124884"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1061"></a>

starts with, ends with

<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1062"></a><a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1063"></a>The `starts with` and `ends with` operators work with lists and `text` objects.

[Table 9-1](#//apple_ref/doc/uid/TP40000983-CH5g-SW2) summarizes the use of these operators and their synonyms.

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124917"></a>

##### list

A list `starts with` the items in a second list if all the items in the second list are found at the beginning of the first list. A list `ends with` the items in a second list if all the items in the second list are found at the end of the first list. For example, the following three expressions are all `true`:

```
{ "this", "is", 2, "cool" } ends with "cool"
{ "this", "is", 2, "cool" } starts with "this"
{ "this", "is", 2, "cool" } starts with { "this", "is" }
```

<a id="//apple_ref/doc/uid/TP40000983-CH5g-124958"></a>

##### text

A `text` object `starts with` the text in a second `text` object if all the characters in the second object are found at the beginning of the first object. A `text` object `ends with` the text in a second `text` object if all the characters in the second object are found at the end of the first object. For example, the following expression is `true`:

```
"operand" starts with "opera"
```

A `text` object ends with another `text` object if the characters in the right-hand `text` object are the same as the characters at the end of the left-hand `text` object. For example, the following expression is `true`:

```
"operand" ends with "and"
```

Text comparisons can be affected by `considering` and `ignoring` statements, as described in the Text section of `equal, is not equal to`.<a id="//apple_ref/doc/uid/TP40000983-CH5g-DontLinkElementID_1064"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
