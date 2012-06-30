kf8-region-mag
==============

Python script to insert region mag areas to KF8 files

  * Requires Python3 and BeautifulSoup 4
  * Very early stages
  * Currently only inserts the json/div structure into html files
  * Requires each textblock to be wrapped in a div with unique class that follows a pattern (currently pg\_#\_mag\_# but could be anything)
  * Takes the unique class and makes it the source ID for the inner div, with the < a > tag.
  * Inserts ordinals going down the html tree. If this isn't write you may have to adjust.
 
 
To be added

  * Target divs into HTML
  * Target div css into stylesheet
  * Positioning will be x&y of source div minus 5% (as in the Kindle sample file)
  * Likely might need some cleaning up after