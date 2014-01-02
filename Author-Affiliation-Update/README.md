Author Affiliation Update Scripts
============

These scripts are meant to work as part of a work flow for updating incorrect author and affiliation information in ADS.

###Get-Authors-Affiliations-from-Bibcode-uses-XML.py
This uses the XML version of the ADS abstract displays to capture the author and affiliation data. It was discovered that the affiliation information was not ordered correctly using the API, so this was a work around.  This does not require an API dev key.
This script capture the author and affiliation information, and then writes the information to a CSV in a format where an authors name appears in the cell above his or her affiliation (when opened in MS Excel)

###Interim Work Flow Steps
Example Output from the above python script:
%R		1992NuPhA.540..599K					
%T		Inelastic neutrino scattering on 12C and 16O above the particle emission threshold					
%A		Kolbe, E.								Langanke, K.		
%F		Institut für Theoretische Physik		Institut für Theoretische Physik

To mark a bibcode for addition to the CfA Bibliography, in the cell to the right of the bibcode, write: x
To mark updates for the author and affiliation information, write a "c" just after, and in the same cell as, the %R, %A, %F.

######Example Mark-Ups:
%Rc		1992NuPhA.540..599K		x
%T		Inelastic neutrino scattering on 12C and 16O above the particle emission threshold					
%Ac		Kolbe, E.								Langanke, K.		
%Fc		Institut für Theoretische Physik		Institut für Theoretische Physik
With these mark-ups, this entry would be added to the CfA bibliography, and the author/affiliation information would be updated.

######Important Note:
To save the file, do NOT simply click on the save icon.  Always make sure you go to "Save File As..." and choose CSV (Comma delimited) (*.csv).  Saving it without being careful to "save as" causes weird formatting issues and problems with the unicode characters.  I may try to fix this so its not so touchy, but not likely any time soon because I do not even know where to start, and it works well enough as is.  Do not change the file name when saving, unless you want to also edit the file name in the outputs python script.

###Outputs-for-CfA-bib-updates.py
This looks at the file edited using the above Interim Work Flow Steps, and creates two new text files to be submitted to ADS for approval.  One lists corrected author and affiliation info marked for updated in the ADS, and another lists all bibcodes marked for addition into the CfA bibliography.  These output files will be date and time stamped, to the second, of when the script was run.

######Final Notes:
These scripts, if the interim steps are compelted and saved properly, should preserve special characters such as umlauts and the like.