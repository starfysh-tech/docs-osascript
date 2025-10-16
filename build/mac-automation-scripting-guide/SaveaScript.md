## Saving a Script

After you write a script, you can save it for future reference or to be run outside of Script Editor.

### Saving a Script or Script Bundle

Scripts and script bundles open in Script Editor when double-clicked in the Finder.

**To save a script or script bundle**

1. Choose File > Save (or press Command-S) to display the save dialog.
2. Type a name for the script and choose an output folder.
3. Choose Script or Script Bundle from the File Format popup menu.

   ![image: ../Art/scripteditor_save_dialog_scriptformat_2x.png](Art/scripteditor_save_dialog_scriptformat_2x.png)
4. Click Save.

### Saving a Script Application

Script applications, known as applets, work like other apps on your Mac. Double-click an applet to run it.

**To save an applet**

1. Choose File > Save (or press Command-S) to display the save dialog.
2. Type a name for the applet and choose an output folder.
3. Choose Application from the File Format popup menu.

   ![image: ../Art/scripteditor_save_dialog_appformat_2x.png](Art/scripteditor_save_dialog_appformat_2x.png)
4. If you want the script’s description—defined in the Accessory View pane—to display when the applet launches, select the “Show startup screen” checkbox.
5. If you want to create a stay-open applet, select the “Stay open after run handler” checkbox.
6. Click Save.

> **Note**
>
>
> To open a saved script applet or droplet for editing, drag it onto the Script Editor app or choose File > Open in Script Editor.
>
> To convert a previously saved script or script bundle to an applet, choose File > Duplicate, press Shift-Command-S, or choose File > Export. Then, perform the steps above.
>
> If an AppleScript applet contains an `open` event handler, or a JavaScript applet contains an `openDocuments` function, it automatically becomes a drag and drop application known as a droplet. Drag files and folders onto the droplet to process them, or double-click the droplet to run it. To learn about creating droplets, see [Processing Dropped Files and Folders](ProcessDroppedFilesandFolders.md#//apple_ref/doc/uid/TP40016239-CH53-SW1).

### Protecting a Script’s Source Code

If you plan to distribute your script, you may wish to protect is source code. This is done by exporting the script in run-only format.

**To save a script in run-only format**

1. Choose File > Export to display the export dialog.
2. Type a name for the applet and choose an output folder.
3. Choose a format from the File Format popup menu.
4. If you’re saving in application format, choose whether you want a startup screen or a stay-open script.
5. Select the Run-only checkbox.

   ![image: ../Art/scripteditor_export_dialog_runonly_2x.png](Art/scripteditor_export_dialog_runonly_2x.png)
6. Click Save.

Important

When saving a script in run-only format, make sure you retain a backup of your editable script.

### Code Signing a Script

By default, the security settings in OS X only allow the launching of apps (including applets and droplets) that have been created by you, downloaded from the Mac App Store, or created by developers identified by Apple. If you plan to distribute your scripts to others, you should consider code signing your scripts with an Apple developer ID.

You obtain a Developer ID certificate from [Certificates, Identifiers & Profiles](https://developer.apple.com/account/mac/certificate/) in your developer account and import it on your Mac. For detailed information about obtaining and importing a certificate, see Maintaining Your Signing Identities and Certificates in *App Distribution Guide*.

**To prepare a script application or bundle code signing**

1. If the Bundle Contents pane isn’t visible, choose View > Show Bundle, press Command-0, or click the bundle contents button (![image: ../Art/icon_bundlecontents_2x.png](Art/icon_bundlecontents_2x.png)) in the toolbar.
2. Make sure the following highlighted fields are populated in the Bundle Contents pane.

   ![image: ../Art/scripteditor_bundleinfo_codesigningfields_2x.png](Art/scripteditor_bundleinfo_codesigningfields_2x.png)
   * Name—The name of your script.
   * Identifier—A uniform type identifier for your script. For information, see *[Uniform Type Identifiers Overview](../../../FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319)*.
   * Short Version—The version number for your script.
   * Copyright—The copyright string for your script.

**To code sign a script**

1. Choose File > Export to display the export dialog.
2. Type a name for the applet and choose an output folder.
3. Choose a format from the File Format popup menu.
4. If you’re saving in application format, choose whether you want a startup screen or a stay-open script.
5. Choose whether you want to save the script as run-only.
6. Choose your developer identity from the Code Sign popup menu.

   ![image: ../Art/scripteditor_export_dialog_code_signing_2x.png](Art/scripteditor_export_dialog_code_signing_2x.png)
7. Click Save.
