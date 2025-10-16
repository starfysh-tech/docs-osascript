<a id="//apple_ref/doc/uid/TP40000983-CH213-SW1"></a>

# Glossary

* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW2"></a>**absolute object specifier**

  An object specifier that has enough information to identify an object or objects uniquely. For an object specifier to an application object to be complete, its outermost container must be the application itself. See [relative object specifier](#//apple_ref/doc/uid/TP40000983-CH213-SW95).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW3"></a>
  **Apple event**

  An interprocess message that encapsulates a command in a form that can be passed across process boundaries, performed, and responded to with a reply event. When an AppleScript script is executed, a statement that targets a scriptable application may result in an Apple event being sent to that application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW4"></a>**AppleScript**

  A scripting language that makes possible direct control of scriptable applications and scriptable parts of macOS.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW5"></a>**AppleScript command**

  A script command provided by AppleScript. AppleScript commands do not have to be included in `tell` statements.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW6"></a>**application command**

  A command that is defined by scriptable application to provide access to a scriptable feature. An application command must either be included in a `tell` statement or include the name of the application in its direct parameter.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW7"></a>**application object**

  An object stored in an application or its documents and managed by the application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW8"></a>**arbitrary reference form**

  A reference form that specifies an arbitrary object in a container.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW9"></a>**assignment statement**

  A statement that assigns a value to a variable. Assignment statements use the `copy` or `set` commands.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW10"></a>**attribute**

  A characteristic that can be considered or ignored in a `considering` or `ignoring` statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW11"></a>**binary operator**

  An operator that derives a new value from a pair of values.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW12"></a>**boolean**

  A logical truth value; see the `boolean` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW13"></a>**Boolean expression**

  An expression whose value can be either true or false.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW14"></a>**chevrons**

  See [double angle brackets](#//apple_ref/doc/uid/TP40000983-CH213-BBCFEEHB).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW15"></a>**child script object**

  A `script` object that inherits properties and handlers from another object, called the parent.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCGGDFI"></a>**class**

  (1) A category for objects that share characteristics such as properties and elements and respond to the same commands. (2) The label for the AppleScript `class` property—a reserved word that specifies the class to which an object belongs.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW54"></a>**coercion**

  The process of converting an object from one class to another. For example, an integer value can be coerced into a real value. Also, the software that performs such a conversion. Also known as object conversion.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW17"></a>**command**

  A word or series of words that requests an action. See also [handler](#//apple_ref/doc/uid/TP40000983-CH213-SW55).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW18"></a>**comment**

  Text that remains in a script after compilation but is ignored by AppleScript when the script is executed.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW19"></a>**compile**

  In AppleScript, to convert a script from the form typed into a script editor to a form that can be used by AppleScript. The process of compiling a script includes syntax and vocabulary checks. A script is compiled when you first run it and again when you modify it and then run it again, save it, or check its syntax.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW20"></a>**compiled script**

  The form to which a script is converted when you compile it.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW21"></a>**composite value**

  A value that contains other values. Lists, records, and strings are examples of composite values.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCICCIH"></a>**compound statement**

  A statement that occupies more than one line and contains other statements. A compound statement begins with a reserved word indicating its function and ends with the word `end`. See also [simple statement](#//apple_ref/doc/uid/TP40000983-CH213-BBCFBDBH).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW22"></a>**conditional statement**

  See [if statement](#//apple_ref/doc/uid/TP40000983-CH213-BBCGEIFI).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW23"></a>**considering statement**

  A control statement that lists a specific set of attributes to be considered when AppleScript performs operations on strings or sends commands to applications.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW24"></a>**constant**

  A reserved word with a predefined value; see the `constant` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW25"></a>**container**

  An object that contains one or more other objects, known as elements. You specify containers with the reserved words `of` or `in`.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW26"></a>**continuation character**

  A character used in Script Editor to extend a statement to the next line. With a U.S. keyboard, you can enter this character by typing Option-l (lower-case L).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW29"></a>**continue statement**

  A statement that controls when and how other statements are executed. AppleScript defines standard control statements such as `if`, `repeat`, and `while`.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW27"></a>**control statement**

  A statement that causes AppleScript to exit the current handler and transfer execution to the handler with the same name in the parent. A `continue` statement can also be used to invoke an inherited handler in the local context.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW28"></a>**current application**

  The application that is using the AppleScript component to compile and execute scripts (typically, Script Editor).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW117"></a>**current script**

  The script currently being executed.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW30"></a>**current target**

  The object that is the current default target for commands.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW31"></a>**data**

  A class used for data that do not belong to any of the other AppleScript classes; see the `data` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW32"></a>**date**

  A class that specifies a time, day of the month, month, and year; see the `date` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW33"></a>**declaration**

  The first occurrence of a variable or property identifier in a script. The form and location of the declaration determine how AppleScript treats the identifier in that script—for example, as a property, global variable, or local variable.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW34"></a>**default target**

  The object that receives a command if no object is specified or if the object is incompletely specified in the command. Default (or implicit) targets are specified in `tell` statements.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW35"></a>**delegation**

  The handing off of control to another object. In AppleScript, the use of a `continue` statement to call a handler in a parent object or the current application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW36"></a>**dialect**

  A version of the AppleScript language that resembles a specific human language or programming language. As of AppleScript 1.3, English is the only dialect supported.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW37"></a>**dictionary**

  The set of commands, objects, and other terminology that is understood by an application or other scriptable entity. You can display an application’s dictionary with Script Editor.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW38"></a>**direct parameter**

  The parameter immediately following a command, which typically specifies the object to which the command is sent.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCFEEHB"></a>**double angle brackets**

  Characters («») typically used by AppleScript to enclose raw data. With a U.S. keyboard, you can enter double angle brackets (also known as chevrons) by typing Option-Backslash and Shift-Option-Backslash.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW39"></a>**element**

  An object contained within another object. An object can typically contain zero or more of each of its elements.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW40"></a>**empty list**

  A list containing no items. See the `list` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW41"></a>**error expression**

  An expression, usually a `text` object, that describes an error.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW42"></a>**error handler**

  A collection of statements that are executed in response to an error message. See the `try` statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW43"></a>**error message**

  A message that is supplied by an application, by AppleScript, or by macOS when an error occurs during the handling of a command.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW44"></a>**error number**

  An integer that identifies an error.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW45"></a>**evaluation**

  The conversion of an expression to a value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW46"></a>**every reference form**

  A reference form that specifies every object of a particular type in a container.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW47"></a>**exit statement**

  A statement used in the body of a `repeat` statement to exit the Repeat statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW48"></a>**explicit run handler**

  A handler at the top level of a `script` object that begins with `on run` and ends with `end`. A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW49"></a>**expression**

  In AppleScript, any series of words that has a value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW50"></a>**filter**

  A phrase, added to a reference to a system or application object, that specifies elements in a container that match one or more conditions.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW51"></a>**filter reference form**

  A reference form that specifies all objects in a container that match a condition specified by a Boolean expression.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW52"></a>**formal parameter**

  See [parameter variable](#//apple_ref/doc/uid/TP40000983-CH213-BBCHJJBG).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW53"></a>**global variable**

  A variable that is available anywhere in the script in which it is defined.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW55"></a>**handler**

  A collection of statements that can be invoked by name. See also [command](#//apple_ref/doc/uid/TP40000983-CH213-SW17).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW56"></a>**identifier**

  A series of characters that identifies a value or handler in AppleScript. Identifiers are used to name variables, handlers, parameters, properties, and commands.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW57"></a>**ID reference form**

  A reference form that specifies an object by the value of its ID property.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCGEIFI"></a>**if statement**

  A control statement that contains one or more Boolean expressions whose results determine whether to execute other statements within the `if` statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW58"></a>**ignoring statement**

  A control statement that lists a specific set of attributes to be ignored when AppleScript performs operations on text strings or sends commands to applications.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW59"></a>**implicit run handler**

  All the statements at the top level of a script except for property definitions, `script` object definitions, and other handlers. A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW60"></a>**index reference form**

  A reference form that specifies an object by describing its position with respect to the beginning or end of a container.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW139"></a>**inheritance**

  The ability of a child `script` object to take on the properties and handlers of a parent object.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW62"></a>**inheritance chain**

  The hierarchy of objects that AppleScript searches to find the target for a command or the definition of a term.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW63"></a>**initializing a script object**

  The process of creating a `script` object from the properties and handlers listed in a `script` object definition. AppleScript creates a `script` object when it runs a script or handler that contains a `script` object definition.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW64"></a>**insertion point**

  A location where another object or objects can be added.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW65"></a>**integer**

  A positive or negative number without a fractional part; see the `integer` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW137"></a>**item**

  A value in a list or record. An item can be specified by its offset from the beginning or end of the list or record.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW66"></a>**keyword**

  A word that is part of the AppleScript language. Synonymous with [reserved word](#//apple_ref/doc/uid/TP40000983-CH213-SW99).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW67"></a>**labeled parameter**

  A parameter that is identified by a label. See also [positional parameter](#//apple_ref/doc/uid/TP40000983-CH213-BBCDAEBE).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW138"></a>**lifetime**

  The period of time over which a variable or property is in existence.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW68"></a>**list**

  An ordered collection of values; see the `list` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW69"></a>**literal**

  A value that evaluates to itself.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW70"></a>**local variable**

  A variable that is available only in the handler in which it is defined. Variables that are defined within handlers are local unless they are explicitly declared as global variables.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW71"></a>**log statement**

  A script statement that reports the value of one or more variables to the Event Log pane of a script window, and to the Event Log History window, if it is open.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW72"></a>**loop**

  A series of statements that is repeated.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW73"></a>**loop variable**

  A variable whose value controls the number of times the statements in a `repeat` statement are executed.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW74"></a>**middle reference form**

  A reference form that specifies the middle object of a particular class in a container. (This form is rarely used.)
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW75"></a>**name reference form**

  A reference form that specifies an object by name—that is, by the value of its `name` property.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW76"></a>**nested control statement**

  A control statement that is contained within another control statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW77"></a>**number**

  A synonym for the AppleScript classes `integer` and `real`.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW78"></a>**object**

  An instantiation of a class definition, which can include properties and actions.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW16"></a>**object conversion**

  See [coercion](#//apple_ref/doc/uid/TP40000983-CH213-SW54).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW79"></a>**object specifier**

  A phrase specifies the information needed to find another object in terms of the objects in which it is contained. See also [absolute object specifier](#//apple_ref/doc/uid/TP40000983-CH213-SW2), [relative object specifier](#//apple_ref/doc/uid/TP40000983-CH213-SW95), and [reference form](#//apple_ref/doc/uid/TP40000983-CH213-SW94).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW80"></a>**operand**

  An expression from which an operator derives a value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW81"></a>**operation**

  The evaluation of an expression that contains an operator.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW82"></a>**operator**

  A symbol, word, or phrase that derives a value from another value or pair of values.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW136"></a>**optional parameter**

  A parameter that need not be included for a command to be successful.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW83"></a>**outside property, variable, or statement**

  A property, variable, or statement in a `script` object but occurs outside of any handlers or nested `script` objects.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCHJJBG"></a>**parameter variable**

  An identifier in a handler definition that represents the actual value of a parameter when the handler is called. Also called a *formal parameter*.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW84"></a>**parent object**

  An object from which another `script` object, called the child, inherits properties and handlers. A parent object may be any object, such as a `list` or an `application` object, but it is typically another `script` object.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCDAEBE"></a>**positional parameter**

  A handler parameter that is identified by the order in which it is listed. In a handler call, positional parameters are enclosed in parentheses and separated by commas. They must be listed in the order in which they appear in the corresponding handler definition.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW85"></a>**property**

  A labeled container in which to store a value. Properties can specify characteristics of objects.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW86"></a>**property reference form**

  A reference form that specifies a property of an `application` object, `record` or `script` object.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW87"></a>**range reference form**

  A reference form that specifies a series of objects of the same class in the same container.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW88"></a>**raw format**

  AppleScript terms enclosed in double angle brackets, or chevrons («»). AppleScript uses raw format because it cannot find a script term in any available dictionary, or cannot display data in its native format.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW89"></a>**real**

  A number that can include a decimal fraction; see the `real` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW90"></a>**record**

  An unordered collection of properties, identified by unique labels; see the `record` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW91"></a>**recordable application**

  An application that uses Apple events to report user actions for recording purposes. When recording is turned on, Script Editor creates statements corresponding to any significant actions you perform in a recordable application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW92"></a>**recursive handler**

  A handler that calls itself.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW93"></a>**reference**

  An object that encapsulates an object specifier.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW94"></a>**reference form**

  The syntax for identifying an object or group of objects in an application or other container—that is, the syntax for constructing an object specifier. AppleScript defines reference forms for arbitrary, every, filter, ID, index, middle, name, property, range, and relative.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW95"></a>**relative object specifier**

  An object specifier that does not include enough information to identify an object or objects uniquely. When AppleScript encounters a partial object specifier, it uses the default object specified in the enclosing `tell` statement to complete the reference. See [absolute object specifier](#//apple_ref/doc/uid/TP40000983-CH213-SW2).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW96"></a>**relative reference form**

  A reference form that specifies an object or location by describing its position in relation to another object, known as the base, in the same container.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW97"></a>**repeat statement**

  A control statement that contains a series of statements to be repeated and, in most cases, instructions that specify when the repetition stops.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW98"></a>**required parameter**

  A parameter that must be included for a command to be successful.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW99"></a>**reserved word**

  A word that is part of the AppleScript language. Synonymous with [keyword](#//apple_ref/doc/uid/TP40000983-CH213-SW66).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW100"></a>**result**

  A value generated when a command is executed or an expression evaluated.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW61"></a>**return statement**

  A statement that exits a handler and optionally returns a specified value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW101"></a>**scope**

  The range over which AppleScript recognizes a variable or property, which determines where else in a script you may refer to that variable or property.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW102"></a>**script**

  A series of written instructions that, when executed, cause actions in applications or macOS.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW103"></a>**scriptable application**

  An application that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, called Apple events, sent when a script command targets the application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW104"></a>**script application**

  An application whose only function is to run the script associated with it.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW106"></a>**script editor**

  An application used to create and modify scripts.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW107"></a>**Script Editor**

  The script-editing application distributed with AppleScript.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW108"></a>**scripting addition**

  A file that provides additional commands or coercions you can use in scripts. If a scripting addition is located in the Scripting Additions folder, its terminology is available for use by any script.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW140"></a>**scripting addition command**

  A command that is implemented as a scripting addition.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW126"></a>**script library**

  A script saved in a Script Libraries folder so it can be used by other scripts.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW109"></a>**script object**

  A user-defined object that can combine data (in the form of properties) and actions (in the form of handlers and additional `script` objects).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW110"></a>**script object definition**

  A compound statement that contains a collection of properties, handlers, and other AppleScript statements.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-BBCFBDBH"></a>**simple statement**

  One that can be written on a single line. See also [compound statement](#//apple_ref/doc/uid/TP40000983-CH213-BBCICCIH).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW112"></a>**simple value**

  A value, such as an integer or a constant, that does not contain other values.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW116"></a>**Standard suite**

  A set of standard AppleScript terminology that a scriptable application should support if possible. The Standard suite contains commands such as `count`, `delete`, `duplicate`, and `make`, and classes such as `application`, `document`, and `window`.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW105"></a>**statement**

  A series of lexical elements that follows a particular AppleScript syntax. Statements can include keywords, variables, operators, constants, expressions, and so on. See also [compound statement](#//apple_ref/doc/uid/TP40000983-CH213-BBCICCIH), [simple statement](#//apple_ref/doc/uid/TP40000983-CH213-BBCFBDBH).
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW113"></a>**statement block**

  One or more statements enclosed in a compound statement and having an `end` statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW114"></a>**string**

  A synonym for the `text` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW115"></a>**styled text**

  Text that may include style and font information. Not supported in AppleScript 2.0.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW132"></a>**suite**

  Within an application's scriptability information, a grouping of terms associated with related operations.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW118"></a>**synonym**

  An AppleScript word, phrase, or language element that has the same meaning as another AppleScript word, phrase, or language element. For example, the operator `does not equal` is a synonym for `≠`.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW119"></a>**syntax**

  The arrangement of words in an AppleScript statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW120"></a>**syntax description**

  The rules for constructing a valid AppleScript statement of a particular type.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW121"></a>**system object**

  An object that is part of a scriptable element of macOS.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW122"></a>**target**

  The recipient of a command. Potential targets include `application` objects, `script` objects (including the current script), and the current application.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW123"></a>**tell statement**

  A control statement that specifies the default target for the statements it contains.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW124"></a>**test**

  A Boolean expression that specifies the conditions of a filter or an `if` statement.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW125"></a>**text**

  An ordered series of characters (a text string); see the `text` class.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW127"></a>**try statement**

  A two-part compound statement that contains a series of AppleScript statements, followed by an error handler to be invoked if any of those statements cause an error.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW128"></a>**unary operator**

  An operator that derives a new value from a single value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW129"></a>**Unicode**

  An international standard that uses a 16-bit encoding to uniquely specify the characters and symbols for all commonly used languages.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW141"></a>**Unicode code point**

  A unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW130"></a>**Unicode text**

  A class that represents an ordered series of two-byte Unicode characters.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW142"></a>**use statement**

  A control statement that declares a required resource for a script and may import terminology from that resource.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW131"></a>**user-defined command**

  A command that is implemented by a handler defined in a `script` object.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW111"></a>**using terms from statement**

  A control statement that instructs AppleScript to use the terminology from the specified application in compiling the enclosed statements.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW133"></a>**variable**

  A named container in which to store a value.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW134"></a>**with timeout statement**

  A control statement that specifies the amount of time AppleScript waits for application commands to complete before stopping execution of the script.
  
* <a id="//apple_ref/doc/uid/TP40000983-CH213-SW135"></a>**with transaction statement**

  A control statement that allows you to take advantage of applications that support the notion of a transaction—a sequence of related events that should be performed as if they were a single operation, such that either all of the changes are applied or none are.
  

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
