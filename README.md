# FlySmart-Helper-scripts
scripts to carry out some functions in managing and updating FlySmart application

### Airport_Database_Editor.py
Airport_Database_Editor.py is a script that makes the following edits to an AODB from Navblue:
1. updates the landing distance of any runway affected by a temporary notam such that the runway is shortened. (If the runway is lengthened no change is made)
2. if the Engine fail procedure is non standard, the EFP is copied to the landing page for reference
3. if the EFP is standard, the standard wording is written in the EFP box on the takepff page


Airbus_extract_NO_STD_EFP-AIRCON.AIRBUS.A330.210521_165743.txt is a sample AODB to carry out Airport_Database_editor.py on


### FlySmart Tester.py
FlySmart Tester.py is a script that tests an output from FlySmart and helps the user do a comparison calaulation in PEP


GHJ-21-521-182419.xml is a sample FlySmart output that can be tested
